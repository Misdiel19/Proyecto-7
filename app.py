import streamlit as st
import pandas as pd
import plotly.express as px

# Títulos
st.title("Proyecto 7 – Vehicles US")
st.header("Análisis exploratorio de anuncios de coches")

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

st.write("Vista previa del dataset:")
st.write(df.head())

# -------- Botón 1: Histograma --------
hist_button = st.button("Mostrar histograma del odómetro")

if hist_button:
    st.write("Generando histograma del odómetro...")
    fig_hist = px.histogram(
        df,
        x="odometer",
        title="Distribución del kilometraje (odometer)"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# -------- Botón 2: Gráfico de dispersión --------
scatter_button = st.button("Mostrar gráfico de dispersión (precio vs kilometraje)")

if scatter_button:
    st.write("Generando gráfico de dispersión...")
    fig_scatter = px.scatter(
        df,
        x="odometer",
        y="price",
        title="Precio vs Kilometraje",
        labels={
            "odometer": "Kilometraje",
            "price": "Precio"
        }
    )
    st.plotly_chart(fig_scatter, use_container_width=True)