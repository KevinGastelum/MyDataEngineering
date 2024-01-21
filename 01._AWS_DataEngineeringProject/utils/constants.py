import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST=parser.get('database', 'database_host')
DATABASE_NAME=parser.get('database', 'database_name')
DATABASE_PORT=parser.get('database', 'database_port')
DATABASE_USER=parser.get('database', 'database_user')
DATABASE_PASSWORD=parser.get('database', 'database_password')

INPUT_PATH=parser.get('file_paths', 'input_path')
OUTPUT_PATH=parser.get('file_paths', 'output_path')

POST_FIELDS = (
  'id',
  'title',
  'selftext',
  'score',
  'num_comments',
  'author',
  'created_utc',
  'url',
  'upvote_ratio',
  'over_18',
  'edited',
  'spoiler',
  'stickied',
)

# Verify our ENV variables are commmunicatuing with constants.py
# print(DATABASE_USER)