#!/usr/bin/env python3

import boto3

iam_client = boto3.client('iam', aws_access_key_id="<RGW_LOCAL_USER>", aws_secret_access_key="<RGW_SECRET>", endpoint_url="https://<RGW_ENDPOINT>", region_name='')

oidc_response = iam_client.create_open_id_connect_provider(
    Url='https://<IAM_HOSTNAME>/',
    ClientIDList=['object'],
    ThumbprintList=['<THUMBPRINT>']
)

oidc_response = iam_client.list_open_id_connect_providers()

oidc_response = iam_client.get_open_id_connect_provider(
    OpenIDConnectProviderArn='arn:aws:iam:::oidc-provider/<IAM_HOSTNAME>/'
)

oidc_response = iam_client.delete_open_id_connect_provider(
    OpenIDConnectProviderArn='arn:aws:iam:::oidc-provider/<IAM_HOSTNAME>/'
)

print (oidc_response)
