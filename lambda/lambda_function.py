import os
import logging
import jsonpickle
import boto3
import random

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create an S3 client
s3 = boto3.client("s3")
bucket_name = (
    "my-bucket"  # os.environ["BUCKET_NAME"]  # Supplied by Function service-discovery wire
)


def lambda_handler(event, context):
    logger.info("## ENVIRONMENT VARIABLES\r" + jsonpickle.encode(dict(**os.environ)))
    logger.info("## EVENT\r" + jsonpickle.encode(event))
    logger.info("## CONTEXT\r" + jsonpickle.encode(context))
    # Add a file to your Object Store
    length = random.randint(1, 100)
    response = s3.put_object(
        Bucket=bucket_name, Key=random_word(length), Body=str(length), ACL="public-read"
    )
    return response


def random_word(length):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(letters) for i in range(length))
