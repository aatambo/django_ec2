import os

import boto3
from dotenv import load_dotenv

from .utils import create_dynamo_table

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


def insert_into_dynamo_table(filename, fileurl, filesize):
    # create table if not exists
    try:
        create_dynamo_table()
    except:
        pass

    # use table
    table = dynamo_client.Table("shareitfiles")
    table.put_item(
        Item={
            "Name": filename,
            "Url": fileurl,
            "Size": filesize,
        }
    )
