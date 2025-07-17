import boto3
from botocore.exceptions import ClientError
dynamodb=boto3.resource('dynamodb',region_name='ap-south-1')

def table_exists(table_name):
    try:
        table = dynamodb.Table(table_name)
        table.load()  # Triggers a call to check if table exists
        print(f"🔁 Table '{table_name}' already exists.")
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            return False
        else:
            raise

def create_users_table():
    if not table_exists('Users'):
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
