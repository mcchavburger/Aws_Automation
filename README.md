Overview
- This Repo contains basic scripts to automate the provisioning of AWS resources using Boto3 and Python. They have been written to further my own understanding of python, apis and boto3
- Scripts have been developed using the following versions
- Python Version 3.13.7, boto 3 requires Python 3.9 of newer.
- Python venv was configured with the following configured/installed
- pip install boto3
- pip install boto3[crt]
- credentials file configured as below (Linux location, ~/.aws/credentials. Windows Location C:\Users\%user%\.aws\credentials)

  - [default]
  - aws_access_key_id = YOUR_ACCESS_KEY
  - aws_secret_access_key = YOUR_SECRET_KEY

  - https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html
  
  - configuration file configured as below (Linux location, ~/.aws/config. Windows Location C:\Users\%user%\.aws\config)
 
  - [default]
  - region=us-east-1
