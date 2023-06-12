import streamlit as st
import pandas as pd
import yfinance as yf
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
yf.pdr_override()

st.title("FINANCE")
end=dt.datetime.now()
start=end-dt.timedelta(days=365)
stocklist=['TATASTEEL','CGPOWER','TTML','HUDCO']
stocks= [i+'.NS' for i in stocklist]
dt.datetime(2022, 6, 6, 18, 53, 40, 938696)
df=yf.get_data_yahoo(stocks,start,end)
print(df)
st.title("DAY CLOSING")
st.line_chart(df['Close'])
returns=(df['Close']/df['Close'].shift(1)-1)*100
print(returns)
st.title('RETURNS EACH DAY')
st.area_chart(returns)
sns.set_style('whitegrid')
fig1=sns.pairplot(returns[1:],hue='TATASTEEL.NS')
st.title("RETURNS WRT TATASTEEL")
st.pyplot(fig=fig1)
x=df['Volume'].mean().sort_values(ascending=False)
print(x)
st.title('VOLUME')
st.line_chart(x)
