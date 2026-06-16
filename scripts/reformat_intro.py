import re

with open(r'D:\Maourice\Universidad\Usal\Libros\bigdata-Mercados\Recursos\Pdf\0. Capitulo 1 Big Data.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Ecuaciones
text = text.replace('**==> picture [40 x 8] intentionally omitted <==**\n', 
r'''
$$
V = N \times S
$$ (eq-volumen)
''')

text = text.replace('**==> picture [36 x 24] intentionally omitted <==**\n',
r'''
$$
V_e = \frac{N}{\Delta t}
$$ (eq-velocidad)
''')

text = text.replace('**==> picture [70 x 11] intentionally omitted <==**\n',
r'''
$$
D_e = \text{rank}(X)
$$ (eq-dimensionalidad)
''')

text = text.replace('**==> picture [79 x 11] intentionally omitted <==**\n',
r'''
$$
D_e = \sum_{i=1}^{p} \mathbf{1}_{(\lambda_i > 0)}
$$ (eq-dimensionalidad-autovalores)
''')

text = text.replace('**==> picture [218 x 25] intentionally omitted <==**\n',
r'''
$$
R_i = \ln\left(\frac{cp_i}{cp_{i-1}}\right)
$$ (eq-retorno-log)
''')

text = text.replace('**==> picture [329 x 25] intentionally omitted <==**\n',
r'''
$$
R_i = \ln\left(\frac{1.1568}{1.1528}\right) = 0.00346
$$ (eq-ejemplo-retorno)
''')

text = text.replace('**==> picture [132 x 50] intentionally omitted <==**\n',
r'''
$$
\sigma_v = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(v_i - \bar{v})^2}
$$ (eq-volatilidad-volumen)
''')

text = text.replace('**==> picture [94 x 26] intentionally omitted <==**\n',
r'''
$$
D = \frac{\Delta A_i - \Delta B_i}{\sigma_{\Delta A - \Delta B}}
$$ (eq-divergencia-normalizada)
''')

# Figuras
text = text.replace('**==> picture [468 x 238] intentionally omitted <==**\n\nFigura 1. Big Data en los Mercados Financieros.',
r'''
```{figure} ../../_static/big_data_figuras/1_BigData.png
---
name: fig-big-data
width: 100%
align: center
---
Big Data en los Mercados Financieros.
```
''')

text = text.replace('**==> picture [468 x 196] intentionally omitted <==**\n\nFigura 2. Panorama Actual de los Modelos Predictivos.',
r'''
```{figure} ../../_static/big_data_figuras/2_Problema_Actual.png
---
name: fig-panorama
width: 100%
align: center
---
Panorama Actual de los Modelos Predictivos.
```
''')

text = text.replace('**==> picture [468 x 256] intentionally omitted <==**\n\nFigura 3. Big Data en los Mercados Financieros',
r'''
```{figure} ../../_static/big_data_figuras/3_Torbellino_Big_Data.png
---
name: fig-torbellino
width: 100%
align: center
---
Las tres V del Big Data en los Mercados Financieros.
```
''')

text = text.replace('**==> picture [468 x 200] intentionally omitted <==**\n\nFigura 4 Arquitectura Conceptual del Flujo de Datos en los Mercados Financieros',
r'''
```{figure} ../../_static/big_data_figuras/4_Flujo_de_datos_Mercados.png
---
name: fig-flujo-datos
width: 100%
align: center
---
Arquitectura Conceptual del Flujo de Datos en los Mercados Financieros.
```
''')

text = text.replace('**==> picture [468 x 217] intentionally omitted <==**\n\nFigura 5. Variables Primarias',
r'''
```{figure} ../../_static/big_data_figuras/5_Problemas_estructurales.png
---
name: fig-variables-primarias
width: 100%
align: center
---
Variables Primarias.
```
''')

text = text.replace('**==> picture [469 x 225] intentionally omitted <==**\n\nFigura 6. Problemas estructurales en la formulación de modelos predictivos.',
r'''
```{figure} ../../_static/big_data_figuras/6_Problemas_Estructurales.png
---
name: fig-problemas-estructurales
width: 100%
align: center
---
Problemas estructurales en la formulación de modelos predictivos.
```
''')

# Admonition TIP
text = text.replace('## **TIP**\n\nEn la construcción',
r'''
```{admonition} Consejo (Tip)
:class: tip

En la construcción
''')
text = text.replace('independencia y estructura multivariante.', 'independencia y estructura multivariante.\n```')

# Referencias cruzadas - Citas
text = text.replace('(Gandomi 2015)', '{cite:p}`gandomi2015beyond`')
text = text.replace('(Chen, 2014)', '{cite:p}`chen2014big`')
text = text.replace('Según Jolliffe (2016)', 'Según {cite:t}`jolliffe2016principal`')
text = text.replace('De acuerdo con (Campbell, 1997)', 'De acuerdo con {cite:t}`campbell1997econometrics`')
text = text.replace('(Hasbrouck, 2007)', '{cite:p}`hasbrouck2007empirical`')
text = text.replace('como Karpoff (1987), Hasbrouck (2007) y Campbell, Lo & MacKinlay (1997)', 'como {cite:t}`karpoff1987relation`, {cite:t}`hasbrouck2007empirical` y {cite:t}`campbell1997econometrics`')
text = text.replace('Campbell (1997)', '{cite:t}`campbell1997econometrics`')

# Referencias cruzadas - Figuras y Tablas
text = text.replace('La Figura 4 ilustra', 'La {numref}`fig-flujo-datos` ilustra')
text = text.replace('Tabla 1.', '```{table} Umbrales según percentiles de volatilidad del volumen\n:name: tabla-volatilidad\n:align: center\n')
# We need to close the table block. Since the table ends with an empty line, let's fix it manually later if needed, 
# actually MyST table wrappers must wrap the markdown table. Let's do it right.

text = re.sub(r'(Tabla 1\. Umbrales según percentiles de volatilidad del volumen\n\n\|.*?)\n\n\n', 
r'''```{table} Umbrales según percentiles de volatilidad del volumen
:name: tabla-volatilidad
:align: center

\1
```

''', text, flags=re.DOTALL)
text = text.replace('Tabla 1. Umbrales según percentiles de volatilidad del volumen\n\n', '')

text = text.replace('la tabla 1', 'la {numref}`tabla-volatilidad`')

text = re.sub(r'(Tabla 2\. Tick Volume del par EUR/USD \(5 minutos\)\n\n\|.*?)\n\n\n', 
r'''```{table} Tick Volume del par EUR/USD (5 minutos)
:name: tabla-tick-volume
:align: center

\1
```

''', text, flags=re.DOTALL)
text = text.replace('Tabla 2. Tick Volume del par EUR/USD (5 minutos)\n\n', '')


text = re.sub(r'(## Tabla 3\. Percentiles históricos del par EUR/USD\n\n\|.*?)\n\n\n', 
r'''```{table} Percentiles históricos del par EUR/USD
:name: tabla-percentiles
:align: center

\1
```

''', text, flags=re.DOTALL)
text = text.replace('## Tabla 3. Percentiles históricos del par EUR/USD\n\n', '')


text = re.sub(r'(Tabla 4\. Series históricas del precio de cierre y el valor RSI \(14\) del par EUR/USD\n\n\|.*?)\n\n\n', 
r'''```{table} Series históricas del precio de cierre y el valor RSI (14) del par EUR/USD
:name: tabla-eur-usd-rsi
:align: center

\1
```

''', text, flags=re.DOTALL)
text = text.replace('Tabla 4. Series históricas del precio de cierre y el valor RSI (14) del par EUR/USD\n\n', '')
text = text.replace('la Tabla 4', 'la {numref}`tabla-eur-usd-rsi`')


text = re.sub(r'(Tabla 5\. Divergencia normalizada \(D\)\n\n\|.*?)\n\n\n', 
r'''```{table} Divergencia normalizada (D)
:name: tabla-divergencia
:align: center

\1
```

''', text, flags=re.DOTALL)
text = text.replace('Tabla 5. Divergencia normalizada (D)\n\n', '')


with open(r'book/es/01_big_data/intro.md', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'book/en/01_big_data/intro.md', 'w', encoding='utf-8') as f:
    f.write('*(Traducción pendiente)*\\n')

