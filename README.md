# Overview
- Basic Python/Boto3 scripts for automating common AWS tasks (EC2 provisioning, S3 listing, and region lookups).
- Written as learning exercises to explore Python, APIs, and Boto3.

## Repository structure
- **EC2/**: Scripts and helpers for creating EC2 instances and inspecting images or instance types.
- **S3/**: A minimal helper that lists all buckets in the configured account/region.
- **regions/**: Shared helper for enumerating service regions, reused by other scripts.

## Key modules
- `EC2/create_ec2_instance.py`: Argparse-based CLI that discovers valid regions, fetches AMI metadata, and provisions a `t3.micro` instance.
- `EC2/images/image_methods.py`: Wraps `describe_images` to return AMIs for a given owner in a region.
- `EC2/instances/instance_methods.py`: Demonstrates `describe_instance_types` with optional free-tier filtering.
- `regions/region_methods.py`: Returns available regions for a given service via `boto3.Session.get_available_regions`.
- `S3/get_s3_buckets.py`: Lists bucket names using the active AWS credentials and region.

## Getting started
1. Ensure Python **3.9+** (developed on Python 3.13.7) and install dependencies:
   - `pip install boto3`
   - `pip install boto3[crt]`
   - Boto3 quickstart: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation
2. Configure AWS credentials (Linux: `~/.aws/credentials`, Windows: `C:\\Users\\%user%\\.aws\\credentials`):
   - `[default]`
   - `aws_access_key_id = YOUR_ACCESS_KEY`
   - `aws_secret_access_key = YOUR_SECRET_KEY`
3. Configure AWS region (Linux: `~/.aws/config`, Windows: `C:\\Users\\%user%\\.aws\\config`):
   - `[default]`
   - `region = us-east-1`
4. Run examples:
   - List buckets: `python S3/get_s3_buckets.py`
   - Create an EC2 instance: `python EC2/create_ec2_instance.py --user_region "<region>" --image_owner "amazon" --image_id "<ami>"` (or run without args to be prompted).

Configuration file info: https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html

## Learning pointers
- Strengthen argument validation and add unit tests around input handling (the EC2 script mixes prompts and CLI args).
- Expand filtering/pagination for instance type and AMI lookups (architecture, cost, performance, NextToken handling).
- Introduce structured logging and error handling instead of printing/exit flows.
- Experiment with additional AWS services (VPC setup, security groups, IAM roles) and infrastructure-as-code patterns.
- Consider packaging the helpers as a small CLI with dependency pinning for easier reuse.
