import json
from backend.functions.utils import auth, db
from botocore.exceptions import ClientError

#handler for user login
def lambda_handler(event, context):
    try:
        body=json.loads(event.get('body', '{}'))
        username=body.get('user_id')
        password=body.get('password')

        if not username or not password:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required fields'})
            }
        
        #authenticate user
        info= db.get_user(username)
        if not info:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }  
        else:
            if not auth.verify_password(password, info['password']):
                return {
                    'statusCode': 401,
                    'body': json.dumps({'message': 'Invalid credentials'})
                }
            else:
                #create access token
                access_token=auth.create_access_token(data={"user_id": username})
                return {
                    'statusCode': 200,
                    'body': json.dumps({'access_token': access_token})
                }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }
    

#example usage for valid login
# event = {
#     "body": json.dumps({
#         "user_id": "testuser123","password": "TestPass@123"})
# }
# response = lambda_handler(event, None)
# print("Status Code:", response["statusCode"])
# print("Response Body:", response["body"])


# Example usage for invalid login
# event = {
#     "body": json.dumps({
#         "user_id": "testuser123",
#         "password": "WrongPass@123"
#     })
# }
# response = lambda_handler(event, None)
# print("Status Code:", response["statusCode"])
# print("Response Body:", response["body"])
