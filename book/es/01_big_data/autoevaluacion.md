# Autoevaluación del Capítulo 1

## Presentación
Esta sección ha sido diseñada para consolidar los conocimientos adquiridos en el capítulo de *Big Data y Modelos Predictivos en los Mercados Financieros*. A través de un cuestionario interactivo, podrás poner a prueba tu comprensión de los conceptos clave abordados en la teoría.

## Objetivos
- Evaluar la comprensión de las tres "V" del Big Data aplicadas a los mercados financieros, con especial énfasis en la *Velocidad* y *Dimensionalidad Efectiva*.
- Reforzar el entendimiento del rol de la *acción del precio* frente a modelos complejos (LSTM, Transformers) y su susceptibilidad al ruido.
- Validar la interpretación operativa de indicadores clave como la volatilidad del volumen y la divergencia normalizada.

## Metodología
A continuación se presenta una serie de preguntas de opción múltiple. Lee detenidamente cada enunciado y selecciona la respuesta que consideres correcta. Al responder, recibirás retroalimentación automática e inmediata, explicando por qué la opción es correcta o incorrecta según lo estudiado en el capítulo. Esta autoevaluación no es calificada, su propósito es estrictamente formativo.

---

````{only} html
```{code-cell} ipython3
:tags: ["remove-input"]
from jupyterquiz import display_quiz
display_quiz("quiz_cap1.json")
```
````

````{only} latex
```{admonition} Pregunta 1
:class: dropdown

**¿Cuál de las siguientes afirmaciones describe correctamente la velocidad en el contexto del Big Data financiero?**

- a) Cantidad total de datos generados por unidad de tiempo.
- b) Rapidez con la que se producen y procesan los eventos del mercado, como actualizaciones del libro de órdenes.
- c) Número de tipos distintos de datos utilizados en un modelo predictivo.
- d) Número de columnas independientes en una matriz de datos.

**Respuesta correcta:** b) Rapidez con la que se producen y procesan los eventos del mercado, como actualizaciones del libro de órdenes.

**Explicación:** Correcto. El documento define la velocidad como la rapidez con la que se generan eventos financieros y la necesidad de procesarlos en milisegundos.
```

```{admonition} Pregunta 2
:class: dropdown

**Según el documento, ¿por qué la acción del precio sigue siendo una fuente robusta de información predictiva?**

- a) Porque incorpora automáticamente datos alternativos como imágenes satelitales.
- b) Porque es menos susceptible a ruido y redundancia que muchos indicadores derivados.
- c) Porque elimina la necesidad de modelos predictivos.
- d) Porque garantiza predicciones perfectas en mercados líquidos.

**Respuesta correcta:** b) Porque es menos susceptible a ruido y redundancia que muchos indicadores derivados.

**Explicación:** Correcto. La acción del precio es más estable y menos redundante que muchos indicadores derivados, los cuales introducen ruido.
```

```{admonition} Pregunta 3
:class: dropdown

**¿Qué representa la dimensionalidad efectiva (De) en un conjunto de datos financieros?**

- a) El número total de variables disponibles.
- b) El número de variables que presentan correlación perfecta.
- c) El número real de dimensiones independientes en la matriz de datos.
- d) El número de observaciones por unidad de tiempo.

**Respuesta correcta:** c) El número real de dimensiones independientes en la matriz de datos.

**Explicación:** Correcto. El documento define De como el número de columnas linealmente independientes (rango de la matriz).
```

```{admonition} Pregunta 4
:class: dropdown

**¿Qué indica un valor de divergencia normalizada |D| > 3 entre precio y RSI?**

- a) Un desacoplamiento normal sin relevancia predictiva.
- b) Un evento estadísticamente significativo que puede anticipar un punto de inflexión.
- c) Un error en el cálculo del RSI.
- d) Que el precio y el RSI evolucionan de forma perfectamente alineada.

**Respuesta correcta:** b) Un evento estadísticamente significativo que puede anticipar un punto de inflexión.

**Explicación:** Correcto. El documento establece que |D| > 3 indica un evento raro y crítico, asociado a transiciones o puntos de inflexión.
```

```{admonition} Pregunta 5
:class: dropdown

**¿Cuál de los siguientes problemas se menciona como una limitación clave de los modelos complejos como LSTM o Transformers?**

- a) Su incapacidad para capturar patrones no lineales.
- b) Su fragilidad ante cambios de régimen y sobreajuste.
- c) Su excesiva simplicidad y baja capacidad predictiva.
- d) Su imposibilidad de procesar datos de alta frecuencia.

**Respuesta correcta:** b) Su fragilidad ante cambios de régimen y sobreajuste.

**Explicación:** Correcto. El documento indica que estos modelos pueden deteriorarse ante cambios de régimen, ruido microestructural y sobreajuste.
```

```{admonition} Pregunta 6
:class: dropdown

**Según el documento, una volatilidad del volumen (σv) situada por encima del percentil 75 indica:**

- a) Actividad reducida y movimientos poco fiables.
- b) Actividad típica del mercado sin relevancia operativa.
- c) Aumento significativo de la actividad y mayor intensidad informacional.
- d) Un evento informacional extremadamente raro.

**Respuesta correcta:** c) Aumento significativo de la actividad y mayor intensidad informacional.

**Explicación:** Correcto. El percentil 75 corresponde a Alta volatilidad, asociada a mayor intensidad informacional.
```
````
