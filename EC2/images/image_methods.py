import boto3

def get_region_images(region,owner):
    # Initialize a session using Boto3
    ec2_client = boto3.client('ec2',region_name=region)

    # Fetch all AMIs visible to your account
    response = ec2_client.describe_images(Owners=[owner])  # Replace 'self' with 'amazon' or other owner IDs if needed

    # Extract and print image details
    return response['Images']