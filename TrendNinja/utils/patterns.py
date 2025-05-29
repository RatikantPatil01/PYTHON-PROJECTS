import pandas_ta as ta

def detect_hammer(df):
    pattern = ta.cdl.hammer(df['Open'], df['High'], df['Low'], df['Close'])
    df['Hammer'] = pattern
    return df
