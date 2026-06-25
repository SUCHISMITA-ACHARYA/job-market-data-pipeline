# Job Market Data Pipeline

## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using Python. It processes raw job posting data from a JSONL file, cleans and transforms the data, stores it in a SQLite database, executes SQL queries, and visualizes key insights using Power BI.

The project demonstrates the complete data engineering workflow from raw data ingestion to analysis and reporting.

---

## Project Workflow

1. Extract raw job posting data from a JSONL file.
2. Clean and preprocess the dataset.
3. Create new analytical features.
4. Extract technical skills from job descriptions.
5. Validate the processed data.
6. Save the cleaned dataset as a CSV file.
7. Load the data into a SQLite database.
8. Analyze the data using SQL.
9. Visualize insights using Power BI.

---

## Input

The pipeline uses a JSONL dataset containing job postings with information such as:

* Job Title
* Company Name
* City
* Job Category
* Job Type
* Salary Range
* Experience Required
* Job Description
* Remote/On-site Status

---

## Data Transformation

The pipeline performs the following operations:

* Removes duplicate records.
* Handles missing values.
* Standardizes date fields.
* Calculates average salary.
* Creates an experience range.
* Classifies jobs as Remote or On-site.
* Extracts technical skills from job descriptions, including Python, SQL, Java, JavaScript, React, AWS, Azure, Docker, Git, Power BI, Excel, Machine Learning, TensorFlow, Pandas, NumPy, Spark, and Hadoop.

---

## Output

### Cleaned Dataset

Location:

`data/cleaned/cleaned_jobs.csv`

Additional columns generated:

* average_salary
* experience_required
* work_mode
* has_python
* has_sql
* has_java
* has_javascript
* has_react
* has_aws
* has_azure
* has_docker
* has_git
* has_power_bi
* has_excel
* has_machine_learning
* has_tensorflow
* has_pandas
* has_numpy
* has_spark
* has_hadoop

### SQLite Database

Location:

`database/jobs.db`

Database Table:

`jobs`

---

## SQL Analysis

The SQL queries answer questions such as:

* Which companies have the most job postings?
* Which cities have the highest number of openings?
* What are the most common job categories?
* What is the average salary by category?
* Which technical skills are most frequently required?

---

## Power BI Dashboard

The dashboard includes:

* Top Hiring Companies
* Top Hiring Cities
* Job Category Distribution
* Remote vs On-site Jobs
* Average Salary by Category
* Skill Demand Analysis


## Project Structure

```text
Job-Market-Data-Pipeline/
│
├── data/
│   ├── raw/
│   └── cleaned/
├── database/
├── powerbi/
├── sql/
├── src/
├── requirements.txt
├── README.md
├── .gitignore
└── pipeline.log
```

---

## Technologies Used

* Python
* Pandas
* SQLite
* SQL
* Power BI
* Git
* GitHub

---

## Running the Project

```bash
git clone <repository-url>

cd Job-Market-Data-Pipeline

pip install -r requirements.txt

cd src

python pipeline.py
```

The pipeline generates:

* `data/cleaned/cleaned_jobs.csv`
* `database/jobs.db`

The cleaned CSV can then be loaded into the Power BI dashboard.

---

## Future Improvements

* Support larger datasets.
* Integrate PostgreSQL or MySQL.
* Automate pipeline execution.
* Add advanced data validation.
* Publish the dashboard online.

---

## Author

**Suchismita Acharya**
