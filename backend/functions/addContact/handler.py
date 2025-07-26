#accepts a POST request with a contact's details, authenticates the token, then add contacts if they dont already exist
import json
from backend.functions.utils import auth, db
from botocore.exceptions import ClientError


def lambda_handler(event, context):
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
    
    #add contacts 
    user_id = payload.get('user_id')
    if not user_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User ID not found in token'})
        }
    try:
        body = json.loads(event['body'])
        contact_name = body.get('name')
        contact_email = body.get('email')
        contact_number = body.get('number')
        contact_relation= body.get('relation', 'friend')  # default to 'friend' if not provided
        
        if not contact_name or not contact_email:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Name and email are required'})
            }
        
        #check if the contact already exists
        existing_contacts = db.get_contacts(user_id)
        for contact in existing_contacts:
            if contact.get('number') == contact_number or contact.get('email') == contact_email:

                return {
                    'statusCode': 409,
                    'body': json.dumps({'error': 'Contact already exists'})
                }

        
        
        #add the new contact
        contact_id = f"{user_id}_{contact_name.replace(' ', '_').lower()}"
        contact_data = {
            'user_id': user_id,
            'name': contact_name,
            'email': contact_email,
            'number': contact_number,
            'relation': contact_relation
        }
        db.insert_contact(contact_id, contact_data)
        
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Contact added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

# Example usage:
# eg_token = auth.create_access_token({'user_id': '12345'})
# sample_event = {
#     'headers': { 'Authorization': f"Bearer {eg_token}" },
#     'body': json.dumps({
#         'name': 'John Doe',
#         'email': 'johndoe@bla',
#         'number': '1234567890',
#         'relation': 'friend'
#     })
# }
# response=lambda_handler(sample_event, None)  
# print('Status Code:', response['statusCode'])
# print('Response Body:', response['body'])