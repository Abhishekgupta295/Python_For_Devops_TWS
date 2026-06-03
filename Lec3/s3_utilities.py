import boto3

class aws_utilities:

    def __init__(self):
       self.s3_client =  self.get_connection('s3') #creating a connection to s3 service

    def get_connection( self ,service):
        return boto3.client(service)


    def get_bucket_list(self, s3_client):
        response = self.s3_client.list_buckets()
        for bucket in response["Buckets"]:
             print(bucket["Name"])  
            

    def create_bucket(self,s3_client, bucket_name):

        try : 
            response = self.s3_client.create_bucket(Bucket=bucket_name,
                                            CreateBucketConfiguration={
                'LocationConstraint': 'eu-west-1',
            },)
            print(response)
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                print("Bucket created successfully")
            else:
                print("Bucket creation failed")    

        except :
            print("Bucket creation failed")       


    def upload_file_to_bucket(self,s3_client,file_path, bucket_name, file_name):
        try:
            self.s3_client.upload_file(file_path , bucket_name, file_name)
            print("File Upload Successfully")
        except :
            print("File upload failed")

print("start")
if __name__ == "__main__":  # this main block will execute only when this file is run directly, it will not execute when 
    #this file is imported as a module in another file.
    # if we dont use it, then even after running other file, this code will execute which is not what we want.
    #  means repeated same output
    print("inside main block")
    aws = aws_utilities()
    bucket_list = aws.get_bucket_list(aws.s3_client)
print("exit")    
   




aws.create_bucket(aws.s3_client, "rehman-therja")
aws.upload_file_to_bucket(aws.s3_client,"json_output.json", "rehman-therja", "uploaded2_json_output.json")



#ec2 = get_connection('ec2')    