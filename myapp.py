#!pip install streamli
#!pip install yfinance

import streamlit as st
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

# Página Home
#def home():
#    col1, col2 , col3 = st.columns([1,5,1])
#    with col2:
#        st.image('myapp_logo.jpg')
#        st.markdown('---')
#        st.title('Projeto Final - Matheus Brito')
#        st.markdown('---')

st.title('Funções de Dados')


tickers=['PETR4.SA', 'VALE3.SA', 'EQTL3.SA', 'CSAN3.SA']

precos = yf.download(tickers, period='1y')['Adj Close']

st.header('Função st.dataframe()')
st.dataframe(precos, width=700, height=300)

st.header('Função st.table()')

st.table(precos.head(10))

st.subheader('Funções st.dataframe e st.table com pandas style')

st.dataframe(precos.head(10).style.highlight_max(axis=1))

st.table(precos.head(10).style.highlight_max(axis=1))


st.subheader('Função st.metric()')

st.metric('Temperatura', value='27ºC', delta='1%')

ultimo_petr4 = round(precos['PETR4.SA'].iloc[-1],2)
penultimo_petr4 = precos['PETR4.SA'].iloc[-2]
var_petr4 = round(((ultimo_petr4/penultimo_petr4)-1)*100,2)

st.metric('Cotação PETR4', value=ultimo_petr4, delta=f'{var_petr4}%')