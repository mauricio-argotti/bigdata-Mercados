<!-- Automatically converted from PDF. Review and correct format if necessary. -->

# Big data in financial markets

**INTRODUCTION** 

The growing digitization of financial markets has generated an ecosystem characterized by massive volumes of data, reduced latencies, and an increasing diversity of information sources. This phenomenon, widely documented in recent literature, has driven the development of predictive models based on Big Data and machine learning to anticipate the directional movement of financial asset prices. However, the proliferation of increasingly complex models—**such as deep neural networks, LSTM, or Transformers**—has introduced a new challenge: **the loss of interpretability and the difficulty of justifying investment decisions based on opaque models**. 

```{figure} ../../_static/big_data_figuras/1_BigData.png
---
name: fig-big-data
width: 100%
align: center
---
Big Data in Financial Markets.
```
 
In parallel, various studies have shown that price action continues to be one of the most robust and stable sources of predictive information, especially in short-term horizons and highly liquid markets. However, the abundance of variables derived from price generates redundancy, multicollinearity, and noise, which compromises the stability of coefficients and the generalization capacity of the models. 

This TeachBook proposes an alternative approach: parsimonious, interpretable, and statistically robust models, built from multivariate analysis and variable selection techniques applied to large volumes of data. The objective is to provide a methodological framework that allows quantitative traders, asset managers, and research teams to build predictive models that are not only accurate, but also explainable and defensible before risk committees, regulators, and academic reviewers. 

## Predictive Models

The world of financial markets has experienced a significant change with the arrival of the big data era and machine learning technology. The ability to process large amounts of data in real time has allowed predictive models to improve their accuracy and effectiveness in price prediction and market pattern detection. However, the complexity of this data and the lack of interpretability of these models pose new challenges for analysts and investors. 

```{figure} ../../_static/big_data_figuras/2_Problema_Actual.png
---
name: fig-panorama
width: 100%
align: center
---
Current Landscape of Predictive Models.
```
 
The complexity and volatility of financial markets have led to the search for more effective solutions for price prediction and informed decision-making. In this context, two key approaches are presented that have proven their ability to improve accuracy and efficiency in the prediction of financial markets. 

Contemporary research in financial modeling is at a turning point marked by the convergence between Big Data, machine learning, and the growing need for explainable models. The use of advanced architectures, from high-frequency data pipelines to deep networks capable of capturing non-linear patterns, has significantly expanded predictive capacity in complex markets. However, this technical sophistication has been accompanied by critical challenges: opacity, fragility to regime changes, overfitting, and difficulties in justifying decisions in regulated environments. 

In this context, price action emerges again as a primary source of robust information, while model governance and interpretability are consolidated as essential requirements to ensure operational reliability. The following sections synthesize recent advances and methodological tensions that define the current state of the field. 

### Predictive models based on Big Data

Recent literature highlights the use of Big Data architectures to process massive streams of financial data in real time, integrating machine learning techniques for price prediction and market pattern detection. These approaches allow handling high-frequency data, order book depth, and alternative signals, but often lack interpretability. 

### Machine learning and deep learning

Models such as Random Forest, SVM, LSTM, and Transformers have shown the ability to capture non-linear relationships and complex patterns in financial time series. However, recent studies warn that their performance can deteriorate significantly in the presence of regime changes, microstructural noise, and overfitting, especially when rigorous validation protocols are not applied. 

### Price action

Price action remains one of the most stable and predictive sources in liquid markets. Recent research shows that many technical indicators derived from price do not provide significant additional information and can introduce redundancy and multicollinearity, affecting the stability of the models. 

### Interpretability and model governance

Growing concern about the opacity of models has fueled interest in explainable approaches (XAI) and linear or semi-linear models that allow understanding the relationship between predictor variables and trading signals. The literature emphasizes the need for models that combine accuracy with interpretability, especially in regulated and high operational risk contexts. 

### Accuracy vs interpretability

Recent literature shows that modern financial prediction moves between two poles. On the one hand, Big Data architectures and deep learning models capable of processing massive volumes of information and capturing non-linear patterns. On the other hand, the growing need for interpretability, stability, and governance in environments where operational risk is critical. 

Although advanced models like Random Forest, SVM, LSTM, and Transformers have demonstrated remarkable performance under controlled conditions, their fragility to regime changes, microstructural noise, and overfitting reveals that historical accuracy does not guarantee future robustness. In contrast, price action emerges as a more stable source of information less susceptible to distortions, while many derived indicators introduce redundancy and degrade model quality. 

Added to this panorama is a transversal finding: complexity does not always translate into better predictive capacity, and in financial markets, explainability is an operational requirement, not a methodological luxury. The literature converges that models must balance accuracy and transparency, integrating rigorous validation practices, dimensionality reduction, and XAI (Explainable Artificial Intelligence) techniques that allow justifying decisions in regulated contexts. 

Furthermore, studies suggest that the future of financial prediction depends not only on more sophisticated models, but on more governable, auditable, and resilient models, capable of maintaining performance under changing conditions and providing understandable signals for decision making. Thus, scientific advancement in the field of financial prediction depends not only on more powerful models, but on more responsible models. The literature converges that the optimal combination integrates robust data (price action), parsimonious or explainable models, strict validation, and solid governance of the model lifecycle. This balance is what allows transforming technical precision into real operational value. 

# Theoretical Foundations

## Big Data in Financial Markets 

The use of Big Data in financial markets has evolved rapidly over the last decade, driven by the digitization of stock market operations, the proliferation of unstructured data sources, and the advancement of high-performance computing. Today, financial institutions, from investment banks to quantitative hedge funds, depend on infrastructures capable of processing massive volumes of information in real time to gain competitive advantages in prediction, risk management, and algorithmic execution. In this context, the classic three Vs of Big Data acquire specific characteristics in the financial field, where technical and analytical requirements are especially demanding. 

## The three Vs of financial Big Data

Big Data in financial markets has become a fundamental tool for decision making, risk management, and the detection of business opportunities. This phenomenon is based on three key characteristics, known as the **"Three Vs"**: **Volume**, **Velocity**, and **Variety**.

```{figure} ../../_static/big_data_figuras/3_Torbellino_Big_Data.png
---
name: fig-torbellino
width: 100%
align: center
---
The three Vs of Big Data in Financial Markets.
```

The image visually synthesizes the structural complexity of Big Data applied to financial markets, articulating the classic three Vs—Volume, Velocity, and Variety—as forces that generate a turbulent, non-linear, and high-dimensional informational environment. The vortex of data, formulas, and numerical flows accurately represents the chaotic yet structured nature of the modern market, where billions of observations per second, millions of signals per hour, and multiple heterogeneous sources converge to form an informational ecosystem that exceeds human processing capacity.

### **Volume**: millions of intraday observations and alternative data. 

In modern financial markets, the volume of data grows exponentially. Not only are millions of intraday observations generated per asset—prices, volumes, orders, cancellations—but new sources of alternative data are also incorporated, such as: 

- Mobile device geolocation, 
- Satellite images, 
- Electronic transaction records, 
- Weather data, 
- Social media activity, 
- Digital behavior metrics. 

According to recent estimates, a medium-sized quantitative fund can process between 1 and 10 terabytes of raw data daily. This growth requires the use of distributed architectures (Hadoop, Spark), cloud storage, and intelligent compression and filtering techniques. 

#### Data Volume ($V$) 

The total amount of data ($V$) generated in a time interval (analysis interval defined by the analyst: a second, an hour, a market session, etc.). According to {cite:p}`gandomi2015beyond`, the formula that best explains this criterion is: 

$$
V = N \times S
$$ (eq-volume)

Where: 

- $N$ = Number of records generated during a time interval 
- $S$ = Average size in bytes of each record. 

_**Example:**_

If 50,000 ticks are generated in 1 second and each tick takes 120 bytes, then the volume of data generated in a second is 6 million bytes. 

### **Velocity**: millisecond latencies and automated decisions.

Velocity is critical in financial markets, especially in _high-frequency trading_ (HFT) and _market making_ strategies. Competition is measured in milliseconds or even microseconds. 

- Trading systems must process market data feeds with latencies of less than 1 ms. 
- Algorithmic decisions, pattern detection, order execution, risk management, are automated to avoid human delays. 
- Infrastructure is optimized through co-location, low-latency networks, and specialized hardware (FPGAs, GPUs). 

Velocity not only affects execution but also analysis: nowcasting models, intraday prediction, and anomaly detection require streaming data pipelines (Kafka, Flink) capable of updating estimates in real time. 

#### Data Generation Velocity (**$V_e$**):

The data generation velocity is a metric that quantifies how quickly a financial system produces observable events, such as transactions, order book updates, or bid/ask changes, within a specific time interval. This metric allows evaluating the intensity of the information flow that a predictive model or Big Data architecture must process in real time. Mathematically, according to {cite:p}`chen2014big`, it is defined as: 

$$
V_e = \frac{N}{\Delta t}
$$ (eq-velocity)

Where:

$N$ = Number of events generated or observable changes in data flows (transactions, order updates, etc.) 

$\Delta t$ = Time interval. 

_**Example:**_

Suppose that, in a 1-second interval, 12,000 order book updates, 1,500 executed transactions, and 3,000 bid/ask changes were recorded. When calculating the data generation velocity ($V_e$), this indicates that a total of 16,500 events were produced in that period, that is, a rate of 16,500 events per second. 

### **Variety**: prices, volumes, news, sentiment, derivatives. 

The variety of financial data has increased drastically. Traditional time series are no longer enough; modern models integrate multiple types of heterogeneous information: 

- **Structured data**: prices, volumes, yield curves, implied volatilities. 
- **Semi-structured data**: limit order books (LOB), FIX messages, regulatory reports. 
- **Unstructured data**: economic news, corporate reports, social media posts, earnings call transcripts, textual sentiment via NLP. 

Recent research shows that models combining traditional data with alternative data, for example, Twitter sentiment or semantic analysis of news, can improve predictive capacity between 5% and 20%, depending on the asset and the time horizon. 

Additionally, variety includes model-derived data: realized volatility, liquidity indicators, neural network-generated embeddings, etc. This diversity requires advanced integration, cleaning, and temporal alignment techniques. 

From the point of view of analyzing data variety prior to building predictive models, there are numerous useful metrics to size the importance and utility of data in this process. Some of the most relevant, according to Gandomi (2015), are: data type cardinality, structural complexity index, Shannon entropy for textual data, effective dimensionality for numerical data, and diversity of independent sources. Although all these metrics provide value, the most crucial one, the one that truly determines what type of data is useful for a predictive model, is effective dimensionality. 

#### Effective Dimensionality ($D_{e}$)

According to {cite:t}`jolliffe2016principal`, effective dimensionality is the actual number of independent dimensions in a dataset. It is a measure that reflects how much informational structure actually exists, beyond the redundancy, correlation, and noise present in the data. Formally, effective dimensionality corresponds to the rank of the data matrix, that is, the number of linearly independent column vectors that provide unique information for modeling. 

Let $X$ be a data matrix of size $n\times p$, where 

- $n = \text{number of observations}$ 
- $p = \text{number of variables}$ 

Effective dimensionality ( $D_e$ ) is defined as: 

$$
D_e = \text{rank}(X)
$$ (eq-dimensionality)

Where: 

$\text{rank}(X)$ = number of linearly independent columns. Mathematically it is calculated using: 

- **SVD** decomposition 
- **QR** decomposition 
- **Eigenvalues** of the covariance matrix 

Equivalently: 

$$
D_e = \sum_{i=1}^{p} \mathbf{1}_{(\lambda_i > 0)}
$$ (eq-dimensionality-eigenvalues)

Where: 

$\lambda_i$ are the eigenvalues of the covariance matrix $X^{T}X$ 

_**Example:**_

Suppose an analyst builds a dataset with a total of 300 variables distributed as follows: 

- 200 technical indicators 
- 40 volatility variables 
- 30 volume variables 
- 20 microstructure variables 
- 10 sentiment variables 

When analyzing the correlation matrix and calculating its rank, the following result is obtained: 

$$ 
D_{e} = rank (X) = 8 
$$ (eq-dimensionality-example)

This implies that, despite having 300 variables, only 8 dimensions contain truly independent information. The remaining variables are redundant; many of them are linear combinations of others, and together they can cause multicollinearity problems. Furthermore, many of these variables are derived transformations of the same price or another source, mainly providing noise and little useful additional information for modeling. 

# Conceptual Architecture of the Data Flow

In modern financial markets, trend-based predictive analysis depends directly on the ability to manage the Three Vs of Big Data: volume, velocity, and variety. The growing volume of transactions, the extreme velocity with which market events are generated, and the increasing variety of sources—prices, volumes, order books, news, sentiment, and alternative data—require designing architectures capable of capturing, processing, and transforming heterogeneous information into robust predictive signals. In this context, the quality of the model depends not only on the technique used but on the system's ability to integrate diverse data, clean it, temporally align it, and extract the relevant informative structure from it to anticipate the direction of the price. 

{numref}`fig-flujo-datos` illustrates precisely this logic through three functional layers representing the complete flow of a Big Data-based predictive system. The first layer, acquisition and data sources, integrates information from traditional markets (prices, volumes, microstructure), alternative data (social networks, satellite images, sentiment), and economic fundamentals. The second layer, real-time processing and analysis, applies cleaning, normalization, multivariate analysis, and dimensionality reduction techniques to transform raw data into informative representations suitable for modeling. Finally, the third layer, decision and feedback, uses quantitative models to generate actionable trading signals, continuously evaluate them, and feed back the system, closing the learning and optimization cycle. 

```{figure} ../../_static/big_data_figuras/4_Flujo_de_datos_Mercados.png
---
name: fig-flujo-datos
width: 100%
align: center
---
Conceptual Architecture of the Data Flow in Financial Markets.
```
 
This structure reflects how, in an environment dominated by Big Data, competitive advantage does not come solely from the predictive model, but from the capacity of the entire architecture to convert massive, fast, and varied data into accurate and timely decisions. 

## Acquisition and data sources layer

This first part of the image, located at the initial end of the flow, represents the massive and heterogeneous input of information: intraday quotes, order books, news, social media, macroeconomic indicators, and alternative data. Here, the first two Vs materialize: 

- **Volume**, due to the magnitude of observations generated every second. 
- **Variety**, due to the coexistence of structured data (prices, volumes) and unstructured data (text, sentiment, satellite images in specialized cases). 

In this context, the modern financial system no longer depends only on market data, but on a much broader informational ecosystem that requires semantic integration and automated cleaning. 

## Real-time processing and analysis layer 

In the center of the diagram, the processing core is observed, where data flows are transformed through streaming analytics, machine learning, and predictive algorithms. Here, Velocity is emphasized, as systems must operate with millisecond latencies to allow automatic decisions in algorithmic trading or risk management. 

The efficiency of the system depends on the ability to process and react in real time, turning velocity into a design principle, not just a technical feature. 

## Decision and feedback layer 

In the final part of the flow, where analytical results are translated into decisions such as buy/sell orders, risk alerts, and portfolio adjustments, the three Vs are integrated, making the system data-driven because: 

- The **volume** of data feeds the predictive models. 
- The **variety** of data provides a multidimensional view of the market. 
- The **velocity** ensures that decisions are timely and competitive. 

This final phase closes the cycle, evidencing the transition of traditional financial systems, based on retrospective analysis, towards predictive and adaptive environments, where information flows continuously and feeds back the models. 

# Price Action as a Predictive Core 

Price action constitutes the strategic and methodological starting point to better understand the underlying dynamics of the market. Instead of relying on external signals, opaque models, or derived indicators that dilute the actual structure of the movement, this approach focuses the analysis on what the market truly reveals: the interaction between prices, volume, internal divergences, and the context of the dominant trend. 

Below, the five groups of variables that make up this predictive core are described, each capturing an essential aspect of market behavior before, during, and after a trend change. 

## Primary variables 

Primary variables represent the quantitative heart of the analysis. They are direct, untransformed, and highly interpretable measures that describe the behavior of price and volume in the 18 candles prior to the ET instant (inflection point). Their function is to capture market microstructure just before a directional shift occurs. 

```{figure} ../../_static/big_data_figuras/5_Problemas_estructurales.png
---
name: fig-variables-primarias
width: 100%
align: center
---
Primary Variables.
```
 
This image shows the architecture of the primary variables useful for capturing relevant information regarding market microstructure. An exhaustive measure analysis demonstrated that 18 periods prior to the ET inflection point allow obtaining measures with significant and satisfactory results in understanding market dynamics. Furthermore, the analysis of measures with this number of periods showed that the primary variable architecture correlates significantly with relevant market microstructure information, suggesting that this architecture is effective in capturing key market patterns and trends. 

### Price-based variables

These variables quantify the way the price moves, oscillates, and disperses in the short term. They include measures such as: 

- The closing price spread, 
- The mean of the returns, 
- The dispersion of those returns. 

Their purpose is to describe the intensity, stability, and directionality of the recent price movement, allowing to identify whether the market is in expansion, contraction, or transition. 

#### Logarithmic return ($R_i$) 

The logarithmic return of a financial asset is the logarithmic variation between two consecutive closing prices, allowing the relative price change to be measured over a specific period. This statistical measure is particularly useful in finance analysis, as it provides information on the trend and volatility of an asset's price. According to {cite:t}`campbell1997econometrics` the logarithmic return is obtained as follows: 

$$
R_i = \ln\left(\frac{cp_i}{cp_{i-1}}\right)
$$ (eq-return-log)

Where: 

$cp_i$= closing price registered by a financial asset in period $i$ 
$cp_{i-1}$= closing price registered by a financial asset in period $i-1$

_**Example:**_

Assuming the euro/dollar exchange rate has the following closing prices ($cp_i$) for the days $cp_{i-1}$= 1.1528 and $cp_i$= 1.1568, applying the formula for the logarithmic return $R_i$: 

$$
R_i = \ln\left(\frac{1.1568}{1.1528}\right) = 0.00346
$$ (eq-example-return)

The value of 0.00346 represents the logarithmic return in continuous terms obtained between two periods. In percentage, this return is equivalent to approximately 0.346%, reflecting the relative rate of change of the asset in that interval. 

### Volume-based variables

In financial markets, volume acts as an indicator of market activity and interest, functioning as its **"pulse"**. However, in forex trading, the actual transaction volume is not observable in real-time due to its OTC (Over The Counter) nature. Therefore, proxy variables are used, such as tick volume, which represents the number of price changes in a given period and has proven to be a useful indicator of market activity. In this context, these variables capture aspects such as: 

- The amplitude of the traded proxy volume, 
- The average variation of that volume, 
- The dispersion or volatility of these variations. 

Volume analysis, even in its proxy form, helps to confirm or contradict price action. A price movement without an increase in proxy volume may lack credibility, while a movement accompanied by an increase in volume often anticipates the continuation or a breakout in the trend. These variables allow evaluating the internal strength of the movement and the intensity of interest in the market. 

#### Volume volatility ($\sigma_v$)

Volume volatility is a statistical measure that quantifies the dispersion, variability, or instability of the traded volume (or proxy volume, such as tick volume) around its mean in a given period. It reflects the intensity and irregularity of market activity, allowing the identification of phases of accumulation, distribution, breakout, or trend exhaustion. According to Hasbrouck et al. {cite:p}`hasbrouck2007empirical`, mathematically, it corresponds to the standard deviation of the volume over a specified time window. 

$$
\sigma_v = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(v_i - \bar{v})^2}
$$ (eq-volatility-volume)

Where: 

- $v_i$ = Volume or tick volume in period $i$ 
- $\bar{v}$ = Average volume 
- $n$ = Number of observations 

Furthermore, in quantitative analysis and market microstructure, volume volatility must be interpreted relatively. This is because volume, and especially tick volume in **OTC markets** such as **Forex**, presents highly variable distributions depending on the asset, the volatility regime, and the time of day. 

In this context, scientific literature establishes that activity levels must be evaluated using percentile-based thresholds, derived from the asset's own historical distribution. This methodology is supported by fundamental works such as those by {cite:t}`karpoff1987relation`, {cite:t}`hasbrouck2007empirical`, and {cite:t}`campbell1997econometrics`, who demonstrate that the market's informational intensity manifests in relative increases in volume variability, not in absolute values. 

The following table summarizes the universally accepted thresholds for classifying volume volatility in financial Big Data. 

```{table} Thresholds based on volume volatility percentiles
:name: tabla-volatilidad
:align: center

|Volatility<br>Level|Mathematical<br>Criterion|Interpretation|
|---|---|---|
|Low|𝜎𝑣< P25|**Reduced activity**; low market interest; unreliable<br>price movements.|
|Normal|P25 ≤𝜎𝑣≤ P75|**Typical**<br>**market**<br>**activity**;<br>stable<br>conditions;<br>movements with moderate credibility.|
|High|𝜎𝑣> P75|**Significant increase in activity**; higher informational<br>intensity; high probability of trend breakout or continuation.|
|Extremely<br>High<br>(informational<br>event)|𝜎𝑣> P90|**Exceptional activity**; entry of institutional players; macro<br>announcements; high probability of impulsive movements.|
```

It is important to keep in mind that a sharp increase in volume volatility (𝜎𝑣) usually anticipates support/resistance breakouts, trend changes, impulsive movements, the entry of institutional participants, among other key aspects in the trading of financial instruments. 

_**Example:**_

To illustrate how volume volatility is evaluated in financial Big Data, consider the EUR/USD pair's tick volume on 5-minute candles. These values represent market activity over five consecutive intervals, as summarized in {numref}`tabla-volatilidad`. 

```{table} EUR/USD pair Tick Volume (5 minutes)
:name: tabla-volatilidad
:align: center

|**Minute**|**Tick Volume**|
|---|---|
|1|980|
|2|1200|
|3|1500|
|4|1100|
|5|2100|
```

By calculating the mean tick volume value, $\bar{v}= 1376$ ticks, and the volume volatility experienced over the 5 minutes, $\sigma_v = 448.2$ ticks. The volume volatility for EUR/USD is 448.2 ticks. 

Now suppose that, from a historical window of 2,000 EUR/USD observations, the following percentiles are obtained: 

```{table} EUR/USD pair historical percentiles 
:name: tabla-percentiles
:align: center

|Percentile|Value<br>(ticks)|Volatility|Operational interpretation|
|---|---|---|---|
|P25|180|Low|Reduced activity; low market interest;<br>unreliable price movements.|
|P50|260|Normal (mean)|Typical market behavior; stable<br>conditions; moderate credibility.|
|**P75**|**410**|**High**|**Significant increase in activity**; higher informational<br>intensity; high probability of trend breakout or<br>continuation.|
|P90|580|Extremely High<br>(informational event)|Exceptional activity; entry of institutional players;<br>macro announcements; impulsive and directional movements.|
```

When making an operational interpretation based on the above percentiles and a volume volatility of 448.2 ticks, located above the 75th percentile, it indicates: 

- Significant increase in `Market Activity`, 
- Higher `informational intensity`, 
- High probability of trend `breakout or continuation`, 
- Possible entry of `institutional participants`. 

In building predictive models, this level of activity usually reinforces price signals, anticipates directional movements, and filters out false signals when volume is low. 

### Variables measuring decouplings

In market analysis, there are phenomena called decouplings, where different market components show divergent behaviors. These decouplings can be critical signals in the formation of `Inflection Points`, that is, changes in the overall market trend. Below are some variables that measure these decouplings: 

**Discrepancies between price and volume** 

When the price rises or falls without trading volume accompanying it, or vice versa, it can be an indicator that the market is experiencing a decoupling. This can be a sign that the trend is changing. 

**Discrepancies between indicators** 

Divergence between different technical indicators, for example, such as the relative strength index (RSI), the simple moving average (SMA), and the exponential moving average (EMA), can also be an indicator of decoupling. When these indicators show divergent results, it can be a sign that the market is experiencing a transition phase. 

**Discrepancies between price and other market indicators** 

Divergence between the price of a financial asset and other market indicators, such as buyer and seller activity, trader positioning, and the overall economy, can also be an indicator of decoupling. This can be a sign that the market is experiencing a change in trend. 

#### Normalized divergence measure (D)

In quantitative market analysis and in the field of financial Big Data, one of the most robust tools for detecting decouplings between price, volume, and technical indicators is normalized divergence. According to {cite:t}`campbell1997econometrics`, this measure allows identifying when two variables that normally evolve coherently begin to show divergent behaviors, which usually anticipates inflection points, trend changes, or structural breakouts in the market. 

Normalized divergence is defined as: 

$$
D = \frac{\Delta A_i - \Delta B_i}{\sigma_{\Delta A - \Delta B}}
$$ (eq-normalized-divergence)

Where: 

$A_i$, $B_i$ = series being compared (for example, price vs. volume, price vs. RSI, RSI vs. EMA), $\sigma_{\Delta A - \Delta B}$ = historical sample standard deviation of the difference between both series. 

This normalization is fundamental because: it eliminates the effect of different units, allows comparing decouplings between multiple variables, turns the difference into a statistically interpretable magnitude, and allows detecting significant events when the divergence exceeds 1.5, 2, or more standard deviations. 

When analyzing decoupling patterns in financial information, it is important to establish thresholds to determine the predictive relevance of the results. In operational terms, these thresholds can be classified as follows: 

- |D| < 1 → `Normal decoupling`, without predictive relevance, 
- |D| > 2 → `Statistically Significant Event`, 
- |D| > 3 → Strong transition signal or `Inflection Point`. 

This metric is especially useful in Forex, where real volume is not observable, and proxies like tick volume are used. Normalized divergence allows evaluating whether the price, volume, and technical indicators are aligned or if there is a decoupling anticipating a regime change. 

_**Example:**_

Below is an example based on EUR/USD pair data in 1-hour candles. The example includes: closing prices, $RSI (14P)$ values, calculation of variations, normalized divergence, and operational interpretation. 

```{table} Historical series of closing price and RSI(14) value of the EUR/USD pair
:name: tab-divergencia
:align: center

|Period|Closing Price (`EUR/USD`)|RSI(14P)|
|---|---|---|
|i-4|1.0830|58|
|i-3|1.0845|55|
|i-2|1.0860|52|
|i-1|1.0875|49|
|i|1.0900|44|
```

In {numref}`tab-divergencia` a clear decoupling in the market is observed, where the price achieves a 70-point increase from 1.0830 to 1.0900, while the RSI(14P) drops drastically from 58 to 44 points. This decrease in the internal strength of the movement, despite the increase in price, is an indication of a **classic decoupling**, where price and internal strength are not aligned. In {numref}`tabla-eur-usd-rsi` the procedure used for the calculation of the **normalized divergence** ($D$) is summarized: 

```{table} Normalized divergence ($D$) 
:name: tabla-eur-usd-rsi
:align: center


|Period|Closing price|RSI(14P)|∆ P|∆ RSI|∆$𝑃_𝑖$−∆$𝑅𝑆𝐼_𝑖$|$𝐷_𝑃$, $𝑅𝑆𝐼_(𝑖)$|
|---|---|---|---|---|---|---|
|i-4|1.0830|58|||||
|i-3|1.0845|55|0.0014|-0.0531|0.054|2.07|
|i-2|1.0860|52|0.0014|-0.0561|0.057|2.19|
|i-1|1.0875|49|0.0014|-0.0594|0.061|2.31|
|i|1.0900|44|0.0023|-0.1076|0.110|4.18|
|||||$\sigma_{ΔP−ΔRSI}$:|**0.026**||
```

According to the results obtained, the last column shows the values of the normalized divergence $𝐷_𝑃,   𝑅𝑆𝐼(𝑖)$. In the ΔP and ΔRSI columns, the decoupling is highlighted in all sections, since while the closing price rises, the RSI values fall. This is reflected in $𝐷_𝑃,   𝑅𝑆𝐼(𝑖) > 2$. It is important to note that the last section is clearly critical, as the price accelerates upwards, the RSI plummets, and the normalized divergence reaches an exceptional value of 4.18, making it a very rare event. 

In terms of the logic of inflection points, the first three sections suggest a progressive decoupling, while the last section presents a significant divergence in which the occurrence of an inflection point that deserves to be analyzed further can be intuited. 

## Structural problems in price action-based prediction

Contemporary literature on `Prediction of the Directional Movement of Financial Asset Prices` has achieved significant advances in terms of computational capacity. However, these advances have not been accompanied by a deep understanding of the mechanisms governing price action. In the context of building predictive models, there is a set of structural, recurring, and widely documented problems that limit the effectiveness of existing models. Below is a brief summary of the main problems currently influencing the construction of predictive models, as shown in the following figure. 


```{figure} ../../_static/big_data_figuras/6_Problemas_Estructurales.png
---
name: fig-problemas-estructurales
width: 100%
align: center
---
Structural problems in the formulation of predictive models.
```
 

### Lack of interpretability in predictive models

One of the most important problems currently influencing the construction of predictive models is the inability of dominant models to explain why they predict what they predict. Techniques such as **LSTM**, **SVM**, **deep neural networks**, or **hybrid models** achieve high levels of predictive accuracy, but this success is achieved at the expense of understanding the underlying mechanisms that generate the predictions. In a financial environment, where decisions must be justifiable, this opacity is unacceptable. 

The consequence of this problem is twofold: on the one hand, the analyst cannot understand which variables drive the signal or determine the direction of the price, and on the other hand, the model cannot be economically audited or validated. 

This methodological gap constitutes the starting point for structuring and formulating a methodology that allows building parsimonious predictive models, and thus becomes an open problem for research. 

### Excessive complexity and `Black Box` nature

Literature has evolved towards increasingly complex models, with deep architectures, hard-to-calibrate hyperparameters, and highly non-linear behaviors. However, this complexity does not translate into a proportional improvement in performance, but it does introduce several problems, such as: 

- Extreme sensitivity to data structure 
- Dependence on specific configurations 
- Difficulty in replicating results 

In this context, results from recent research suggest that excessive complexity and the `Black Box` nature of these models have displaced understanding of the underlying phenomenon, limiting their generalization capacity and performance improvement in different scenarios. 

### Overfitting and low generalization capacity 

Machine learning models and other statistical models frequently fall into the trap of capturing spurious patterns present in historical data. This limitation makes them unable to accurately reproduce in future scenarios, particularly in modeling financial asset prices, where: 

- The underlying trend signal is frequently hidden by price noise and volatility in the market. 
- Price distributions change over time, making generalization and the development of robust models difficult. 
- Complexity without `Parsimony` can lead to fragile models prone to overfitting, which reduces their predictive capacity. 

To address this challenge, it is necessary to develop innovative strategies and techniques that allow models to be more flexible and adaptable to changes in distributions and relationships between variables, and that mitigate the problem of overfitting, thereby improving the accuracy and reliability of predictive models. 

### Parametric instability in the face of structural market changes

By understanding the financial market as a complex and dynamic environment, characterized by permanent structural changes in volatility, correlations, and price regimes, predictive models, in addition to being accurate, must also be stable and able to adapt to `Market Regime` changes. However, this instability is a challenge for many traditional models, which can be sensitive to changes in market parameters. Some of the problems associated with parametric instability in financial models include: 

- Sensitivity to changes in market volatility, which can affect the model's accuracy. 
- Changes in correlations between assets, which can generate incorrect results. 
- Changes in the `Market Regime`, which can cause significant deviations. 

In this operating context, model instability can have significant consequences that can lead to various problems such as incorrect decision-making that can result in financial losses, undermine confidence in the models, and hinder informed decision-making. To address these challenges, it is necessary to develop more flexible models that can adapt to market changes. 

### Non-normal distributions in price returns

It is well known that returns on financial instruments, especially those generated by trading the EUR/USD exchange rate, present: 

- Marked skewness, 
- Extreme leptokurtosis, 
- Heavy tails, 
- High concentration of small values. 

These characteristics violate the normality assumptions underlying many traditional statistical methods. Ignoring the verification of these assumptions hinders the use of multivariate statistical methods for building predictive models and can lead to erroneous conclusions and misspecified models. 

### Poor variable selection and excess of indicators 

One of the biggest challenges in building predictive models to forecast asset price direction or trend is identifying the variables that truly have a causal and discriminant impact on price movement (relevance). The common tendency to adopt the paradigm that "**more variables are better**" can lead to multicollinearity problems and the formation of overfitted and hard-to-interpret models, where the indiscriminate inclusion of technical, financial, or fundamental analysis-derived indicators does not guarantee a better prediction. 

Excessive use of variables often sacrifices interpretability and traceability of the model, in addition to requiring dimensionality reduction techniques such as principal component analysis or factor analysis, which transform original variables into components or factors, but make it difficult to understand which specific factors drive the prediction. Therefore, the key is to identify and select variables with high discriminative and causal power, those that have the ability to clearly differentiate when an asset will tend to rise or fall. The correct selection of these relevant variables allows building models that are not only accurate but also interpretable and useful for decision making, avoiding excessive reliance on an excessive volume of indicators that, ultimately, can decrease the predictive capacity and clarity of the model. 

### Absence of context analysis prior to trend changes

Many studies in the financial field focus on predicting returns, classifying movements, or detecting patterns, but generally fail to thoroughly analyze the moments preceding price inflection points. These moments, in which valuable information about possible trend changes is concentrated, are often underestimated or overlooked, limiting the complete understanding of market dynamics. 

This methodological gap can hinder the early identification of relevant changes and reduce the ability to anticipate significant movements, representing an important limitation for the development of more robust and explanatory predictive models. By ignoring the moments before inflection points, where the most valuable information is concentrated, the understanding of actual market dynamics is implicitly limited. In this context, building a predictive model without considering a reference point in the market, to serve as a basis for applying existing knowledge, can significantly limit its accuracy and usefulness, hindering the detection of relevant patterns and anticipation of future changes. 

### Excessive reliance on exogenous data or `Sentiment Analysis`

**Price action**, if properly analyzed, can provide valuable information for building effective predictive models, reducing to some extent the reliance on exogenous data. From the perspective of the efficient market hypothesis in its strongest form, all relevant information is already reflected in the price, which implies that market movements immediately reflect investor expectations and valuations. 

In this context, technical analysis, focused on variables measuring price action, such as moving averages, support and resistance levels, candlestick patterns, momentum and volume indicators, turns out to be a useful tool for identifying trends and inflection points in the market. However, it is important to recognize that, in practice, external variables such as news, macroeconomic or political events can influence the market and affect the stability and predictability of models based solely on price action. 

Although these events can introduce noise, on many occasions, price action reflects, in real time, the sum of market expectations and reactions, constituting a valuable indicator for decision making, always complemented by an adequate contextual analysis. 

### Lack of parsimonious, robust, and stable models

Current literature lacks parsimonious models that simultaneously meet the following characteristics: 

- `Interpretable`: easy to understand and explain how the relationships between variables work. 
- `Accurate`: capable of making accurate predictions, based on input data. 
- `Generalizable`: capable of predicting accurately in different contexts and scenarios with new data or scenarios, without the need for additional adjustments. 

This approach must be centered on the structural selection of variables, which means that predictor variables are identified and selected according to the specifications of the method used. Therefore, the purpose of the variable selection process is to maintain causality, traceability, and interpretability of the estimated values based on the predictor variables that best explain and model the phenomenon under simulation and prediction. 

# Final synthesis 

The identified problems form an ecosystem of limitations that has prevented price action-based prediction from advancing towards explanatory, robust, and scientifically sound models. Therefore, the solution regarding the construction of predictive models is not to increase their complexity, but to understand market structure, selecting relevant variables that allow building parsimonious models. 

```{caution}
In building predictive models for asset price direction or trend, it is important to avoid including price-derived variables without prior analysis of their discriminative capacity, multicollinearity, independence, and multivariate structure.
``` 

## **Chapter Bibliography.** 

- Gandomi, A., & Haider, M. (2015). Beyond the hype: Big data concepts, methods, and analytics. International Journal of Information Management, 35(2), 137–144. 
- Chen, M., Mao, S., & Liu, Y. (2014). Big Data: A Survey. Mobile Networks and Applications, 19, 171–209. 
- Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: a review and recent developments.  Philosophical Transactions of the Royal Society A. 
- Campbell, J. Y., Lo, A. W., & MacKinlay, A. C. (1997). The Econometrics of Financial Markets. Princeton University Press. 
- Hasbrouck, J. (2007). Empirical Market Microstructure. Oxford University Press. 
- Karpoff (1987). The Relation Between Price Changes and Trading Volume. Journal of Financial and Quantitative Analysis 

