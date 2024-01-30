# [AWS End to End Data Engineering Project](https://github.com/KevinGastelum/MyDataEngineering/tree/main/01._AWS_DataEngineeringProject)

## Reddit real-time Data Extraction --> Data Warehousing --> Data Modeling --> Data Pipeline

End to End AWS project to extract, transform, and load (ETL) real-time data from Reddit posts into a Redshift data warehouse. This pipeline integrates multiple technologies to ensure efficient data handling and storage.

<img src="01._AWS_DataEngineeringProject\images\RedditDataEngineering-.png">

## Technologies Used

- **Data Extraction**: Reddit API
- **Workflow Automation**: Apache Airflow, Celery
- **Database Management**: PostgreSQL
- **Cloud Storage**: Amazon S3
- **Data Transformation**: AWS Glue, Lambda
- **Query Service**: Amazon Athena
- **Data Warehousing**: Amazon Redshift
- **Data Visualization**:

<!-- ## Data Pipeline

- **Automated Data Processing Workflow**: Utilizing Apache Airflow and Celery for data processing.
- **Data Storage**: PostgreSQL and Amazon S3 for data storage.
- **Data Transformation**: Integrates AWS Glue, Lambda and Amazon Athena for effective data transformation and querying.
- **Scalable Data Warehousing**: Utilizes Amazon Redshift for a high-performance data warehousing solution. -->

## Objective

Showcases my ability to integrate various technologies to create a robust and scalable data pipeline. Demonstrate my expertise in handling big data and my capabilities to deliver efficient and reliable data solutions.

## [Walkthrough HERE](https://github.com/KevinGastelum/MyDataEngineering/tree/main/01._AWS_DataEngineeringProject#aws-end-to-end-data-engineering-project)

<!--

KEVIN'S PERSONAL NOTES/INSTRUCTIONS

Take screensshots of Docker/VSCode, AWS EC2/S3, Airflow/Celery, Glue/Lambda, Athena/Redshift, Visuals

Docker/ VSCODE Screenshot -- Connecting to Airflow locally through Docker container
EC2 CLI && S3 Bucket with reddit file screenshot -- Setting up AWS EC2 instance and S3 bucket for automated Data storage
Airflow / Celery screenshot -- Connecting to AWS from Airflow


-- DOCKER Commands used
- Shows all containers
docker ps
docker-compose ps

- Build/Start or update your containers
docker compose up -d --build
docker compose up -d
docker exec -it {container hash}
docker stop $(docker ps -a -q)
docker compose down

- REMOVE all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune
docker system prune -a --volumes


-- FRESH Start steps
- Set up VENV through Conda
conda create --name redditDE python=3.9
conda activate redditDE // netflixDE

- Run reqs.txt to install all required packages
pip install -r requirements.txt

- Pull/Create config.conf settings , data/input, data/output, logs, plugins, tests
mkdir data logs plugins tests

compose up -d --build

run airflow on localhost:8080

Obtain Reddit API Keys and insert into your config file


-- AWS SETUP

- Go to AWS -> Create user -> Group -> EC2 instance -> S3 bucket
Begin @ min 9 to watch video walkthrough
https://www.youtube.com/watch?v=j_skupZ3zw0&t=3s

- Login to AWS with your new user (make sure user has admin privileges)
https://{YOUR ACNT ID}.signin.aws.amazon.com/console
- Create EC2 instance and launch

- Inside EC2 console
sudo apt-get update
sudo apt install python3-pip
sudo apt install python3.10-venv
- might need to restart terminal
python3 -m venv netflixDE
- Start Venv
source netflixDE/bin/activate

- Install AWS CLi
pip install --upgrade awscli
sudo pip install apache-airflow
airflow standalone -- to launch

-- OBTAIN SESSION TOKEN
- Run the following command inside your AWS EC2 instance to generate your AWS Session token. --duration-seconds can be any number
configure aws
aws sts get-session-token --duration-seconds 3600


-- SSH into AWS EC2 through VSCODE
- Download then locate .pem file directory ie Downloads
ssh -i "redditdataengineering-pair.pem" ubuntu@ec2{YOUR INSTANCE}



### FUTURE PROJECT NOTES:
Build 3 different End to End projects (AWS, Azure, GCP)

AWS:
Reddit Real time - (Docker, PSQL, Airflow), (EC2, S3, Lambda, Glue, Athena, Redshift)
https://www.youtube.com/watch?v=LSlt6iVI_9Y

Zillow End to End (AWS, Quicksight)
https://www.youtube.com/watch?v=j_skupZ3zw0&t=3s


Azure:
Power BI
https://www.youtube.com/watch?v=iQ41WqhHglk


GCP:
Uber Data Analytics
https://www.youtube.com/watch?v=WpQECq5Hx9g


Snowflake:
https://www.youtube.com/watch?v=qDmqE89DSQQ



FCC (Docker, PSQL, Build Pipeline from scratch, dbt, CRON, Airflow, Airbyte):
https://www.youtube.com/watch?v=PHsC_t0j1dU


-->
<!-- -->
<!-- -->
<!-- -->
