# AWS End to End Data Engineering Project

### Steps to reproduce this Data Pipeline

- Step 1 - Download projects files
- Step 2 - Set up your environment variables, credentials and API keys
- Step 3 - Set up Docker in order to run Apache Airflow, Celery, and Postgres Database
- Step 4 - Set up AWS (EC2, S3, Lambda, Glue, Athena)
- Step 5 - Ensure everything is running correctly

## Step 1 - Download project files to your local directory using Git

```bash
# Clone the directory to your local drive using Git but to not checkout any files yet using --no-checkout
git clone --no-checkout https://github.com/KevinGastelum/MyDataEngineering.git
# Change directory to MyDataEngineering
cd MyDataEngineering
# Check out the AWS DataEngineering project files with the following commands
git sparse-checkout init --cone
git sparse-checkout set 01._AWS_DataEngineeringProject
git checkout main
```

I will be including other Data Engineering pipelines ([Azure](https://azure.microsoft.com/en-us), [GCP](https://cloud.google.com/docs/overview), [Snowflake](https://www.snowflake.com/en/)) inside my MyDataEngineering repo so make sure to only clone the files for the Pipeline you need, in this project we will set up an [AWS](https://aws.amazon.com/) pipeline.

## Step 2 - Setting up environment variables, credentials and API keys

There are some files I didnt include so you'll need to create these files and directories which will contain your environment variables, credentials, and APIs.

It's considered best practice to create new virtual environment when starting a new project.

```bash
# Run python venv or use Conda for this.
conda create --name redditDE python=3.9
conda activate redditDE
```

```bash
# Create directories - data, plugins, tests, logs
mkdir data plugins tests logs
# Inside the data directory create an input and output directort
mkdir data/input data/output
```

```bash
# You can rename the config.conf.example file inside the config directory to config.conf.
# Just fill in the brackets with your credentials
mv config/config.conf.example config/config.conf
```

<img src="images\Step1-redditDE.png">

```bash
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

Trigger the DAG to pull data from the Reddit API (make sure your Reddit data is being stored in your S3 bucket)

<img src="images\EC2--S3.png">

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
