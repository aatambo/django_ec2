import os

import boto3

# from django.core.mail import send_mail
from dotenv import load_dotenv

# load .env
load_dotenv()

aws_access_key_id = os.getenv("AWS_S3_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_S3_SECRET_ACCESS_KEY")

# resource
dynamo_client = boto3.resource(
    "dynamodb",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name="us-east-1",
)


def create_dynamo_table():
    table = dynamo_client.create_table(
        TableName="shareitfiles",
        KeySchema=[
            {"AttributeName": "Name", "KeyType": "HASH"},
            {"AttributeName": "Url", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "Name", "AttributeType": "S"},
            {"AttributeName": "Url", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )

    # Wait until the table exists.
    table.wait_until_exists()
