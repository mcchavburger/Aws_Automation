'''
These scripts have been written in order to test and further my python and boto3 understanding, they are not intend (at this point) to be used in any production environment
However please feel free to use these scripts any way you wish, dont blame me if stuff breaks :-)
'''

import boto3

# Retrieve the list of existing buckets
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')