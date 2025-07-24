import json
from utils import auth, db
from botocore.exceptions import ClientError

def handler(event, context):