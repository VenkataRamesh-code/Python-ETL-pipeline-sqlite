import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    """Read data from CSV source"""
    print("📥 Extracting data...")
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error in extraction: {e}")
        raise