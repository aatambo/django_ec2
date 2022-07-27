import json
import os

import boto3
from dotenv import load_dotenv

# load .env
load_dotenv()

aws_access_key_id = os.getenv("AWS_S3_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_S3_SECRET_ACCESS_KEY")
sender = os.getenv("EMAIL")

# client
lambda_client = boto3.client(
    "lambda",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name="us-east-1",
)


def invoke_lambda(user, link, recipients):
    params = {
        "aws_access_key_id": aws_access_key_id,
        "aws_secret_access_key": aws_secret_access_key,
        "user": user,
        "link": link,
        "sender": sender,
        "recipients": recipients,
    }
    lambda_client.invoke(
        FunctionName="email-send-handler",
        Payload=json.dumps(params),
    )
