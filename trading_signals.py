import pandas as pd
# Generate trading signals for all companies
def generate_trading_signals(df):
    # Calculate moving averages
    df['SMA_5'] = df['close'].rolling(window=5).mean()
    df['SMA_10'] = df['close'].rolling(window=10).mean()
    df['SMA_20'] = df['close'].rolling(window=20).mean()
    df['SMA_50'] = df['close'].rolling(window=50).mean()
    df['SMA_200'] = df['close'].rolling(window=200).mean()
    df['SMA_500'] = df['close'].rolling(window=500).mean()

    # Initialize signals column with zeros
    df['signal'] = 0
    # Generate buy signals
    df.loc[(df['SMA_50'] > df['SMA_500']) & (df['SMA_50'].shift(1) < df['SMA_500'].shift(1)), 'signal'] = 1
    # Generate sell signals
    df.loc[(df['SMA_20'] < df['SMA_200']) & (df['SMA_20'].shift(1) > df['SMA_200'].shift(1)), 'signal'] = -1
    # Close buy positions
    df.loc[(df['SMA_10'] < df['SMA_20']) & (df['SMA_10'].shift(1) > df['SMA_20'].shift(1)), 'signal'] = 0
    # Close sell positions
    df.loc[(df['SMA_5'] < df['SMA_10']) & (df['SMA_5'].shift(1) > df['SMA_10'].shift(1)), 'signal'] = 0
    return df