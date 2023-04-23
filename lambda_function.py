from urllib.parse import unquote_plus

import boto3


import json




def label_function(bucket, name):
    """This takes an S3 bucket and a image name!"""
    print(f"This is the bucketname {bucket} !")
    print(f"This is the imagename {name} !")
    """
    rekognition = boto3.client("rekognition", region_name="us-east-2")
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": name,
            }
        },
    )
    labels = response["Labels"]
    print(f"I found these labels {labels}")
    """
    labels = ["we are debugging :)", "pipeline > service :)"]
    return labels


def lambda_handler(event, context):
    """This is a computer vision lambda handler"""

    """
    print(f"This is my S3 event {event}")
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        print(f"This is my bucket {bucket}")
        key = unquote_plus(record["s3"]["object"]["key"])
        print(f"This is my key {key}")

    my_labels = label_function(bucket=bucket, name=key)
    return my_labels
    """

    result = {
        'status': 'debug',
        'this_': 'did work tho',
    }
    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(result),
    }
    return response
