from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.wikipedia_pipeline import extract_wikipedia_data, transform_wikipedia_data


dag = DAG(
  dag_id = 'wikipedia_flow',
  default_args={
    'owner': 'Kevin Gastelum',
    'start_date': datetime(2024, 4, 6),
  },
  schedule_interval = None,
  catchup = False
)

# Extraction 
extract_data_from_wikipedia = PythonOperator(
  task_id = 'extract_data_from_wikipedia',
  python_callable = extract_wikipedia_data,
  provide_context = True,
  op_kwargs = { 'url': 'https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity' },
  dag=dag,
)
# print(get_wikipedia_page('https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity'))

transform_wikipedia_data = PythonOperator(
  task_id='transform_wikipedia_data',
  provide_context=True,
  python_callable=transform_wikipedia_data,
  dag=dag
)

# Write
