from airflow import DAG
from datetime import datetime

from airflow.operators.python import PythonOperator

dag = DAG(
  dag_id = 'wikipedia_flow',
  default_args={
    'owner': 'Kevin Gastelum',
    'start_date': datetime(2024, 04, 06),
  },
  schedule_interval = None
  catchup = False
)

# Extraction 
extract_data_from_wikipedia = PythonOperator(
  task_id = 'extract_data_from_wikipedia',
  python_callable = get_wikipedia_page,
  provide_context = True,

)

# Preprocessing

# Write