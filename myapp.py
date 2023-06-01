import streamlit as st
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

# Página Home
def home():
    col1, col2 , col3 = st.columns([1,5,1])
    with col2:
        st.image('myapp_logo.jpg')
        st.markdown('---')
        st.title('Projeto Final - Matheus Brito')
        st.markdown('---')

def pairs():
    st.title('Pairs Trading')

def momentum():
    st.title('Momentum')

def fundamentos():
    st.title('Fundamentos')
    tickers=['PETR4.SA', 'VALE3.SA', 'EQTL3.SA', 'CSAN3.SA']
    precos = yf.download(tickers, period='1y')['Adj Close']
    st.header('Função st.dataframe()')
    st.dataframe(precos, width=700, height=300)

# Função principal
def main():
    st.sidebar.image('myapp_logo.jpg', width=200)
    st.sidebar.title('Projeto Final')
    st.sidebar.markdown('---')
    lista_menu=['Home', 'Pairs Trading', 'Momentum','Fundamentos']
    escolha = st.sidebar.radio('Escolha a opção', lista_menu)

    if escolha =='Home':
        home()
    if escolha == 'Pairs Trading':
        pairs()
    if escolha =='Momentum':
        momentum()
    if escolha == 'Fundamentos':
        fundamentos()

main()