import boto3
from botocore.exceptions import ClientError
dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
from boto3.dynamodb.conditions import Key

def table_exists(table_name):
    try:
        table = dynamodb.Table(table_name)
        table.load()  # Triggers a call to check if table exists
        print(f"Table '{table_name}' already exists.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            return False
        else:
            raise

def create_users_table():
    if not table_exists('Users'):
        dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
        table=dynamodb.create_table(TableName='Users',
                                    KeySchema=[{'AttributeName':'user_id','KeyType':'HASH'}],
                                    AttributeDefinitions=[{'AttributeName':'user_id','AttributeType':'S'}],
                                    ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}      
                                    )
        print("creating Users table..")
        table.wait_until_exists()
        print("Users table created successfully ")

def create_contacts_table():
    if not table_exists('Contacts'):
        dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
        table=dynamodb.create_table(TableName='Contacts',
                                    KeySchema=[{'AttributeName':'user_id','KeyType':'HASH'},
                                                {'AttributeName':'contact_id','KeyType':'RANGE'}],
                                    AttributeDefinitions=[{'AttributeName':'user_id','AttributeType':'S'},
                                                          {'AttributeName':'contact_id','AttributeType':'S'}],
                                    ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}      
                                    )
        print("creating Contacts table..")
        table.wait_until_exists()
        print("Contacts table created successfully ")

def create_logs_table():
    if not table_exists('Logs'):
        dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
        table=dynamodb.create_table(TableName='Logs',
                                    KeySchema=[{'AttributeName':'user_id','KeyType':'HASH'},
                                                {'AttributeName':'log_id','KeyType':'RANGE'}],
                                    AttributeDefinitions=[{'AttributeName':'user_id','AttributeType':'S'},
                                                          {'AttributeName':'log_id','AttributeType':'S'}],
                                    ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}      
                                    )
        print("creating Logs table..")
        table.wait_until_exists()
        print("Logs table created successfully ")
    
#create tables
if __name__=="__main__":
    create_users_table()
    create_contacts_table()
    create_logs_table()


def insert_user(user_id, user_data):
    dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
    table = dynamodb.Table('Users')
    table.put_item(Item={'user_id': user_id, **user_data})
    print(f"User {user_id} inserted successfully.")

def insert_contact(contact_id, contact_data):
    dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
    table = dynamodb.Table('Contacts')
    table.put_item(Item={'contact_id': contact_id, **contact_data})
    print(f"Contact {contact_id} inserted successfully.")

def insert_log(log_id, log_data):
    dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
    table = dynamodb.Table('Logs')
    table.put_item(Item={'log_id': log_id, **log_data})
    print(f"Log {log_id} inserted successfully.")

# Example usage of insertion functions
# insert_user('user123', {'name': 'John Doe', 'email': 'bla@bla'})
# insert_contact('contact123', {'user_id': 'user123', 'name': 'Jane Doe', 'phone': '1234567890'})
# insert_log('log123', {'user_id': 'user123', 'action': 'login', 'timestamp': '2023-10-01T12:00:00Z'})


def get_user(user_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Users')
    response = table.get_item(Key={'user_id': user_id})
    return response.get('Item', None)

def get_contacts(user_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Contacts')
    response = table.query(
        KeyConditionExpression=Key('user_id').eq(user_id)
    )
    return response.get('Items', [])
def get_logs(user_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Logs')
    response = table.query(
        KeyConditionExpression=Key('user_id').eq(user_id)
    )
    return response.get('Items', [])
# Example usage of retrieval functions
# user = get_user('user123')
# contacts = get_contacts('user123')
# logs = get_logs('user123')
# print(user)
# print(contacts) 
# print(logs)

def delete_user(user_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Users')
    table.delete_item(Key={'user_id': user_id})
    print(f"User {user_id} deleted successfully.")

def delete_contact(user_id, contact_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Contacts')
    table.delete_item(Key={'user_id': user_id, 'contact_id': contact_id})
    print(f"Contact {contact_id} for user {user_id} deleted successfully.")

def delete_log(user_id, log_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Logs')
    table.delete_item(Key={'user_id': user_id, 'log_id': log_id})
    print(f"Log {log_id} for user {user_id} deleted successfully.")

# Example usage of deletion functions
# delete_user('user123')
# delete_contact('user123', 'contact123')
# delete_log('user123', 'log123')

