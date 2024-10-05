import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.client(service_name="iam")

user = iam_console.list_users()
for i in user.get("Users"):
    print(i.get("UserName"))
