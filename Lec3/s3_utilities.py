import boto3

def get_connection(service):
    return boto3.client(service)


def get_bucket_list(s3_client):
    response = s3_client.list_buckets()
    for key, values in response.items():
    #print(key, ":-", values)
       if key == 'Buckets':
           print("can fetch bucket list successfully")
       else:
           pass   
# better get_bucket_list code 
"""
def get_bucket_list(s3):
    response = s3.list_buckets()

    for bucket in response["Buckets"]:
        print(bucket["Name"])
"""

def create_bucket(s3_client, bucket_name):

    try : 
        response = s3_client.create_bucket(Bucket=bucket_name,
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

s3_client = get_connection('s3') #creating a connection to s3 service
bucket_list = get_bucket_list(s3_client)


create_bucket(s3_client, "rehman-therja")



#ec2 = get_connection('ec2')    