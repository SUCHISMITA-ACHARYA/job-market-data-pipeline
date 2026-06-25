from extract import extract_data
from transform import transform_data
from validation import validate_data
from load import load_data
from logger import logger


def main():

    logger.info("========== ETL PIPELINE STARTED ==========")

    file_path = "../data/raw/job_postings.jsonl"

    df = extract_data(file_path)

    if df is None:
        logger.error("Pipeline stopped because extraction failed.")
        return

    cleaned_df = transform_data(df)

    validate_data(cleaned_df)

    load_data(cleaned_df)

    print("\nPipeline Completed Successfully!")

    logger.info("========== ETL PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    main()