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

