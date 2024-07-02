#!/usr/bin/env python3

import boto3

iam_client = boto3.client('iam', aws_access_key_id="RGWCNAFTB", aws_secret_access_key="HHpb1vMjWo7TVBUhWh3IaOsoElF1Tk3abtldphZ7", endpoint_url="https://ceph-osd01.cloud.cnaf.infn.it:7480", region_name='')


policy_document = '''{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"Federated":["arn:aws:iam:::oidc-provider/iam-pilota.cloud.cnaf.infn.it/"]},"Action":["sts:AssumeRoleWithWebIdentity","sts:TagSession"]}]}'''

role_response = iam_client.create_role(
    AssumeRolePolicyDocument=policy_document,
    Path='/',
    RoleName='IAMaccess',
    )

role_policy = '''{"Version":"2012-10-17","Statement":{"Effect":"Allow","Action":"s3:*","Resource":"arn:aws:s3:::*"}}'''

response = iam_client.put_role_policy(
    RoleName='IAMaccess',
    PolicyName='IAMpolicy',
    PolicyDocument=role_policy
    )
