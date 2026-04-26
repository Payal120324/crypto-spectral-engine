import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    
    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Sort properly
    df = df.sort_values('Date')
    
    return df