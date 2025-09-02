'''
These scripts have been written in order to test and further my python and boto3 understanding, they are not intend (at this point) to be used in any production environment
However please feel free to use these scripts any way you wish, dont blame me if stuff breaks :-)

*** usage ***

script can be interactively and user will be asked for values\variables as the script runs, all efforts have been made to ensure no typos can prevent the provisioning of an ec2 instance by validating user provided variables against lists obtained from AWS.

A live lists of regions is returned by using the module "get_regions", the user provided region will be checked against this list

script can also be run by providing variables as input

.\create_ec2_instance.py --user_region "eu-west-02"

'''

#import boto3
import os
import platform
import sys
import argparse

parser = argparse.ArgumentParser(description="Define Variables..")
parser.add_argument("--user_region", nargs='?', type=str, help="The Region You want to create the EC2 Instance in")
parser.add_argument("--image-id", nargs='?', type=str, help="The Image ID you want to use to create the EC2 Instance")
parser.add_argument("--instance-type", nargs='?', type=str, help="The EC2 Instance Type")
args = parser.parse_args()

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

availble_regions = get_regions("ec2")
print("User supplied region:", args.user_region)

if {args.user_region} != {None}:
    user_region = {args.user_region}
else:
    user_region = input('Please Enter Which Region You Would Like to Create a EC2 Instance in?\n')

while True:
    if user_region.lower() in availble_regions:
        break
    else:
        print('The provided region is not valid, please enter a valid region from the list below...')
        for i in availble_regions:
            print(i)
        user_region = input('Please Enter Which Region You Would Like to Create a EC2 Instance in?\n')
        continue

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