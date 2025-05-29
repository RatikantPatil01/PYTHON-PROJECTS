# main.py
from utils.setup import install_requirements
install_requirements()
import streamlit as st
from utils.fetcher import fetch_data
from utils.patterns import detect_hammer
from utils.visuals import plot_chart
from utils.risk import calculate_position_size
from utils.alerts import send_alert

# -------------------------------
# Streamlit UI Setup
# -------------------------------
st.set_page_config(page_title='PatternScope', layout='wide')
st.title("🧐 PatternScope - Real-Time Chart Pattern Analyzer")

input_tickers = st.text_input("Enter stock symbols (comma-separated)", "AAPL,TSLA")
tickers = [t.strip().upper() for t in input_tickers.split(',') if t.strip() != '']

capital = st.number_input("Your Trading Capital ($)", min_value=100.0, value=10000.0)
risk_percent = st.slider("Risk per Trade (%)", min_value=0.5, max_value=5.0, value=1.0)

if st.button("Analyze Now"):
    for ticker in tickers:
        st.subheader(f"Analyzing {ticker}")
        try:
            df = fetch_data(ticker)
            df = detect_hammer(df)

            if df['Hammer'].iloc[-1] != 0:
                send_alert(ticker)
                st.success(f"Hammer pattern detected in {ticker}")

            stop_loss = abs(df['Close'].iloc[-1] - df['Low'].iloc[-2])
            position_size = calculate_position_size(capital, risk_percent, stop_loss)
            st.info(f"Entry: {df['Close'].iloc[-1]:.2f}, Stop Loss: {stop_loss:.2f}, Position Size: {position_size} shares")

            plot_chart(df, ticker)
        except Exception as e:
            st.error(f"Error analyzing {ticker}: {e}")
