import pandas as pd
from logger import logger


def extract_data(file_path):
    """
    Extract data from a JSON Lines (.jsonl) file.

    Args:
        file_path (str): Path to the raw JSONL file.

    Returns:
        pandas.DataFrame: Extracted dataset.
    """

    try:
        logger.info(f"Starting data extraction from {file_path}")

        # Read JSON Lines file
        df = pd.read_json(file_path, lines=True)

        print("Data extracted successfully!")
        print(f"Total Records: {len(df)}")
        print(f"Total Columns: {len(df.columns)}")

        logger.info(
            f"Data extraction completed successfully. "
            f"Rows: {len(df)}, Columns: {len(df.columns)}"
        )

        return df

    except Exception as e:
        logger.error(f"Data extraction failed: {str(e)}")

        print("\nError while extracting data.")
        print(e)

        return None