#lambda function to get contacts for a user by authentication, then db.get_contacts
import json
from backend.functions.utils import auth,db
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    try:
        #first authenticate the token
        token=event['headers'].get('Authorization', None).replace('Bearer ', '')
        if not token:
            return {
                'statusCode': 401,
                'body': json.dumps({'error': 'Unauthorized'})
            }
        payload = auth.verify_access_token(token)
        if not payload:
            return {
                'statusCode': 401,
                'body': json.dumps({'error': 'Invalid or expired token'})
            }
        
        #get user_id from token
        user_id = payload.get('user_id')
        if not user_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'User ID not found in token'})
            }
        
        #fetch contacts from the database
        contacts = db.get_contacts(user_id)
        if not contacts:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'No contacts found'})
            }
        
        #return the contacts
        print(f"Contacts fetched for user {user_id}: {contacts}")
        return {
            'statusCode': 200,
            'body': json.dumps({'contacts': contacts})
        }
    except ClientError as e:
        print(f"Error fetching contacts: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }

#example usage
# eg_token = auth.create_access_token({'user_id': '123456'})
# sample_event = {
#     'headers': { 'Authorization': f"Bearer {eg_token}" }
#     }

# response=lambda_handler(sample_event, None)  
# print('Status Code:', response['statusCode'])
# print('Response Body:', response['body'])