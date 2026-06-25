def validate_data(df):

    print("\n========== DATA VALIDATION ==========")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\n========== VALIDATION COMPLETE ==========\n")