# Prueba técninca Sumz

# Sumz

Este repositorio contiene el código y los archivos necesarios para replicar los experimentos y el modelo predictivo de demanda desarrollado para Sumz. El objetivo de este proyecto es crear un modelo preciso para estimar las unidades vendidas de cada artículo en un comercio minorista y responder a preguntas de negocio sobre la estacionalidad, el impacto de la competencia y la tendencia de demanda.

## Configuración del Entorno

Para replicar todos los experimentos, es crucial configurar un entorno virtual con Python 3.10 o 3.11. Los pasos a seguir son:

1. **Crear un entorno virtual**
   - Si se usa `venv`, correr el siguiente comando en la terminal:
     ```bash
     python3 -m venv nombre_del_entorno
     ```
   - Si se usa `conda`, correr el siguiente comando en la terminal:
     ```bash
     conda create -n nombre_del_entorno python=3.10
     ```

2. **Activar el entorno virtual**
   - En `venv`, activar el entorno:
     - En Windows:
       ```bash
       nombre_del_entorno\Scripts\activate
       ```
     - En macOS/Linux:
       ```bash
       source nombre_del_entorno/bin/activate
       ```
   - En `conda`, activar el entorno:
     ```bash
     conda activate nombre_del_entorno
     ```

3. **Instalar las dependencias**
   - Asegurarse de estar en la raíz del repositorio y ejecutae:
     ```bash
     pip install -r requirements.txt
     ```
   Esto instalará todas las librerías necesarias para el experimento y la aplicación.

## Ejecución de la Aplicación de Streamlit

Para correr la aplicación en Streamlit y visualizar las gráficas interactivas que responden a las preguntas de negocio, además de utilizar el modelo predictivo de una manera amigable, seguir estos pasos:

1. **Posicionarse en la raíz del repositorio**
   - Asegurarse de estar en la carpeta principal del proyecto.

2. **Ejecutar la aplicación**
   - En la terminal, correr el siguiente comando:
     ```bash
     streamlit run app.py
     ```

Esto abrirá una interfaz interactiva en el navegador donde se podrá:
- Navegar por las diferentes secciones de la aplicación y responder a las preguntas de negocio.
- Realizar predicciones cargando el archivo `demanda_test.csv` en la sección "Predicciones modelo".

## Estructura del Repositorio

El repositorio contiene los siguientes archivos y carpetas clave:

- `app.py`: Archivo principal de la aplicación en Streamlit.
- `requirements.txt`: Archivo de dependencias para instalar los paquetes necesarios.
- `Datos/`: Carpeta con los datasets `catalogo_productos.csv`, `demanda.csv` y `demanda_test.csv`.
- `Model/`: Carpeta que almacena el preprocesador y el modelo final en formato `.joblib` para su carga en la aplicación.

## Notas Adicionales

- Asegurarse de que todos los archivos de datos se encuentren en la carpeta `Datos/` para que el código pueda acceder a ellos sin problemas.
- Las predicciones generadas se guardarán en un archivo `predicciones_demanda.csv` en la raíz del repositorio.

