import pyodbc

def load_to_db(df):
    """Load data into SQL Server database (SSMS)"""
    print("Loading data to SQL Server...")

    try:
        # Connect to SQL Server
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=MyPracticeSalesDB;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )

        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='salesdata' AND xtype='U')
        CREATE TABLE sales (
            order_id INT,
            customer VARCHAR(100),
            amount FLOAT,
            date VARCHAR(50),
            amount_with_tax FLOAT
        )
        """)
        conn.commit()

        # Insert data
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO sales (order_id, customer, amount, date, amount_with_tax)
                VALUES (?, ?, ?, ?, ?)
            """,
                           row.order_id,
                           row.customer,
                           row.amount,
                           row.date,
                           row.amount_with_tax
                           )

        conn.commit()
        conn.close()
        print(" Data loaded successfully into SQL Server!")

    except Exception as e:
        print(f" Error in loading: {e}")
        raise