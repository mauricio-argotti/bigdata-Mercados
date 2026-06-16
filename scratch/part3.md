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
