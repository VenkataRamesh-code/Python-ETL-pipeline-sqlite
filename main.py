from ETL.extract import extract_data
from ETL.transform import transform_data
from ETL.load import load_to_db

def run_pipeline():
    file_path = "data/raw_sales.csv"

    df = extract_data(file_path)
    df_clean = transform_data(df)
    load_to_db(df_clean)

    print("✅ ETL pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()