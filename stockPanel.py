import streamlit as st
import pandas as pd
import yfinance as yf

st.write("""# Stock Tracker""")

symbol = 'xau'
data = yf.Ticker(symbol)
df = data.history(period='1d',start='2010-01-01',end='2022-05-1')
st.line_chart(df.Close)

