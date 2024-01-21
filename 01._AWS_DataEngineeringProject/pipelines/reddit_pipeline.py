import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
  # Connect to reddit API
  instance = connect_reddit(CLIENT_ID, SECRET, 'kevapp') # Enter reddit user-agent or app name
  # Extract
  posts = extract_posts(instance, subreddit, time_filter, limit)
  post_df = pd.DataFrame(posts)
  # Transform
  post_df = transform_data(post_df)
  # Load
  file_path = f'{OUTPUT_PATH}/{file_name}.csv'
  load_data_to_csv(post_df, file_path)

  return file_path

# print(CLIENT_ID)
