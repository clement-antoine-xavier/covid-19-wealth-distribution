# COVID-19 and Wealth Distribution Analysis

A comprehensive econometric analysis examining the impact of the COVID-19 pandemic on wealth distribution in the Euro Area, with a focus on Germany, France, and Slovenia.

## 🎯 Overview

This project combines distributional wealth accounts data from the European Central Bank with COVID-19 epidemiological data to analyze how the pandemic disrupted wealth accumulation trends and exacerbated inequality across different European economies.

## 🔬 Research Questions

1. **Pandemic Impact**: How has COVID-19 affected wealth distribution in Euro Area countries compared to pre-pandemic trends?
2. **Demographic Effects**: Which wealth segments (by percentile) experienced the most significant changes during the pandemic? How did the top 10% vs bottom 50% evolve?
3. **Correlation Analysis**: How do COVID-19 infection rates and mortality correlate with changes in wealth inequality metrics?
4. **Predictive Deviation**: To what extent did actual wealth metrics deviate from pre-pandemic linear trend predictions?
5. **Cross-Country Comparison**: How do countries with different initial inequality levels (Germany, France, Slovenia) respond differently to the pandemic shock?

## 📊 Data Sources

### Wealth Distribution Data

- **Source**: [European Central Bank - Distributional Wealth Accounts](https://data.ecb.europa.eu/)
- **Coverage**: Quarterly data (2016-2025)
- **Metrics**:
  - Adjusted total assets and net wealth of households
  - Mean and median wealth distributions
  - Gini coefficients (inequality measure)
  - **Distributional breakdowns** (new):
    - Net wealth by decile (D1-D10)
    - Top 10%, Top 5%, and Bottom 50% absolute wealth values
    - Wealth shares (% of total) for Top 10%, Top 5%, and Bottom 50%
- **Countries**: Germany (DE), France (FR), Slovenia (SI)

### COVID-19 Epidemiological Data

- **Source**: [European Centre for Disease Prevention and Control (ECDC)](https://www.ecdc.europa.eu/en/covid-19/data)
- **Coverage**: Daily case and death counts
- **Aggregation**: Quarterly totals normalized per 100,000 population
- **Variables**: Total cases, deaths, population data (2020)

## 📁 Project Structure

```
covid-19-wealth-distribution/
├── Covid-19 - Wealth Distribution.ipynb  # Main analysis notebook
├── datasets/
│   ├── Distributional Wealth Accounts.csv
│   └── EU Covid-19.csv
├── helpers/                                   # Modular Python code
│   ├── config.py                          # Configuration and constants
│   ├── data_loader.py                     # Data loading utilities
│   ├── modeling.py                        # ML models for prediction
│   ├── visualization.py                   # Plotting functions
│   ├── evaluation.py                      # Model evaluation metrics
│   └── analysis.py                        # Analysis utilities
├── README.md
└── requirements.txt
```

The project has been refactored into modular components:
- **Configuration**: Centralized constants and metric definitions
- **Data Loading**: Reusable data import and preprocessing
- **Modeling**: Machine learning pipeline for wealth prediction
- **Visualization**: Standard plotting utilities
- **Evaluation**: Model performance metrics
- **Analysis**: Correlation and statistical analysis

See [helpers/README.md](helpers/README.md) for detailed module documentation.

## 🔧 Methodology

### 1. Data Preparation

- **Temporal Alignment**: Aggregate daily COVID data to quarterly frequency to match wealth data
- **Normalization**: Calculate per-capita metrics (per 100,000 population) for cross-country comparison
- **Train-Test Split**:
  - Training: 2016-2019 (pre-pandemic baseline)
  - Testing: 2020-2025 (pandemic period)

### 2. Exploratory Analysis

- **Wealth Metrics Visualization**: Time series plots of 5 key indicators per country
- **COVID Timeline Analysis**: Cases and deaths trends across countries
- **Descriptive Statistics**: Distribution summaries and data quality checks

### 3. Predictive Modeling

- **Baseline Approach**: Linear regression using pre-pandemic trends (2016-2019)
- **Enhanced Models**:
  - **Polynomial Regression** (degree 2): Captures non-linear pre-pandemic trends
  - **Ridge Regression**: Regularized model to prevent overfitting
- **Purpose**: Establish counterfactual baseline to quantify pandemic disruption
- **Models**: Separate models for each country-metric-model combination
- **Model Comparison**: Side-by-side performance evaluation to identify best predictive approach
- **Evaluation Metrics**:
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - MAPE (Mean Absolute Percentage Error)
  - R² Score

### 4. Correlation Analysis

- **Pairwise Correlations**: Between COVID severity (cases/deaths) and wealth metrics
- **Visualization**: Heatmaps and color-coded tables
- **Interpretation**: Identify temporal relationships between pandemic waves and wealth changes

### 5. Integrated Visualization

- **Dual-Axis Plots**: Overlay wealth metrics with COVID severity timelines
- **Dashboard**: Comprehensive 5-panel summary of key findings
- **Comparison**: Cross-country patterns and divergent outcomes

## 📈 Key Findings

### Model Performance & Enhanced Predictions

- **Model Comparison Results**: Polynomial and Ridge regression models significantly outperform simple linear baseline
  - **Germany**: Polynomial models reduce average MAPE from 3.7% to 2.9%
  - **France**: Linear models perform well (2.4% MAPE) due to stable pre-pandemic trends
  - **Slovenia**: Polynomial models achieve up to 60% MAPE reduction (10.9% → 4.3%) for certain metrics
- **Best Model by Metric**:
  - Polynomial regression wins 8/15 metrics across countries
  - Linear regression: 6/15 metrics (particularly for France)
  - Ridge regression: 1/15 metrics
- **Key Insight**: Capturing non-linear pre-pandemic trends essential for accurate counterfactual predictions

### Prediction Accuracy & Pandemic Disruption

- **Pre-pandemic linear models**: Underestimated pandemic-era volatility for most metrics
- **Enhanced models improved accuracy**: Polynomial features capture acceleration/deceleration in wealth trends
- **Gini predictions most stable**: Inequality measures showed relatively smaller prediction errors, suggesting structural resilience

### COVID-19 Severity Comparison

- **Germany**: Highest absolute cases but moderate per-capita impact
- **France**: Severe outbreak with high deaths per 100k population
- **Slovenia**: Lower overall impact but concentrated waves

### Wealth Inequality Trends (Gini Coefficient)

- **Germany**: Slight increase in inequality (Gini change: +0.01 to +0.02 from 2020 Q1 to 2025 Q2)
- **France**: Moderate inequality resilience with minor fluctuations
- **Slovenia**: Relatively stable, confirming lower baseline inequality

### Correlation Patterns

- **Weak to moderate correlations** between COVID severity and wealth metrics (|r| < 0.5 in most cases)
- **Gini vs Deaths**: Mixed signals across countries, no consistent pattern
- **Mean Wealth vs Cases**: Slight positive correlations suggest asset price effects
- **Temporal lags**: Immediate COVID impact vs delayed wealth data reporting

### Distributional Analysis: Wealth Inequality Dynamics

#### Top 10% vs Bottom 50% Wealth Evolution

- **Wealth Concentration Ratios (Top 10% to Bottom 50%)**:
  - **Germany**: 26.40x (2019) → 24.20x (2024) — **8.3% decrease** (narrowing gap)
  - **France**: 10.98x (2019) → 11.04x (2024) — **0.6% increase** (slight widening)
  - **Slovenia**: 4.86x (2019) → 4.71x (2024) — **3.2% decrease** (narrowing gap)

- **Key Observation**: Germany shows highest absolute inequality but also largest improvement during pandemic period

#### Wealth Share Distribution Changes (2019 → 2024)

**Bottom 50% Share of Total Wealth:**
- **Germany**: 2.25% → 2.51% (+0.26 percentage points)
- **France**: 4.91% → 4.96% (+0.06 pp)
- **Slovenia**: 10.32% → 10.62% (+0.30 pp)

**Top 10% Share of Total Wealth:**
- **Germany**: 59.40% → 60.50% (+1.10 pp) — wealth concentration increased
- **France**: 53.83% → 54.71% (+0.89 pp) — wealth concentration increased
- **Slovenia**: 50.16% → 50.07% (-0.09 pp) — wealth concentration slightly decreased

**Net Distributional Shift:**
- **Germany**: 1.36 pp toward top concentration
- **France**: 0.95 pp toward top concentration
- **Slovenia**: 0.21 pp away from top concentration

#### Distributional Insights

1. **Paradox of Inequality**: While wealth gaps narrowed in absolute ratio terms (Germany, Slovenia), the *share* of total wealth still shifted toward the top 10% in most countries
2. **Slovenia's Resilience**: Only country where top 10% share actually declined, demonstrating more equitable pandemic response
3. **Bottom 50% Gains**: All countries saw bottom 50% increase their absolute share, but gains were modest (0.06-0.30 pp)
4. **Top 10% Resilience**: Wealthiest households maintained or increased their share despite pandemic, suggesting:
   - Asset price appreciation (stocks, real estate) benefited top wealth holders
   - Policy interventions (low interest rates, fiscal stimulus) supported asset valuations
   - Labor market disruptions affected middle/lower wealth groups more severely

### Research Implications

1. **Pandemic disrupted long-term wealth accumulation trends**: Pre-COVID models inadequate for crisis periods, but polynomial models capture non-linear dynamics better
2. **Wealth inequality showed resilience**: Structural factors outweighed short-term pandemic shocks
3. **Country-specific responses led to divergent outcomes**: Different policy approaches and economic structures matter
4. **Asset price effects dominate**: Financial asset valuations influenced wealth more than labor market disruptions
5. **Model selection matters**: Appropriate baseline model critical for measuring pandemic deviation from expected trends

## 🛠️ Technical Stack

- **Python 3.x**
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib (with seaborn styling)
- **Machine Learning**: scikit-learn
  - Models: LinearRegression, Ridge
  - Preprocessing: PolynomialFeatures, make_pipeline
  - Metrics: mean_absolute_error, mean_squared_error, r2_score
- **Environment**: Jupyter Notebook

## 📁 Project Structure

```plain
covid-19-wealth-distribution/
├── Covid-19 - Wealth Distribution.ipynb  # Main analysis notebook
├── README.md                              # This file
├── requirements.txt                       # Python dependencies
└── datasets/
    ├── Distributional Wealth Accounts.csv # ECB wealth data
    └── EU Covid-19.csv                    # ECDC COVID data
```

## 🚀 Getting Started

### Prerequisites

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

1. Open the Jupyter notebook:

   ```bash
   jupyter notebook "Covid-19 - Wealth Distribution.ipynb"
   ```

2. Execute cells sequentially:
   - **Cells 1-21**: Setup, configuration, and helper functions
   - **Cells 22-28**: Exploratory wealth analysis (2016-2019)
   - **Cells 29-34**: Enhanced predictive modeling with model comparison
   - **Cells 35-42**: COVID data integration and initial predictions
   - **Cells 43-54**: Correlation analysis and dual-axis visualizations
   - **Cells 55-61**: Comprehensive insights dashboard
   - **Cell 62**: Summary of key findings and research implications

## 📊 Notebook Structure

The analysis is organized into clearly defined sections (62 cells total):

1. **Import Libraries and Setup** - Dependencies, warnings configuration, and seaborn styling
2. **Configuration** - Country codes, names, and wealth metric dictionaries
3. **Data Loading** - Import ECB wealth accounts, filter countries, create train/test splits
4. **Helper Functions - Wealth Visualization** - Reusable plotting utilities for time series
5. **Helper Functions - Modeling & Evaluation** - Train/predict functions supporting multiple model types (Linear, Polynomial, Ridge)
6. **Helper Functions - Model Comparison** - Batch training and performance evaluation
7. **Helper Functions - COVID Integration** - Data merge and summary tables
8. **Helper Functions - Dual-Axis COVID-Wealth Plots** - Integrated visualizations
9. **Helper Functions - Correlation Analysis** - Statistical relationship computations
10. **Helper Functions - Dashboard** - Multi-panel comprehensive visualization
11. **Exploratory Analysis** - Pre-pandemic wealth trends by country (2016-2019)
12. **Enhanced Predictive Modeling** - Model comparison across Linear, Polynomial, and Ridge approaches
13. **Model Performance Analysis** - Comparative visualization and best model identification
14. **Baseline Predictions (Legacy)** - Original linear regression analysis by country
15. **COVID Data Processing** - Load, aggregate, and visualize epidemiological data
16. **Data Integration** - Merge COVID and wealth datasets by country
17. **Dual-Axis Visualizations** - COVID severity overlaid with wealth metrics
18. **Correlation Analysis** - Compute and visualize statistical relationships
19. **Comprehensive Insights Dashboard** - 5-panel summary with key findings
20. **Summary & Interpretation** - Research questions answered, evidence links, and caveats

## ⚠️ Limitations & Caveats

- **Correlation ≠ Causation**: Observed associations don't imply causal relationships
- **Timing Misalignment**: Wealth data reported quarterly with potential lags
- **Model Complexity**: While polynomial and ridge models improve accuracy, more sophisticated time series methods (ARIMA, VAR) may capture additional dynamics
- **Country Selection**: Analysis limited to 3 countries; not representative of entire Euro Area
- **Missing Variables**: No controls for fiscal policy, monetary interventions, or sector-specific effects
- **Measurement Issues**: Wealth accounts subject to revision and methodological changes
- **Sample Size**: Limited pre-pandemic training data (16 quarters) for complex models

## 🔮 Future Research Directions

### Data Expansion

- Include household income microdata (EU-SILC) for distributional analysis by quintile
- Add asset price indices (housing, equities) for wealth decomposition
- Integrate policy timeline data (stimulus packages, lockdown stringency)

### Methodological Improvements

- **Time Series Models**: ARIMAX, VAR, Prophet for dynamic relationships and seasonality
- **Machine Learning**: Gradient boosting, random forests, neural networks for complex non-linear patterns
- **Ensemble Methods**: Combine Linear, Polynomial, Ridge, and advanced models for robust predictions
- **Causal Inference**: Difference-in-differences, synthetic control methods, instrumental variables
- **Panel Analysis**: Fixed effects models across multiple countries and time periods
- **Hyperparameter Optimization**: Grid search for optimal polynomial degree and regularization strength

### Inequality Metrics Extension

- Theil index, Palma ratio, 90/10 percentile ratios
- Wealth mobility analysis (transition matrices)
- Decomposition by asset type (financial vs real estate)

### Interactive Dashboards

- Plotly/Dash for interactive exploration
- Streamlit app with country/metric selectors
- Real-time updates with latest data releases

## 📚 References

- European Central Bank. (2025). Distributional Wealth Accounts. <https://data.ecb.europa.eu/>
- European Centre for Disease Prevention and Control. (2025). COVID-19 Data. <https://www.ecdc.europa.eu/en/covid-19/data>
- Piketty, T. (2014). *Capital in the Twenty-First Century*. Harvard University Press.
- OECD. (2021). *Inequalities in Household Wealth and Financial Insecurity of Households*. OECD Report.

## 📝 License

This project is for educational and research purposes.

## 🙏 Acknowledgments

- European Central Bank for distributional wealth accounts data
- European Centre for Disease Prevention and Control for COVID-19 epidemiological data
- Open-source community for Python data science tools
