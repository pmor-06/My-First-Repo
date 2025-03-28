import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('/notebook/vehicles_us.csv') # Read csv data file

st.header('Construir un histograma') # Create a header to explain the app

hist_button = st.button() # Create the button

if hist_button: # If click in the button
    st.write('Creación de un histograma para el conjunto de datos de anuncios de ventas de vehículos de coches en Estados Unidos')

    fig = px.histogram(car_data, x="odometer") # Create histogram
    fig.show() # Show graphic
    st.plotly_chart(fig, use_container_width=True) # Show an interactive chart

dis_button = st.button('Construir un gráfico de dispersión')

if dis_button: # If click in the button
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de ventas de vehículos de coches en Estados Unidos')

    fig = px.scatter(car_data, x="odometer", y="price") # Create an dispersion graph
    fig.show() # Show the graph
    st.plotly_chart(fig, use_container_width=True) # Show an interactive chart