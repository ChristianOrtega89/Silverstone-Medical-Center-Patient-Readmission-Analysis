# ETL Pipeline for Silverstone Medical Center

This repository contains the **ETL pipeline** for extracting, transforming, and loading (ETL) hospital patient data for Silverstone Medical Center. The pipeline extracts data from CSV files on a local folder, processes it, and loads it into a PostgreSQL database for analysis.

## Overview

The ETL pipeline is implemented in Python and uses **pandas**, **SQLAlchemy**, and **PostgreSQL** for data extraction, transformation, and loading. The data processed includes patient admissions, readmissions, patients, and hospital capacity metrics.

### Components of the Pipeline:

1. **Extract**: Extracts data from CSV files stored in the `data/` folder.
2. **Transform**: Cleans and processes the data, handling missing values, correcting invalid data, and preparing the data for loading.
3. **Load**: Loads the transformed data into a PostgreSQL database, creating necessary tables.
4. **Drop Tables**: Drops all existing tables in the PostgreSQL database before the new data is loaded to avoid conflicts.
5. **Pipeline**: Calls all functions defined in the above files and executes them in order.
6. **run_pipeline** Runs the pipeline

### File Structure

The pipeline is made up of several Python files located in the `/python_files` folder:


## Detailed Explanation of Each Component

### Extract

The [**extract.py**](python_files/extract.py) script loads data from the following CSV files in the `data/` folder:
- `patients.csv`
- `modified_admissions.csv`
- `modified_readmissions.csv`
- `modified_hospital_capacity.csv`

This data is returned as pandas DataFrames and passed on to the next stage.

### Transform

The [**transform.py**](python_files/transform.py) script cleans and prepares the data:
- It handles missing values by filling them with default values.
- It corrects invalid data types and ensures proper formatting.
- It removes duplicate rows from the datasets.
- It also handles specific data cleaning tasks, like correcting negative values in hospital capacity.

### Load

The [**load.py**](python_files/load.py) script creates the necessary tables in the PostgreSQL database and loads the transformed data into the appropriate tables. It uses SQLAlchemy to connect to the PostgreSQL database and pandas to load the DataFrames into the database.

### Drop Tables

The [**drop_tables.py**](python_files/drop_tables.py) script drops all tables in the PostgreSQL database to ensure that new data can be loaded without conflicts. It runs a `DROP TABLE` SQL command for each table in the database.

### ETL Pipeline

The [**pipeline.py**](python_files/pipeline.py) file the entire ETL process by calling the `extract()`, `transform()`, and `load()` functions. It also uses the `drop_all_tables()` function to clear the database before starting the process.
