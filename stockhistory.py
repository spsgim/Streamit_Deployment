import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
import yfinance as yf
import streamlit as st
import datetime

# Header
st.header(':blue[Historical Stock Prices]', divider='rainbow')

col1,col2, col3 = st.columns(3)
with col1:
    ticker = st.text_input('Ticker', 'AAPL', key='placeholder')
with col2:
    start_date = st.date_input('From', datetime.date(2020,3,1) )
with col3:
    end_date = st.date_input('To', datetime.date(2024, 5,30) )
    
    
data = yf.Ticker(ticker)
df = data.history(period='1d',start = start_date, end=end_date )

st.dataframe(df)
st.write(f'{ticker} Historical Close Price')
st.line_chart(df['Close'])