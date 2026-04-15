# Análisis de Datos de Viajes en Taxi – Chicago 

### Contexto

El objetivo de este proyecto fue analizar datos de viajes en taxi en Chicago para identificar patrones y evaluar el impacto de factores como el clima en la duración de los viajes.

### Análisis

- Limpieza y transformación de datos con Python (Pandas)
- Análisis exploratorio de datos (EDA)
- Identificación de las empresas con mayor número de viajes
- Identificación de los 10 barrios con mayor número de finalizaciones
- Visualización de datos con Matplotlib

### Prueba de hipótesis

Se evaluó si la duración promedio de los viajes cambia durante sábados lluviosos.

Hipótesis nula (H0): No hay diferencia en la duración promedio de los viajes.

Hipótesis alternativa (H1): Sí existe una diferencia en la duración promedio.

Se utilizó una prueba t para comparar los grupos.

##  Aplicación en Vivo
**[Ver Dashboard →](https://proyecto-7-lrig.onrender.com/)**

## Funcionalidad de la aplicación

La aplicación web proporciona las siguientes funcionalidades:
- Visualización de una vista previa del conjunto de datos.
- Generación de un histograma interactivo para analizar la distribución del kilometraje de los vehículos.
- Generación de un gráfico de dispersión que muestra la relación entre el precio y el kilometraje de los coches.
- Interacción mediante botones que permiten construir las visualizaciones bajo demanda.

##  Tecnologías Utilizadas
- Python
- Streamlit
- Pandas
- Plotly Express

## 📁 Estructura del Proyecto
```
├── app.py              # Aplicación principal de Streamlit
├── vehicles_us.csv     # Dataset de vehículos
├── requirements.txt    # Dependencias del proyecto
├── notebooks/
│   └── EDA.ipynb      # Análisis exploratorio de datos
└── README.md          # Documentación del proyecto


Esta aplicación facilita la comprensión de patrones y relaciones clave dentro del conjunto de datos, apoyando el análisis exploratorio de datos (EDA).

### Conclusiones

Se identificaron patrones importantes en la demanda de viajes por empresa y ubicación.
Además, se encontró evidencia de que las condiciones climáticas pueden influir en la duración de los viajes, lo cual puede ser relevante para la toma de decisiones en servicios de transporte.
