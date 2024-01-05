from airflow import DAG
from datetime import datetime
import os
import sys

sys.path.insert(__index:0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
  'owner': 'Kevin Gastelum',
  'start_date': datetime(year: 2024, month: 1, day: 2)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
  dag_id='etl_reddit_pipeline',
  default_args=default_args,
  schedule_interval='@daily',
  catchup=False,
  tag=['reddit', 'etl', 'pipeline']
)

# Extracting data from Reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
      'file_name': f'reddit_{file_postfix}',
      'subreddit': 'dataengineering',
      'time_filter': 'day',
      'limit': 100
    }
)