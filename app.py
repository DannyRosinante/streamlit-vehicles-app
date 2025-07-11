import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de ventas de autos')

car_data = pd.read_csv('vehicles_us.csv')

if st.button('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.button('Mostrar dispersión odómetro vs precio'):
    st.write('Dispersión entre odómetro y precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)