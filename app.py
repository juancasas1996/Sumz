# Importar librerías necesarias
import pandas as pd
import joblib
import numpy as np
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title("Solución prueba Sumz")

# Barra lateral con menú desplegable
opcion = st.sidebar.selectbox(
    "Seleccione una opción:",
    ["Pregunta 1", "Pregunta 2", "Pregunta 3", "Predicciones modelo"]
)











# Contenido para cada opción del menú
if opcion == "Pregunta 1":
    st.subheader("Pregunta 1: ¿Cuál es la estacionalidad de las ventas?, ¿la estacionalidad cambia dependiendo del producto?")
    st.markdown("""
    La estacionalidad en la demanda de productos es claramente visible en el análisis general y por categoría. Observamos picos en la demanda en los meses de **enero** y **diciembre**, lo cual probablemente está relacionado con festividades importantes, donde el consumo de ciertos productos tiende a aumentar. Este patrón estacional general sugiere que las celebraciones de inicio y fin de año son momentos clave en los que la demanda de diversos productos se incrementa.
    """)

    # Leer y mostrar el archivo HTML interactivo
    with open("Imagenes_streamlit/demanda_mensual_interactiva.html", "r") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)
    # Añade gráficos o análisis específicos para la pregunta 1

    st.markdown("""
    A lo largo del año, entre estos dos picos (enero y diciembre), la demanda cae significativamente en los meses intermedios, con niveles particularmente bajos antes y despues de la temporada de verano. Sin embargo, algunas categorías muestran patrones de estacionalidad adicionales. Por ejemplo, en frutas_y_verduras y carnes_y_aves, se observa un tercer pico en la demanda durante el verano, alcanzando niveles similares a los de las festividades de inicio y fin de año. Esto podría estar relacionado con el hecho de que, durante las vacaciones de verano, las personas pasan más tiempo en casa y consumen más de estos productos frescos.
    """)

    # Leer y mostrar el archivo HTML interactivo
    with open("Imagenes_streamlit/estacionalidad_categorias_interactiva.html", "r") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)
    # Añade gráficos o análisis específicos para la pregunta 1























elif opcion == "Pregunta 2":

    st.markdown("## Pregunta 2: ¿Cúal fué el impacto de la apertura del competidor?")

    st.markdown("""
    ### Demanda promedio antes y después de la apertura del competidor
    - **Demanda promedio antes de la apertura**: 352.97
    - **Demanda promedio después de la apertura**: 282.89
    """)

    st.markdown("### Demanda promedio por categoría:")
    # Crear dos columnas
    col1, col2 = st.columns(2)

    # Contenido de la primera columna
    with col1:
        st.markdown("""
        - **Bebidas**:  
        - Antes de apertura: 365.98  
        - Después de apertura: 306.85
        - **Congelados**:  
        - Antes de apertura: 221.82  
        - Después de apertura: 174.19
        - **Shampoos**:  
        - Antes de apertura: 281.32  
        - Después de apertura: 238.13
        - **Panadería y Panificados**:  
        - Antes de apertura: 311.98  
        - Después de apertura: 249.66
        - **Carnes y Aves**:  
        - Antes de apertura: 377.09  
        - Después de apertura: 326.65
        - **Productos Enlatados y Alimentos Envasados**:  
        - Antes de apertura: 318.71  
        - Después de apertura: 320.64
        """)

    # Contenido de la segunda columna
    with col2:
        st.markdown("""
        - **Aseo**:  
        - Antes de apertura: 486.64  
        - Después de apertura: 244.36
        - **Cereales y Productos Secos**:  
        - Antes de apertura: 321.13  
        - Después de apertura: 321.08
        - **Productos Lácteos**:  
        - Antes de apertura: 399.16  
        - Después de apertura: 191.48
        - **Frutas y Verduras**:  
        - Antes de apertura: 274.19  
        - Después de apertura: 208.75
        - **Jabones**:  
        - Antes de apertura: 380.40  
        - Después de apertura: 346.62
        """)

    # Leer y mostrar el archivo HTML interactivo
    with open("Imagenes_streamlit/demanda_competencia_interactiva.html", "r") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)


    st.markdown("""
                Como se puede observar en la gráfica superior y en la Demanda promedio por categoria, 
                todos los productos a excepcion de los productos Enlatados y Alimentos Envasados, tuvieron una reducción
                en la demanda despues del 2 de julio de 2021, fecha en la que entró en operación una tienda de la competencia a pocos metros
                
                Se puede conncluir que desde que la competencia entró en operación, la demanda ha sido mucho menor casi todos los productos. Esta reducción
                de demanda se observa en la gráfica superior, en la que la demanda promedio antes de la apertura de la tienda era de 352.97, mientras que
                la demanda promedio despues de la apertura de la tienda es de 282.89, una reduccion del 19.85% """)


















elif opcion == "Pregunta 3":
    st.markdown("## Pregunta 3: ¿Las ventas tienen una tendencia creciente o decreciente?")
    st.markdown(
        """
    1.  Antes de la apertura del competidor: Existe una ligera tendencia decreciente en la demanda, reflejada por una pendiente negativa pequeña (-0.01). Esto indica que la demanda ya mostraba una leve disminución con el tiempo, incluso antes de la entrada de la competencia.
                
        """)
    
    st.markdown(
        """
	2. Después de la apertura del competidor: La pendiente negativa sigue siendo igual, (-0.01), lo que sugiere que la tendencia decreciente en la demanda sigue siendo negativa tras la apertura del competidor. Esta diferencia sugiere que la competencia podría haber tenido un impacto adicional en la reducción de la demanda.

        """)

    # Leer y mostrar el archivo HTML interactivo
    with open("Imagenes_streamlit/tendencia_demanda_competencia.html", "r") as f:
        html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)
    # Añade gráficos o análisis específicos para la pregunta 1












if opcion == "Predicciones modelo":
    st.subheader("Predicciones del modelo")
    st.markdown("Cargar csv de los datos que se quieren predecir. Debe ser un csv y debe contener date y id_producto")

    # Cargar el archivo CSV de entrada
    uploaded_file = st.file_uploader("Carga tu archivo demanda_test.csv", type="csv")
    
    if uploaded_file is not None:
        # Cargar el archivo de características por producto
        caracteristicas_producto = pd.read_csv("caracteristicas_producto.csv")

        # Cargar el archivo de prueba subido
        demanda_test = pd.read_csv(uploaded_file, sep=',')

        # Procesar los datos para la predicción
        demanda_test = demanda_test.merge(caracteristicas_producto, on='id_producto', how='left')
        demanda_test['date'] = pd.to_datetime(demanda_test['date'])
        demanda_test['dia'] = demanda_test['date'].dt.day
        demanda_test['mes'] = demanda_test['date'].dt.month
        demanda_test['año'] = demanda_test['date'].dt.year
        demanda_test['dia_semana'] = demanda_test['date'].dt.dayofweek
        demanda_test['Competencia'] = demanda_test['date'] >= pd.Timestamp('2021-07-02')
        
        # Aplicar one-hot encoding a las variables categóricas
        demanda_test_encoded = pd.get_dummies(demanda_test, columns=['categoria', 'subcategoria', 'tamaño'], drop_first=True)

        # Cargar el preprocesador y el modelo entrenado
        preprocessor = joblib.load('Model/preprocessor.joblib')
        final_model = joblib.load('Model/lightgbm_model.joblib')

        # Preparar el DataFrame para la predicción
        X_demanda_test = demanda_test_encoded.drop(columns=["date"])
        X_demanda_test_processed = preprocessor.transform(X_demanda_test)

        # Realizar la predicción
        predicciones = final_model.predict(X_demanda_test_processed)
        predicciones_redondeadas = np.rint(predicciones).astype(int)

        # Añadir las predicciones al DataFrame de prueba
        demanda_test['prediccion_demanda'] = predicciones_redondeadas

        # Mostrar una muestra de las predicciones
        st.write("Predicciones para las primeras filas:")
        st.write(demanda_test[['date', 'id_producto', 'prediccion_demanda']].head(20))

        # Guardar las predicciones en un archivo CSV
        demanda_test[['date', 'id_producto', 'prediccion_demanda']].to_csv("predicciones_demanda.csv", index=False)
        st.success("Predicciones guardadas en 'predicciones_demanda.csv'.")

        # Enlace para descargar el archivo con las predicciones
        with open("predicciones_demanda.csv", "rb") as f:
            st.download_button("Descargar predicciones", f, file_name="predicciones_demanda.csv")

        # Crear y mostrar el histograma con Plotly
        fig = px.histogram(
            x=predicciones_redondeadas,
            nbins=100,
            title="Histograma de Predicciones Redondeadas de Demanda"
        )
        fig.update_layout(
            xaxis_title="Demanda Predicha",
            yaxis_title="Frecuencia"
        )
        st.plotly_chart(fig)

        st.markdown("## En promedio, el modelo se equivoca en 24 unidades de demanda al hacer predicciones. Y comparado a la media de los datos de entrenamiento, el modelo tiene un error de aproximadamente 7.5%")