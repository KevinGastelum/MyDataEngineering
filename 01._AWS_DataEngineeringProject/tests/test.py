import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import praw
from utils.constants import CLIENT_ID, SECRET


def test_reddit_connection(client_id, client_secret, user_agent):
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             user_agent=user_agent)
        
        # Test the connection by fetching the top post from a subreddit
        top_post = next(reddit.subreddit("test").top(limit=1))
        print("Successfully connected to Reddit!")
        print(f"Top post title: {top_post.title}")
    
    except Exception as e:
        print("Failed to connect to Reddit:")
        print(e)

# Replace these with your actual Reddit API credentials
USER_AGENT = 'kevapp'

test_reddit_connection(CLIENT_ID, SECRET, USER_AGENT)
print(f"CLIENT_ID: {CLIENT_ID}, Type: {type(CLIENT_ID)}")
print(f"SECRET: {SECRET}, Type: {type(SECRET)}")
