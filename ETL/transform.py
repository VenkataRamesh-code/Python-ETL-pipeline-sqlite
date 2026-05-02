import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform data"""
    print("🔄 Transforming data...")

    # Handle missing values
    df['amount'] = df['amount'].fillna(0)
    df['date'] = df['date'].fillna('2024-01-01')

    # Convert types
    df['amount'] = df['amount'].astype(float)

    # Add derived column
    df['amount_with_tax'] = df['amount'] * 1.1

    # Remove duplicates (good practice)
    df = df.drop_duplicates()

    return df