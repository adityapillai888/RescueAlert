import json
from backend.functions.utils import auth, db
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        body=json.loads(event.get('body', '{}'))
        username = body.get('user_id')
        password = body.get('password')
        email = body.get('email')

        if not username or not password or not email:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required fields'})
            }
        # Check if user already exists
        if db.get_user(username):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'User already exists'})
            }
        
        # Hash the password
        hashed_pw = auth.hash_password(password)

        #add user to the database
        db.insert_user(username, {
            "email": email,
            "password": hashed_pw
        })

        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'User registered successfully'})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }

# Example usage   
# event = {
#     "body": json.dumps({
#         "user_id": "testuser123",
#         "password": "TestPass@123",
#         "email": "testuser@example.com"
#     })
# }

# response = lambda_handler(event, None)
# print("Status Code:", response["statusCode"])
# print("Response Body:", response["body"])