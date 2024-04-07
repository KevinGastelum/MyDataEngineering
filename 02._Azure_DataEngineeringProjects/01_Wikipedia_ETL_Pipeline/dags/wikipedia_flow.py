from airflow import DAG
from datetime import datetime

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


# Preprocessing

# Write