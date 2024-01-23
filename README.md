# AWS End to End Data Engineering Project

## Real Time Reddit Data Extraction --> Data Warehousing --> Data Modeling --> Data Pipeline

End to End AWS project to extract, transform, and load (ETL) data from Reddit into a Redshift data warehouse. This pipeline integrates multiple technologies to ensure efficient data handling and storage.

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

Showcases my ability to integrate various technologies to create a robust and scalable data pipeline. It demonstrates my expertise in handling big data and my capabilities to deliver efficient and reliable data solutions.

<!--

Take screensshots of Docker/Airflow, AWS EC2/S3, SQL/Celery, Glue/Lambda, Athena/Redshift, Visuals



### DOCKER

docker ps
docker-compose ps

docker compose up -d --build
docker compose up -d

docker exec -it {container hash}

docker stop $(docker ps -a -q)


-- REMOVE all containers
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune
docker system prune -a --volumes


-- FRESH Start steps
- Set up VENV - Conda
conda create --name redditDE python=3.9
conda activate redditDE // netflixDE

- Run reqs.txt to install all required packages
pip install -r requirements.txt

- Pull in config.conf settings , data, logs, plugins, tests
run docker build



-- Install AWS CLi

Go to AWS -> Create user -> group -> EC2 instance -> S3 bucket

Login to AWS with your new user (give user admin privileges)
Begin @ min 9
https://www.youtube.com/watch?v=j_skupZ3zw0&t=3s




ssh -i "redditdataengineering-pair.pem" ubuntu@ec2{YOUR INSTANCE}

Run the following command inside your AWS EC2 instance to generate your AWS Session token. --duration-seconds can be any number
configure aws
aws sts get-session-token --duration-seconds 3600





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
