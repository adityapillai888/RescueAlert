import boto3
from botocore.exceptions import ClientError
dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')

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
                                    KeySchema=[{'AttributeName':'contact_id','KeyType':'HASH'}],
                                    AttributeDefinitions=[{'AttributeName':'contact_id','AttributeType':'S'}],
                                    ProvisionedThroughput={'ReadCapacityUnits': 1, 'WriteCapacityUnits': 1}      
                                    )
        print("creating Contacts table..")
        table.wait_until_exists()
        print("Contacts table created successfully ")

def create_logs_table():
    if not table_exists('Logs'):
        dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')
        table=dynamodb.create_table(TableName='Logs',
                                    KeySchema=[{'AttributeName':'log_id','KeyType':'HASH'}],
                                    AttributeDefinitions=[{'AttributeName':'log_id','AttributeType':'S'}],
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

