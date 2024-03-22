import psycopg
import pandas as pd

# Load stock data from PostgreSQL for all companies
def load_stock_data(conn, symbols):
    dfs = {}
    try:
        for symbol in symbols:
            query = f"SELECT * FROM {symbol}"
            df = pd.read_sql(query, conn)
            dfs[symbol] = df
        return dfs
    except psycopg.Error as e:
        print("Error loading stock data:", e)