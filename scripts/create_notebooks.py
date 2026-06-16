import json
import os

cells = [
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '# Laboratorio interactivo 1: Exploración de datos financieros con Big Data\n',
    '\n',
    '## 1. Introducción\n',
    'El objetivo de este laboratorio es familiarizarse con el flujo básico de análisis de datos financieros. Aquí aprenderás a cargar datos, explorarlos, realizar tareas de limpieza y transformación, visualizar las series de precios y retornos, calcular indicadores financieros sencillos y finalmente construir un primer modelo predictivo de regresión lineal para intentar pronosticar el retorno del siguiente periodo.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    'import pandas as pd\n',
    'import numpy as np\n',
    'import matplotlib.pyplot as plt\n',
    'from sklearn.model_selection import train_test_split\n',
    'from sklearn.linear_model import LinearRegression\n',
    'from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\n',
    '\n',
    '# Configuración de gráficas\n',
    'plt.style.use("ggplot")\n',
    'plt.rcParams["figure.figsize"] = (12, 6)'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 2. Carga de un dataset financiero\n',
    'Al no disponer de un archivo local, generaremos datos simulados que representen el precio de cierre de un activo a lo largo del tiempo.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    '# Generación de datos simulados\n',
    'np.random.seed(42)\n',
    'fechas = pd.date_range(start="2022-01-01", periods=500, freq="B")\n',
    'retornos_sim = np.random.normal(loc=0.0001, scale=0.015, size=500)\n',
    'precios = 100 * np.exp(np.cumsum(retornos_sim))\n',
    '\n',
    'df = pd.DataFrame({\n',
    '    "Fecha": fechas,\n',
    '    "Precio_Cierre": precios\n',
    '})\n',
    '# Introducimos algunos NaN intencionalmente para la limpieza\n',
    'df.loc[10:12, "Precio_Cierre"] = np.nan\n',
    'df.head()'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 3. Lectura y exploración inicial de los datos\n',
    'Vamos a verificar la información del dataframe, el tipo de datos y si existen valores nulos.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    'df.info()'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    'df.describe()'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    '# Detección de valores faltantes\n',
    'print("Valores nulos por columna:\\n", df.isnull().sum())'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 4. Limpieza básica\n',
    'Lidiaremos con los NaN utilizando interpolación o llenado hacia adelante. Además, prepararemos el índice de fechas y calcularemos los retornos.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    '# Convertir a fecha y fijar como índice\n',
    'df["Fecha"] = pd.to_datetime(df["Fecha"])\n',
    'df.set_index("Fecha", inplace=True)\n',
    '\n',
    '# Manejo de NaN: Llenamos los valores nulos con el método forward fill (último valor conocido)\n',
    'df["Precio_Cierre"] = df["Precio_Cierre"].ffill()\n',
    '\n',
    '# Retorno simple\n',
    'df["Retorno_Simple"] = df["Precio_Cierre"].pct_change()\n',
    '\n',
    '# Retorno logarítmico (R_i = ln(P_t / P_{t-1}))\n',
    'df["Retorno_Log"] = np.log(df["Precio_Cierre"] / df["Precio_Cierre"].shift(1))\n',
    '\n',
    'df.dropna(inplace=True) # Eliminar la primera fila que ahora tiene NaN en retornos\n',
    'df.head()'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 5. Visualización inicial\n',
    'Visualizamos la serie de precios y los retornos.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    'fig, ax = plt.subplots(3, 1, figsize=(12, 12), gridspec_kw={"height_ratios": [2, 1, 1]})\n',
    '\n',
    '# Gráfico de precios\n',
    'ax[0].plot(df.index, df["Precio_Cierre"], color="blue")\n',
    'ax[0].set_title("Precio de Cierre Histórico")\n',
    'ax[0].set_ylabel("Precio")\n',
    '\n',
    '# Gráfico de retornos\n',
    'ax[1].plot(df.index, df["Retorno_Log"], color="gray", linewidth=0.8)\n',
    'ax[1].set_title("Retornos Logarítmicos")\n',
    'ax[1].set_ylabel("Retorno")\n',
    '\n',
    '# Histograma de retornos\n',
    'ax[2].hist(df["Retorno_Log"], bins=50, color="orange", edgecolor="black")\n',
    'ax[2].set_title("Distribución de Retornos Logarítmicos")\n',
    '\n',
    'plt.tight_layout()\n',
    'plt.show()'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 6. Cálculo de indicadores simples\n',
    'Agregaremos volatilidad móvil, medias móviles y el retorno acumulado.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    '# Volatilidad (Desviación estándar de 20 días)\n',
    'df["Volatilidad_20d"] = df["Retorno_Log"].rolling(window=20).std()\n',
    '\n',
    '# Medias Móviles\n',
    'df["SMA_20"] = df["Precio_Cierre"].rolling(window=20).mean()\n',
    'df["SMA_50"] = df["Precio_Cierre"].rolling(window=50).mean()\n',
    '\n',
    '# Retorno Acumulado\n',
    'df["Retorno_Acumulado"] = (1 + df["Retorno_Simple"]).cumprod() - 1\n',
    '\n',
    'df.tail()'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 7. Modelo predictivo sencillo\n',
    'Utilizaremos regresión lineal para predecir el retorno del día siguiente usando información de los retornos pasados (lags) y la volatilidad.'
  ]},
  {'cell_type': 'code', 'execution_count': None, 'metadata': {}, 'outputs': [], 'source': [
    '# Creación de variables predictoras (Lags)\n',
    'df["Lag_1"] = df["Retorno_Log"].shift(1)\n',
    'df["Lag_2"] = df["Retorno_Log"].shift(2)\n',
    '\n',
    '# Variable objetivo: El retorno del periodo siguiente\n',
    'df["Target"] = df["Retorno_Log"].shift(-1)\n',
    '\n',
    '# Eliminar NaNs resultantes\n',
    'df_model = df.dropna()\n',
    '\n',
    '# Definición de X e y\n',
    'features = ["Lag_1", "Lag_2", "Volatilidad_20d"]\n',
    'X = df_model[features]\n',
    'y = df_model["Target"]\n',
    '\n',
    '# División en train y test (80% train, 20% test)\n',
    'X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)\n',
    '\n',
    '# Entrenamiento del modelo\n',
    'model = LinearRegression()\n',
    'model.fit(X_train, y_train)\n',
    '\n',
    '# Predicciones\n',
    'y_pred = model.predict(X_test)\n',
    '\n',
    '# Evaluación de métricas\n',
    'mae = mean_absolute_error(y_test, y_pred)\n',
    'mse = mean_squared_error(y_test, y_pred)\n',
    'r2 = r2_score(y_test, y_pred)\n',
    '\n',
    'print(f"MAE: {mae:.5f}")\n',
    'print(f"MSE: {mse:.5f}")\n',
    'print(f"R²: {r2:.5f}")'
  ]},
  {'cell_type': 'markdown', 'metadata': {}, 'source': [
    '## 8. Conclusiones del laboratorio\n',
    '- Hemos limpiado y transformado exitosamente datos crudos en métricas financieras estándar.\n',
    '- La visualización nos permite observar el comportamiento de la serie y la naturaleza leptocúrtica de los retornos.\n',
    '- El modelo de regresión lineal muestra un $R^2$ cercano a cero o negativo, lo que ilustra lo expuesto en el capítulo teórico: los modelos simples basados solo en la acción del precio pasada (sin validación estricta ni selección de variables causales) tienen una capacidad predictiva limitada debido al ruido inherente de los mercados financieros.'
  ]}
]

notebook = {
  'cells': cells,
  'metadata': {
    'kernelspec': {
      'display_name': 'Python 3',
      'language': 'python',
      'name': 'python3'
    },
    'language_info': {
      'codemirror_mode': {'name': 'ipython', 'version': 3},
      'file_extension': '.py',
      'mimetype': 'text/x-python',
      'name': 'python',
      'nbconvert_exporter': 'python',
      'pygments_lexer': 'ipython3',
      'version': '3.12.0'
    }
  },
  'nbformat': 4,
  'nbformat_minor': 5
}

os.makedirs('book/es/01_big_data', exist_ok=True)
os.makedirs('book/en/01_big_data', exist_ok=True)

with open('book/es/01_big_data/laboratorio_bigdata.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

with open('book/en/01_big_data/laboratorio_bigdata.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)
