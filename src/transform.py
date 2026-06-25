import pandas as pd
import re
from logger import logger

def transform_data(df):

    print("\nStarting Data Cleaning...")
    logger.info("Starting data transformation.")

    columns_to_keep = [
        "uniq_id",
        "job_title",
        "company_name",
        "city",
        "category",
        "job_type",
        "post_date",
        "salary_offered",
        "inferred_salary_from",
        "inferred_salary_to",
        "inferred_salary_currency",
        "inferred_min_experience",
        "inferred_max_experience",
        "job_description",
        "is_remote"
    ]

    df = df[columns_to_keep]

 
    df = df.drop_duplicates(subset="uniq_id")

    df = df.dropna(subset=["job_title"])

  
    # Fill missing company names
   
    df["company_name"] = df["company_name"].fillna("Unknown")

 
    # Fill missing cities
  
    df["city"] = df["city"].fillna("Unknown")

    df["post_date"] = pd.to_datetime(df["post_date"])


    df["average_salary"] = (
        df["inferred_salary_from"] +
        df["inferred_salary_to"]
    ) / 2

    df["experience_required"] = (
        df["inferred_min_experience"].astype(str)
        + "-"
        + df["inferred_max_experience"].astype(str)
        + " Years"
    )

    df["work_mode"] = df["is_remote"].map({
        True: "Remote",
        False: "On-site"
    })

    print("Transformation Complete!")
    logger.info("Data transformation completed successfully.")
    df.to_csv(
        "../data/cleaned/cleaned_jobs.csv",
        index=False
    )

    print("Cleaned dataset saved successfully!")
    logger.info("Cleaned dataset saved to data/cleaned/cleaned_jobs.csv")
 

    skills = [
        "Python",
        "SQL",
        "Java",
        "JavaScript",
        "React",
        "AWS",
        "Azure",
        "Docker",
        "Git",
        "Power BI",
        "Excel",
        "C++",
        "C#",
        "Machine Learning",
        "AI",
        "TensorFlow",
        "Pandas",
        "NumPy",
        "Spark",
        "Hadoop"
    ]

    for skill in skills:

        column_name = "has_" + skill.lower().replace(" ", "_").replace("+", "p")

        df[column_name] = df["job_description"].str.contains(
            skill,
            case=False,
            na=False
        )
    return df