import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.constants import AWS_BUCKET_NAME
from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3

def upload_s3_pipeline(ti):
  file_name = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')

  s3 = connect_to_s3()
  create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)
  upload_to_s3(s3, file_path, AWS_BUCKET_NAME, file_path.split('/')[-1])

# test if S3 bucket is connected
# print(AWS_BUCKET_NAME)