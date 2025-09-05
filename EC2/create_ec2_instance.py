'''
These scripts have been written in order to test and further my python and boto3 understanding, they are not intend (at this point) to be used in any production environment
However please feel free to use these scripts any way you wish, dont blame me if stuff breaks :-)

*** usage ***

script can be interactively and user will be asked for values\variables as the script runs, all efforts have been made to ensure no typos can prevent the provisioning of an ec2 instance by validating user provided variables against lists obtained from AWS.

A live lists of regions is returned by using the module "get_regions", the user provided region will be checked against this list

script can also be run by providing variables as input

.\create_ec2_instance.py --user_region "eu-west-02"

'''

import boto3
import os
import platform
import sys
import argparse
from images.image_methods import get_region_images

parser = argparse.ArgumentParser(description="Define Variables..")
parser.add_argument("--user_region", nargs='?', type=str, help="The Region You want to create the EC2 Instance in")
parser.add_argument("--image_id", nargs='?', type=str, help="The Image ID you want to use to create the EC2 Instance")
parser.add_argument("--image_owner", nargs='?', type=str, help="The Image Owner, EG self, amazon, public")
parser.add_argument("--instance_type", nargs='?', type=str, help="The EC2 Instance Type")
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

from regions.region_methods import get_regions

availble_regions = get_regions("ec2")
print("User supplied region:", args.user_region)
print("User supplied image_id:", args.image_id)
print("User supplied image_owner:", args.image_owner)
print("User supplied instance_type:", args.instance_type)

if {args.user_region} != {None}:
    user_region = list({args.user_region})[0]
    if user_region not in availble_regions:
        error = "The region provided is not vaild, please re-run the script with one of the following regions\n"
        error += "User Provided Region: " + str(user_region)
        error += "Availble regions:\n"
        for i in availble_regions:
            error += i + "\n"
        sys.exit(error)
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

if {args.image_owner} != {None}:
    image_owner = {args.image_owner}
else:
    image_owner = "amazon"

availble_images = get_region_images(user_region,image_owner)
image_names = [n['Name'] for n in availble_images] 
image_ids = [id['ImageId'] for id in availble_images] 

if {args.image_id} == {None}:
    print('Please Enter Which EC2 Image You Would Like to use from the following..')
    for i in image_names:
        print(i)
    image_name = input('Please Enter an Image Name to Create the EC2 Instance...\n')
    while True:
        if image_name in image_names:
            break
        else:
            print('The provided image name is not valid, please enter a valid image name from the list below...')
            for i in image_names:
                print(i)
            image_name = input('Please Enter an Image Name to Create the EC2 Instance...\n')
            continue
    image_id = [item for item in availble_images if item["Name"] ==  image_name][0]["ImageId"]
else:
    image_id = list({args.image_id})[0]
    if image_id not in image_ids:
        error = "The Image Id provided is not vaild, or not valid for the given region please re-run the script with one of the following Image Ids\n"
        error += "User Provided image_id:" + str(image_id)
        error += "Availble imageids:\n"
        for i in image_ids:
            error += i + "\n"
        sys.exit(error)

s = boto3.Session(region_name=user_region)
ec2 = s.resource('ec2')

instance = ec2.create_instances(
    ImageId=image_id,
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
)
print(instance[0].id)
