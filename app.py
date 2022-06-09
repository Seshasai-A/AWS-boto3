from asyncore import read
from distutils.command.config import config
from email.policy import Policy
import logging
from urllib import response
from botocore.exceptions import ClientError
import boto3
import json
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY =''

s3_client = boto3.client('s3',region_name='ap-south-1', 
                        aws_access_key_id=AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

location= {'LocationConstraint':'ap-south-1'}
# s3_client.create_bucket(Bucket ='sesha-cousera',
#                         CreateBucketConfiguration =location)
"""
Getting buckets from aws user using list_buckets
"""                    
# response = s3_client.list_buckets()

# for bucket in response['Buckets']:
#     print(bucket['Name'])

"""
Uploading file to s3
"""

# file_name= 'img\ironman.png'
# bucket_name= 'cousera'
# object_name= file_name

# response = s3_client.upload_file(file_name,bucket_name,object_name)

# with open(file_name, 'rb') as f:
#     s3_client.upload_fileobj(f,bucket_name,'ironmanstark')

"""
Download files from s3
"""

# file_name= 'img\ironman.png'
# bucket_name= ''
# object_name= 'ironman_public.png'

# response = s3_client.upload_file(file_name,bucket_name,object_name,
# ExtraArgs={'ACL':'public-read'})
# s3_client.download_file(bucket_name,'ironman_public.png', 'ironman_public_s3.png')

"""
2nd way to download
"""
# with open('ironman_image_write.png','wb') as f:
#     s3_client.download_fileobj(bucket_name, object_name,f)


"""
Mutlipart transefer and File transfer config
"""



# from boto3.s3.transfer import TransferConfig

# GB = 1024**3
# #0.5*GB =500Mb
# #5*GB = 5GB
# config = TransferConfig(multipart_threshold=0.5*GB)
# s3_client.upload_file(file_name,bucket_name, 'ironman_multi_transfer.png', config=config)


"""
presigned urls

A user who doesn't have aws credentials/ permission to access an s3 objcet can be granted 

temporary access by using presigned urls

aws user can generate presigned url who has access to object 

view in browser or web html 

presigned url is valid for limited time when specified url is generated

"""

# response_pre_sign= s3_client.generate_presigned_url('get_object',
# Params={'Bucket':bucket_name,
#         'Key':'ironmanstark'},
# ExpiresIn=3600)

# print(response_pre_sign)


"""
Bucket policies config :

S3 bucket can have an optional access that grant access permission to other aws account
or aws identity and access managemnt user, Bucket policies and define using the same json formate 
as a resource-based IAM policy
"""

# result = s3_client.get_bucket_policy(Bucket='cousera')
# print(result['Policy'])




"""
put policy

"""
# bucket_name = 'cousera'

# bucket_policy = {
#     'Version': '2012-10-17',
#     'Statement':[{
#         'Sid':'AddPerm',
#         'Effect':'Allow',
#         'Principal':'*',
#         'Action':['s3:GetObject'],
#         'Resource':f'arn:aws:s3:::{bucket_name}/*'
#     }]

# }

# bucket_policy = json.dumps(bucket_policy)
# print(bucket_policy)
# s3_client.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)

"""
Delete policy
"""

# s3_client.delect_bucket_policy(Bucket='xyz')


"""
CORS = CRoss origin resource sharing enable client web app in one domain access resource in another domain

an s3 bucket can be config to enable cors 
the config defines rules the specify the allowed origin,
 httop(get, put etc)
"""

"""
retrieve cors
"""

respone =s3_client.get_bucket_cors(Bucket='xyz')
print(respone['CORSRules'])

"""
set cors
"""
# bucket_name='sesha-cousera'
# cors_configuration ={
#     'CORSRules': [
#         {
#             'AllowedHeaders':['Authorization'],
#             'AllowedMethods':['GET','PUT'],
#             'AllowedOrigins':["*"],
#             'ExposeHeaders':['GET','PUT'],
#             'MaxAgeSeconds':3000
#         }
#     ]
# }
# s3_client.put_bucket_cors(Bucket=bucket_name,CORSConfiguration=cors_configuration)