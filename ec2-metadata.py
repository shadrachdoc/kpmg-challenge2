import boto3
import json

client = boto3.client('ec2')

response = client.describe_instances()

print(json.dumps(response, indent=2, default=str))

