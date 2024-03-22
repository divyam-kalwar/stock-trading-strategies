import psycopg

def connect_to_db():
    try:
        conn = psycopg.connect(
            dbname="stockdata",
            user="postgres",
            password="root123",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg.Error as e:
        print("Error connecting to PostgreSQL database:", e)

def add_pnl_column(conn, symbol):
    try:
        # Create a cursor object
        cur = conn.cursor()

        # Check if the column already exists
        cur.execute(
            f"SELECT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = '{symbol}' AND column_name = 'pnl')")
        column_exists = cur.fetchone()[0]

        if not column_exists:
            # SQL command to add PnL column to stock table
            alter_query = f"ALTER TABLE {symbol} ADD COLUMN pnl FLOAT;"

            # Execute the SQL command
            cur.execute(alter_query)

            # Commit the transaction
            conn.commit()

            print("PnL column added successfully to the table:", symbol)
        else:
            print("PnL column already exists in the table:", symbol)

    except psycopg.Error as e:
        print("Error adding PnL column to table:", e)
        conn.rollback()  # Rollback transaction in case of error

    finally:
        # Close cursor
        cur.close()

def store_pnl_to_db(conn, symbol, cumulative_pnl):
    try:
        cursor = conn.cursor()
        query = f"UPDATE {symbol} SET pnl = %s"
        cursor.execute(query, (cumulative_pnl,))
        conn.commit()
        print("PnL data stored successfully.")
    except psycopg.Error as e:
        conn.rollback()
        print("Error storing PnL data:", e)
    finally:
        if cursor:
            cursor.close()
