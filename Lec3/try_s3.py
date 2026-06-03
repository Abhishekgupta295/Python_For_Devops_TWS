from s3_utilities import aws_utilities

print("Inside Try S3 file")
aws = aws_utilities()
aws.get_bucket_list(aws.s3_client)
# or aws_utilities().get_bucket_list(aws.s3_client)

#aws.create_bucket(aws.s3_client, "rehman-therja")
#aws.upload_file_to_bucket(aws.s3_client,"json_output.json", "rehman-therja", "uploaded_json_output.json")

## SDK --> Software Development Kit , CDK --> Cloud Development Kit
## pycache file is created when we use packages by importing it, we generally not push it to git.