import boto3

aws_con = boto3.session.Session(profile_name='ec2_user')
s3 = aws_con.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
