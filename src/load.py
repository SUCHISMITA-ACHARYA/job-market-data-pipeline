import sqlite3
from logger import logger


def load_data(df):

    logger.info("Connecting to SQLite database.")

    print("\nConnecting to SQLite Database...")

    connection = sqlite3.connect("../database/jobs.db")

    df.to_sql(
        "jobs",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("Database Loaded Successfully!")

    logger.info("SQLite database loaded successfully.")