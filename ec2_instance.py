import boto3

aws_management_console = boto3.session.Session(profile_name="default")
ec2_console = aws_management_console.client(service_name="ec2")

instance = ec2_console.describe_instances()
print(instance)