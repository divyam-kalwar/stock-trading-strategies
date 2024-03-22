from trading_signals import generate_trading_signals
from pnl_calculation import calculate_pnl
from database_operations import connect_to_db, add_pnl_column, store_pnl_to_db
from visualization import visualize_trading_data
from data_loader import load_stock_data


def main():
    # Connect to PostgreSQL database
    conn = connect_to_db()

    # Define the symbol for which you want to analyze the stock data
    symbol = 'AAPL'

    # Load stock data for the specified symbol from the database
    dfs = load_stock_data(conn, [symbol])
    df = dfs[symbol]

    # Generate trading signals
    df = generate_trading_signals(df)

    # Calculate profit and loss
    df, cumulative_pnl = calculate_pnl(df)

    # Add PnL column to the stock table
    add_pnl_column(conn, symbol)

    # Store PnL data to database
    store_pnl_to_db(conn, symbol, cumulative_pnl)

    # Visualize trading data
    visualize_trading_data(df, symbol)

    # Close database connection
    conn.close()


if __name__ == "__main__":
    main()
