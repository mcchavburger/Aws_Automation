'''
These scripts have been written in order to test and further my python and boto3 understanding, they are not intend (at this point) to be used in any production environment
However please feel free to use these scripts any way you wish, dont blame me if stuff breaks :-)

'''

#import boto3
import os
import platform
import sys

osVersion = platform.system()

if osVersion.lower() == "windows":
    seperator = "\\"
else:
    seperator = "/"

file_path = os.path.realpath(__file__).split(seperator)
file_path = file_path[:len(file_path)-2]
file_path = seperator.join(file_path)
sys.path.insert(1, file_path)

from regions.get_regions import get_regions

return_regions = get_regions("ec2")
for i in return_regions:
    print(i)

'''
s = boto3.Session(region_name="us-east-1")
ec2 = s.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-00ca32bbc84273381',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
)
print(instance[0].id)
'''