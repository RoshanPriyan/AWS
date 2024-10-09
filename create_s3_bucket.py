import boto3

s3_client = boto3.client('s3', region_name="us-east-1")
response = s3_client.create_bucket(
    ACL='private',
    Bucket='botoroshanbucket' # unique name
)
print(response)
