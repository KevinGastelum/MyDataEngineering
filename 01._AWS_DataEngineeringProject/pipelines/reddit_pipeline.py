from etls.reddit_etl import connect_reddit,extract_posts
from utils.constants import CLIENT_ID, SECRET


def reddit_pipeline(subreddit: str, time_filter='day', limit=None):
  # Connect to reddit API
  instance = connect_reddit(CLIENT_ID, SECRET, '0xKay') # Enter reddit USERNAME
  # Extract
  posts = extract_posts(instance, subreddit, time_filter, limit)
  # Transform
  # Load