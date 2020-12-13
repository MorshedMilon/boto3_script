import boto3

aws_mag_con=boto3.session.Session(profile_name='root')
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
   print(each_user.name)

###########################################################
import boto3

aws_mag_con_root=boto3.session.Session(profile_name='root')
#aws_mag_con_root=boto3.session.Session(profile_name='Ec2-dev')
iam_con_re=aws_mag_con_root.resource(service_name='iam' ,region_name="us-east-2")

for each_user in iam_con_re.users.all():
       print(each_user.name)

##############################################################

import boto3

aws_mag_con_root=boto3.session.Session(profile_name='root')
iam_con_client=aws_mag_con_root.client(service_name='iam',region_name="us-east-2")

for each  in iam_con_client.list_users()['Users']:
       print(each['UserName'])
       