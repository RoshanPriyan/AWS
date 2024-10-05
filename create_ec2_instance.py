import boto3

aws_management_console = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2_console = aws_management_console.client(service_name="ec2")

response = ec2_console.run_instances(
    ImageId='ami-0ebfd941bbafe70c6',  # Specify the AMI ID
    InstanceType='t2.micro',          # Choose an instance type
    MaxCount=1,                       # Max number of instances
    MinCount=1,                       # Min number of instances
)