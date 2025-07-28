# import json
# import boto3
# import os

# sns = boto3.client('sns', region_name='ap-south-1')  # Change if using a different region

# def lambda_handler(event, context):
#     try:
#         # Get phone number and message from request
#         body = json.loads(event.get('body', '{}'))
#         phone_number = body.get('phone_number')
#         message = body.get('message', 'Emergency Alert!')

#         if not phone_number:
#             return {
#                 'statusCode': 400,
#                 'body': json.dumps({'error': 'Phone number is required'})
#             }

#         # Send SMS
#         sns.publish(
#             PhoneNumber=phone_number,
#             Message=message
#         )

#         return {
#             'statusCode': 200,
#             'body': json.dumps({'message': 'SMS sent successfully'})
#         }

#     except Exception as e:
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': str(e)})
#         }
