import plotly.graph_objects as go
import streamlit as st

def plot_chart(df, ticker):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index, open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'], name='Candlestick')])

    hammer_signals = df[df['Hammer'] != 0]
    fig.add_trace(go.Scatter(x=hammer_signals.index, y=hammer_signals['Close'],
                             mode='markers', marker=dict(size=8, color='red'),
                             name='Hammer'))

    fig.update_layout(title=f'{ticker} Chart with Hammer Pattern',
                      xaxis_title='Time', yaxis_title='Price')
    st.plotly_chart(fig)
