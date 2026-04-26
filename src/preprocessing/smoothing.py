def smooth_price(df, window=5):
    df['Smoothed'] = df['Close'].rolling(window=window).mean()
    return df