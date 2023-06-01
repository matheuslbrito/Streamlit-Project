import streamlit as st
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date

# Página Home
def home():
    col1, col2 , col3 = st.columns(1,5,1)
    with col2:
        st.image('grafico_logo.png')
        st.markdown('---')
        st.title('App Financeiro')
        st.markdown('---')