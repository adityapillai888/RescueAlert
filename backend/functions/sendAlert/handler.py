import json
from backend.functions.utils import auth, db
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    
    #authenticate the token
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
    user_id = payload.get('user_id')
    if not user_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'User ID not found in token'})
        }
    #get contacts
    contacts = db.get_contacts(user_id)
    if not contacts:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'No contacts found'})
        }
    
    #send alert code(not written yet due to AWS sns and ses costing money)
    for contact in contacts:
        try:
            # Here you would implement the logic to send the alert
            # For example, using AWS SNS or SES to send an email or SMS
            pass  # Replace with actual sending logic
        except ClientError as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': f'Failed to send alert to {contact}: {str(e)}'})
            }
#example usage       
    
