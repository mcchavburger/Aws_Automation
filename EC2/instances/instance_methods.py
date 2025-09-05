import boto3


def get_instance_types(region, instance_arch, freeTierOnly):
    # Initialize a session using Boto3
    ec2_client = boto3.client("ec2", region_name=region)

    # Fetch all AMIs visible to your account
    response = (
        ec2_client.describe_instance_types()
    )  # Replace 'self' with 'amazon' or other owner IDs if needed
    return_types = []
    return_types.extend(response["InstanceTypes"])
    my_filters = []

    filter = {
            "Name": "processor-info.supported-architecture",
            "Values": [
                instance_arch,
            ],
        }

    if freeTierOnly:
        filter = {
            "Name": "free-tier-eligible",
            "Values": [
                True,
            ],
        }
        my_filters.extend(filter)

    while response["NextToken"]:
        response = ec2_client.describe_instance_types(
            Filters=my_filters, NextToken=response["NextToken"]
        )
        return_types.extend(response["InstanceTypes"])
    # Extract and print image details
    return return_types


instance_types = get_instance_types("eu-west-1", "x86_64", True)
print(instance_types)
