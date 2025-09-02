
def get_regions(service):
    import boto3
    s = boto3.Session()
    regions = s.get_available_regions(service,partition_name='aws', allow_non_regional=False)
    return regions
