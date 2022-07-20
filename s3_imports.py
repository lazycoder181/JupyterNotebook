import boto3
import pandas

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id='#######',
    aws_secret_access_key='#######',
    region_name='ap-southeast-2'
)

# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id='##########',
    aws_secret_access_key='###################',
    region_name='ap-southeast-2'
)

# Fetch the list of existing buckets
clientResponse = client.list_buckets()

# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')

# Creating a bucket in AWS S3
# location = {'LocationConstraint': 'ap-south-1'}
# client.create_bucket(
#     Bucket='sql-server-shack-demo-3',
#     CreateBucketConfiguration=location
# )

# Create the S3 object
obj = client.get_object(
    Bucket='bucket_name',
    Key='file_name/object from s3'
)

# Read data from the S3 object
data = pandas.read_csv(obj['Body'])

# Print the data frame
print('Printing the data frame...')
print(data)