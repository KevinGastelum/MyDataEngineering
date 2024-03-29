# AWS End to End Data Engineering Project

The purpose of this pipeline is to automize fetching/scraping data from Reddit post, we will be using the Reddit API, Apache Airflow to trigger tasks that run once a day, Docker to run everything in a containerized local environment, and SQL Postgres database to store the fetched data. After setting everything up locally we want this pipeline running on Cloud infrastructure which provides additional security, storage and processing capacity. I'll set up the pipeline using AWS to fully automate fetching, cleaning, and storing live data using AWS S3, AWS Lambda,AWS Glue, AWS Athena, and AWS Redshift.

### Steps to reproduce this Data Pipeline

- [Step 1](https://github.com/KevinGastelum/MyDataEngineering/tree/main/01._AWS_DataEngineeringProject#step-1---download-project-files-to-your-local-directory-using-git) - Download projects files
- [Step 2](https://github.com/KevinGastelum/MyDataEngineering/tree/main/01._AWS_DataEngineeringProject#step-2---setting-up-environment-variables-credentials-and-api-keys) - Set up your environment variables, credentials and API keys
- [Step 3](https://github.com/KevinGastelum/MyDataEngineering/tree/main/01._AWS_DataEngineeringProject#step-3---set-up-docker-to-run-apache-airflow-celery-redis-and-postgres-database) - Set up Docker to run Apache Airflow, Celery, and Postgres Database
- [Step 4](https://github.com/KevinGastelum/MyDataEngineering/tree/main/01._AWS_DataEngineeringProject#step-4---set-up-aws-ec2-s3-lambda-glue-athena) - Backup Pipeline in the cloud with AWS (EC2, S3, Lambda, Glue, Athena)
- [Step 5](#redshift-for-a-robust-data-warehousing) - Fully automate the Pipeline with live data
<!-- Ensure everything is running correctly -->

## Step 1 - Download project files to your local directory using Git

Clone the directory to your local drive using Git but to not checkout any files yet using --no-checkout

```bash
git clone --no-checkout https://github.com/KevinGastelum/MyDataEngineering.git
# Change directory to MyDataEngineering
cd MyDataEngineering
```

Check out the AWS DataEngineering project files with the following commands

```bash
git sparse-checkout init --cone
git sparse-checkout set 01._AWS_DataEngineeringProject
git checkout main
```

I will be including other Data Engineering pipelines ([Azure](https://azure.microsoft.com/en-us), [GCP](https://cloud.google.com/docs/overview), [Snowflake](https://www.snowflake.com/en/)) inside my MyDataEngineering repo so make sure to only clone the files for the Pipeline you need, in this project we will set up an [AWS](https://aws.amazon.com/) pipeline.

## Step 2 - Setting up Environment variables, credentials, and API keys

There are some files I didnt include for privacy reasons so you'll need to create these files and directories which will contain your environment variables, credentials, and APIs.

It's considered best practice to create new virtual environment when starting a new project.
<br>If you use Anaconda:

```bash
conda create --name redditDE python=3.9
conda activate redditDE
```

Or in Python:

```bash
python -m venv redditDE
# Activating on Windows
.\redditDE\Scripts\activate
#Activating on Linux/Mac
source redditDE/bin/activate
```

Next in your terminal create the directories data, plugins, tests, and logs:

```bash
# Create directories - data, plugins, tests, logs
mkdir data plugins tests logs
# Inside the data directory create an input and output directort
mkdir data/input data/output
```

<img src="images\Step1-redditDE.png">

```bash
# You can rename the config.conf.example file inside the config directory to config.conf.
mv config/config.conf.example config/config.conf
# Just fill in the brackets with your credentials (EXAMPLE ABOVE)
```

```python
# Run requirements.txt to install all dependencies
pip install -r requirements.txt

```

## Step 3 - Set up Docker to run Apache Airflow, Celery, Redis, and Postgres Database

Install [Docker](https://docs.docker.com/get-docker/) if you don't already have it and launch. Then run the following command in your terminal.

```bash
# This builds our docker containers with Airflow, Celery, Redis and Postgres
docker compose up -d --build
```

You can access your Airflow DAG using localhost:8080 with your login creds.

<img src="images\airflow--vscode.png">

## Step 4 - Set up AWS (EC2, S3, Lambda, Glue, Athena)

Create an EC2 instance with access to your S3 bucket - https://repost.aws/knowledge-center/ec2-instance-access-s3-bucket

Trigger the Airflow DAG to pull data from the Reddit API and make sure your Reddit data is being stored in your S3 bucket (see example below)

### AWS EC2 instance and S3 storage bucket

<img src="images\EC2--S3.png">

### AWS Glue Setup

Set AWS Glue to automatically discover when S3 bucket has new data and keep the catalog up to date.

<img src="images\AWS_glue.png">

AWS Glue script to Fetch and clean data from S3 bucket:

```python
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import concat_ws
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1709844025958 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://redditengineering-s3/raw/reddit_20240307.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1709844025958")

# Convert DynamicFrame to DataFrame
df = AmazonS3_node1709844025958.toDF()

# Concat the 3 columns into a single column
df_combined = df.withColumn('ESS_updated', concat_ws('-', df['edited'], df['spoiler'], df['stickied']))
df_combined = df_combined.drop('edited', 'spoiler', 'stickied')

#Convert back to DynamicFrame
S3bucket_node_combined = DynamicFrame.fromDF(df_combined, glueContext, 'S3bucket_node_combined')

# Script generated for node Amazon S3
AmazonS3_node1709844036570 = glueContext.write_dynamic_frame.from_options(frame=S3bucket_node_combined, connection_type="s3", format="csv", connection_options={"path": "s3://redditengineering-s3/transformed/", "partitionKeys": []}, transformation_ctx="AmazonS3_node1709844036570")

job.commit()
```

### Using AWS Athena to Query data

With the help of AWS Glue our data becomes easier to work with, AWS Athena allows us to Query the data for DataWarehousing
<img src="images\aws_athena.png">

### Redshift for robust Data Warehouse

<img src="images\aws_redshift2.png">

<!-- - Set up AWS (EC2, S3, Lambda, Glue, Athena)
  Set up Ec2 instance and s3 bucket for -->

<!-- End to End AWS project to extract, transform, and load (ETL) real-time data from Reddit posts into a Redshift data warehouse. This pipeline integrates multiple technologies to ensure efficient data handling and storage.

<img src="images\RedditDataEngineering-.png">

## Technologies Used

- **Data Extraction**: Reddit API
- **Workflow Automation**: Apache Airflow, Celery
- **Database Management**: PostgreSQL
- **Cloud Storage**: Amazon S3
- **Data Transformation**: AWS Glue, Lambda
- **Query Service**: Amazon Athena
- **Data Warehousing**: Amazon Redshift
- **Data Visualization**:

## Data Pipeline

- **Automated Data Processing Workflow**: Utilizing Apache Airflow and Celery for data processing.
- **Data Storage**: PostgreSQL and Amazon S3 for data storage.
- **Data Transformation**: Integrates AWS Glue, Lambda and Amazon Athena for effective data transformation and querying.
- **Scalable Data Warehousing**: Utilizes Amazon Redshift for a high-performance data warehousing solution.

## Objective

Showcases my ability to integrate various technologies to create a robust and scalable data pipeline. Demonstrate my expertise in handling big data and my capabilities to deliver efficient and reliable data solutions. -->

<!-- =============================== -->

<!--

Take screensshots of Docker/Airflow, AWS EC2/S3, SQL/Celery, Glue/Lambda, Athena/Redshift, Visuals

-->

<!--
Docker Commands =

docker compose up -d --build
docker compose up -d

docker exec -it


--Fresh Start steps
Set up VENV - Conda
run reqs.txt to install all required packages
pull in config.conf settings , data, logs, plugins, tests
run docker build

-->
