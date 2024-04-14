# Azure End to End Data Engineering Projects

| Project Number                         | Project Name                                                                                                                                   |                                                                   Description                                                                   |                                                                       Services & Tools |
| :------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------: |
| [01](#project-01---wikipedia-analysis) | [Wikipedia Analysis](https://github.com/KevinGastelum/MyDataEngineering/tree/main/02._Azure_DataEngineeringProjects/01_Wikipedia_ETL_Pipeline) | Extract, transform, load Wikipedia info into Azure Workflow to analyze number of Football stadiums ranking and locations there are in the world | Docker, SQL, Airflow, Azure DataFactory, Azure DataLake, Azure Synapse, and DataBricks |
| 02                                     | Blank Example                                                                                                                                  |                                                                    centered                                                                     |                                                                                    $12 |
| 03                                     | Blank Example 2                                                                                                                                |                                                                  right-aligned                                                                  |                                                                                     $1 |

## [Project 01](https://github.com/KevinGastelum/MyDataEngineering/tree/main/02._Azure_DataEngineeringProjects/01_Wikipedia_ETL_Pipeline) - Wikipedia Analysis

Created and deployed an end to end workflow pipeline to perform data extraction, cleaning, and visualization of analysis. Also created a docker image to containerize the entire workflow (server, database, python code) and deploy locally or on the cloud. Since I'll be using Azure I'll store my data in Azure Data Lake, and process

<img src="01_Wikipedia_ETL_Pipeline\data\wiki_table.png">

## Technologies Used

- **Data Extraction**: Wikipedia Website
- **Workflow Automation**: Apache Airflow
- **Database Management**: PostgreSQL
- **Cloud Storage**: Azure Blob
- **Data Transformation**: Azure Data Factory
- **Query Service**: Azure Synapse
- **Data Warehousing**: Azure Databricks
- **Data Visualization**: Power BI
