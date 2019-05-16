import boto3
from botocore.exceptions import ClientError
import logging


BUCKET_PREFIX = "imagerecognyupraveen"
def check_if_bucket_exists(bucket_name):
	s3 = boto3.resource('s3')
	return s3.Bucket(BUCKET_PREFIX+bucket_name) in s3.buckets.all()

def create_bucket(bucket_name):
	if check_if_bucket_exists(bucket_name) == False:
		s3 = boto3.resource('s3')
		sts = boto3.client("sts")
		# userId = sts.get_caller_identity()['Account']
		# print userId
		# s3.create_bucket(Bucket=BUCKET_PREFIX+bucket_name, GrantFullControl="id="+userId)
		s3.create_bucket(Bucket=BUCKET_PREFIX+bucket_name)


def upload_file(file_name, bucket, object_name=None, create_bucket=False):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    s3_client = boto3.client('s3')
    bucket_exists = check_if_bucket_exists(bucket)
    if not bucket_exists:
    	if not create_bucket:
    		logging.error("Bucket does not exist")
    		return False
    	else:
    		create_bucket(bucket)



    if object_name is None:
        object_name = file_name

    # Upload the file
    # try:
    with open(file_name, "rb") as f:
		s3_client.upload_fileobj(f, BUCKET_PREFIX+bucket, object_name)
    # except ClientError as e:
    #     logging.error(e)
    #     return False
    # return True


