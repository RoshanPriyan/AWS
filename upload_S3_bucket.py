import boto3

aws_con = boto3.session.Session(profile_name='default')
s3 = aws_con.client('s3')
s3.upload_file("C:\\Users\\ROSHANHARIHARAPRIYAN\\OneDrive\\Desktop\\s3_service.py", 'botoroshanbucket', 'awscode.py')
