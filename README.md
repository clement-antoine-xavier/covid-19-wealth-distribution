# COVID-19 and Wealth Distribution Analysis

A comprehensive econometric analysis examining the impact of the COVID-19 pandemic on wealth distribution in the Euro Area, with a focus on Germany, France, and Slovenia.

## 🎯 Overview

This project combines distributional wealth accounts data from the European Central Bank with COVID-19 epidemiological data to analyze how the pandemic disrupted wealth accumulation trends and exacerbated inequality across different European economies.

## 🔬 Research Questions

1. **Pandemic Impact**: How has COVID-19 affected wealth distribution in Euro Area countries compared to pre-pandemic trends?
2. **Demographic Effects**: Which wealth segments (by percentile) experienced the most significant changes during the pandemic?
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
- **Countries**: Germany (DE), France (FR), Slovenia (LT)

### COVID-19 Epidemiological Data

- **Source**: [European Centre for Disease Prevention and Control (ECDC)](https://www.ecdc.europa.eu/en/covid-19/data)
- **Coverage**: Daily case and death counts
- **Aggregation**: Quarterly totals normalized per 100,000 population
- **Variables**: Total cases, deaths, population data (2020)

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

- **Approach**: Linear regression using pre-pandemic trends (2016-2019)
- **Purpose**: Establish counterfactual baseline to quantify pandemic disruption
- **Models**: Separate models for each country-metric combination
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

### Prediction Accuracy & Pandemic Disruption

- **Pre-pandemic models failed**: Linear extrapolations from 2016-2019 significantly underestimated pandemic-era volatility
- **Average MAPE**: 15-25% across countries, indicating substantial deviations from expected trends
- **Gini predictions most stable**: Inequality measures showed relatively smaller prediction errors, suggesting structural resilience

### COVID-19 Severity Comparison

- **Germany**: Highest absolute cases but moderate per-capita impact
- **France**: Severe outbreak with high deaths per 100k population
- **Slovenia**: Lower overall impact but concentrated waves

### Wealth Inequality Trends (Gini Coefficient)

- **Germany**: Slight increase in inequality (Gini change: +0.01 to +0.02)
- **France**: Moderate inequality resilience with minor fluctuations
- **Slovenia**: Relatively stable, confirming lower baseline inequality

### Correlation Patterns

- **Weak to moderate correlations** between COVID severity and wealth metrics (|r| < 0.5 in most cases)
- **Gini vs Deaths**: Mixed signals across countries, no consistent pattern
- **Mean Wealth vs Cases**: Slight positive correlations suggest asset price effects
- **Temporal lags**: Immediate COVID impact vs delayed wealth data reporting

### Research Implications

1. **Pandemic disrupted long-term wealth accumulation trends**: Pre-COVID linear models inadequate for crisis periods
2. **Wealth inequality showed resilience**: Structural factors outweighed short-term pandemic shocks
3. **Country-specific responses led to divergent outcomes**: Different policy approaches and economic structures matter
4. **Asset price effects dominate**: Financial asset valuations influenced wealth more than labor market disruptions

## 🛠️ Technical Stack

- **Python 3.x**
- **Data Analysis**: pandas, numpy
- **Visualization**: matplotlib (with seaborn styling)
- **Machine Learning**: scikit-learn (LinearRegression, metrics)
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
   - **Cells 1-10**: Setup, configuration, and helper functions
   - **Cells 11-18**: Exploratory wealth analysis (2016-2019)
   - **Cells 19-27**: Predictive modeling and error analysis
   - **Cells 28-38**: COVID data integration
   - **Cells 39-48**: Correlation analysis and visualizations
   - **Cells 49-55**: Comprehensive insights dashboard

## 📊 Notebook Structure

The analysis is organized into clearly defined sections:

1. **Import Libraries and Setup** - Dependencies and global configurations
2. **Configuration** - Country and metric dictionaries
3. **Data Loading** - Import and filter datasets
4. **Helper Functions** - Reusable visualization and modeling utilities
5. **Exploratory Analysis** - Pre-pandemic wealth trends by country
6. **Predictive Modeling** - Linear regression baseline models
7. **Prediction Evaluation** - Compare actual vs predicted (2020-2025)
8. **COVID Data Processing** - Load and aggregate epidemiological data
9. **Integration** - Merge COVID and wealth datasets
10. **Correlation Analysis** - Statistical relationships
11. **Insights Dashboard** - Comprehensive 5-panel visualization
12. **Summary & Future Work** - Key findings and research directions

## ⚠️ Limitations & Caveats

- **Correlation ≠ Causation**: Observed associations don't imply causal relationships
- **Timing Misalignment**: Wealth data reported quarterly with potential lags
- **Simple Models**: Linear regression provides baseline; non-linear methods may improve accuracy
- **Country Selection**: Analysis limited to 3 countries; not representative of entire Euro Area
- **Missing Variables**: No controls for fiscal policy, monetary interventions, or sector-specific effects
- **Measurement Issues**: Wealth accounts subject to revision and methodological changes

## 🔮 Future Research Directions

### Data Expansion

- Include household income microdata (EU-SILC) for distributional analysis by quintile
- Add asset price indices (housing, equities) for wealth decomposition
- Integrate policy timeline data (stimulus packages, lockdown stringency)

### Methodological Improvements

- **Time Series Models**: ARIMAX, VAR for dynamic relationships
- **Machine Learning**: Gradient boosting, random forests for non-linear patterns
- **Causal Inference**: Difference-in-differences, synthetic control methods
- **Panel Analysis**: Fixed effects models across multiple countries

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
