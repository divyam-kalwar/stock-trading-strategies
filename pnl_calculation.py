import pandas as pd

def calculate_pnl(df):
    # Initialize position and P&L columns
    df['Position'] = 0
    df['PnL'] = 0
    cumulative_pnl = 0

    # Initialize variables to track position and P&L
    position = 0
    entry_price = 0

    # Iterate over rows in DataFrame
    for index, row in df.iterrows():
        # Check for entry signals
        if row['signal'] == 1 and position == 0:  # Buy signal and no existing position
            position = 1  # Enter long position
            entry_price = row['close']  # Record entry price

        elif row['signal'] == -1 and position == 1:  # Sell signal and existing long position
            # Calculate P&L for long position
            df.loc[index, 'PnL'] = row['close'] - entry_price
            cumulative_pnl += row['close'] - entry_price
            position = 0  # Close long position
            entry_price = 0  # Reset entry price

        elif row['signal'] == 0 and position == 1:  # Close existing long position
            # Calculate P&L for long position
            df.loc[index, 'PnL'] = row['close'] - entry_price
            cumulative_pnl += row['close'] - entry_price
            position = 0  # Close long position
            entry_price = 0  # Reset entry price

        elif row['signal'] == -1 and position == 0:  # Sell signal and no existing position
            position = -1  # Enter short position
            entry_price = row['close']  # Record entry price

        elif row['signal'] == 1 and position == -1:  # Buy signal and existing short position
            # Calculate P&L for short position
            df.loc[index, 'PnL'] = entry_price - row['close']
            cumulative_pnl += entry_price - row['close']
            position = 0  # Close short position
            entry_price = 0  # Reset entry price

        elif row['signal'] == 0 and position == -1:  # Close existing short position
            # Calculate P&L for short position
            df.loc[index, 'PnL'] = entry_price - row['close']
            cumulative_pnl += entry_price - row['close']
            position = 0  # Close short position
            entry_price = 0  # Reset entry price
    return df, cumulative_pnl
