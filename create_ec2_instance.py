import boto3

aws_management_console = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2_console = aws_management_console.client(service_name="ec2")

response = ec2_console.run_instances(
    ImageId='ami-0ebfd941bbafe70c6',  # Specify the AMI ID
    InstanceType='t2.micro',          # Choose an instance type
    MaxCount=1,                       # Max number of instances
    MinCount=1,                       # Min number of instances
)

# ___ stop ec2 instance___
aws_management_console = boto3.session.Session(profile_name="default", region_name="us-east-1")
ec2_console = aws_management_console.client(service_name="ec2")

# response = ec2_console.start_instances(InstanceIds=['i-00a69bcb512028f7d']) # start instance
# response = ec2_console.start_instances(InstanceIds=['i-00a69bcb512028f7d']) # stop instance
response = ec2_console.terminate_instances(InstanceIds=['i-00a69bcb512028f7d'])     # terminate instance

