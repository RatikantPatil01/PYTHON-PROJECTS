import yfinance as yf

def fetch_data(ticker, interval='5m', period='1d'):
    df = yf.download(ticker, interval=interval, period=period)
    df.dropna(inplace=True)
    return df
