import praw
from praw import Reddit
import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.constants import POST_FIELDS

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                            client_secret=client_secret,
                            user_agent=user_agent)
        print("connected to reddit!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)


def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter:str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=time_filter, limit=limit)

    post_lists = []

    for post in posts:
        post_dict = vars(post)
        print(post_dict)
        post = {key: post_dict[key] for key in POST_FIELDS}
        post_lists.append(post)

    return post_lists


def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    return post_df


def load_data_to_csv(data: pd.DataFrame, path: str):
    data.to_csv(path, index=False)