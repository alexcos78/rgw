#!/usr/bin/env python3

import boto3
import os

OIDC_ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")

print(OIDC_ACCESS_TOKEN)

sts_client = boto3.client('sts',
    endpoint_url="https://<RGW_HOSTNAME>",
    region_name=''
    )

response = sts_client.assume_role_with_web_identity(
    RoleArn="arn:aws:iam:::role/IAMaccess",
    RoleSessionName="test1",
    DurationSeconds=3600,
    WebIdentityToken=OIDC_ACCESS_TOKEN )


s3client = boto3.client('s3',
    aws_access_key_id = response['Credentials']['AccessKeyId'],
    aws_secret_access_key = response['Credentials']['SecretAccessKey'],
    aws_session_token = response['Credentials']['SessionToken'],
    endpoint_url="https://<RGW_HOSTNAME>",
    region_name='default',)

bucket_name = '<BUCKET_NAME>'
s3bucket = s3client.delete_bucket(Bucket=bucket_name)

resp = s3client.list_buckets()
print(resp)
