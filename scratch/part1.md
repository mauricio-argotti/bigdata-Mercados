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
