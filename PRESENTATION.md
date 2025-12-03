# COVID-19 and Wealth Distribution Analysis

## A Data-Driven Investigation of Pandemic Impact on European Economies

---

## 📋 Agenda

1. **Introduction & Research Questions**
2. **Data Sources & Methodology**
3. **Exploratory Analysis**
4. **Predictive Modeling**
5. **COVID-19 Impact Assessment**
6. **Correlation Analysis**
7. **Key Findings**
8. **Limitations & Future Work**

---

## 🎯 Research Questions

### What We're Investigating

1. **How did COVID-19 affect wealth distribution** compared to pre-pandemic trends?

2. **Which demographic segments** experienced the most significant changes?

3. **What correlations exist** between COVID-19 severity and wealth inequality?

4. **How accurate** were pre-pandemic trend predictions for the crisis period?

5. **How do different countries** respond differently to the pandemic shock?

---

## 🌍 Countries Under Analysis

### Selected Euro Area Economies

- **🇩🇪 Germany** - Largest European economy
- **🇫🇷 France** - Major EU member state  
- **🇸🇮 Slovenia** - Representative smaller economy

### Why These Three?

- Different economic structures
- Varying baseline inequality levels
- Diverse pandemic response policies
- Available high-quality data coverage

---

## 📊 Data Sources

### 1. Wealth Distribution Data

#### European Central Bank - Distributional Wealth Accounts

- **Coverage**: Quarterly data (2016-2025)
- **Metrics**:
  - Adjusted total assets
  - Net wealth (mean & median)
  - Gini coefficient (inequality measure)
- **Granularity**: Household-level distributions

### 2. COVID-19 Epidemiological Data

#### European Centre for Disease Prevention and Control (ECDC)

- **Coverage**: Daily case and death counts
- **Period**: 2020-2025
- **Normalization**: Per 100,000 population

---

## 🔧 Methodology Overview

### Phase 1: Data Preparation

- Temporal alignment (daily → quarterly aggregation)
- Train-test split:
  - **Training**: 2016-2019 (pre-pandemic)
  - **Testing**: 2020-2025 (pandemic period)

### Phase 2: Exploratory Analysis

- Time series visualization of 5 key wealth metrics
- Pre-pandemic trend identification
- Descriptive statistics

### Phase 3: Predictive Modeling

- Multiple regression approaches tested
- Counterfactual baseline establishment

---

## 🤖 Predictive Modeling Approach

### Three Model Types Compared

#### 1. **Linear Regression** (Baseline)

- Simple trend extrapolation
- Interpretable but limited
- Assumes linear growth

#### 2. **Polynomial Regression** (Degree 2)

- Captures curvature in trends
- Better fits for accelerating/decelerating patterns
- More flexible than linear

#### 3. **Ridge Regression** (Regularized)

- Prevents overfitting
- Useful with limited training data
- Balances complexity and generalization

---

## 📈 Model Performance Results

### Best Model by Country

**Germany:**

- Polynomial models: 2.9% average MAPE
- Linear baseline: 3.7% average MAPE
- **Improvement**: 22% error reduction

**France:**

- Linear models: 2.4% average MAPE
- Stable pre-pandemic trends
- Simple models sufficient

**Slovenia:**

- Polynomial models: 4.3% average MAPE
- Linear baseline: 10.9% average MAPE
- **Improvement**: 60% error reduction!

---

## 📊 Key Metrics Analyzed

### 5 Wealth Distribution Indicators

1. **Total Assets** - Aggregate household wealth
2. **Net Wealth** - Assets minus liabilities
3. **Median Wealth** - Middle household value
4. **Mean Wealth** - Average household value
5. **Gini Coefficient** - Inequality measure (0-1 scale)

### Why These Metrics?

- Capture different aspects of distribution
- Median vs. Mean shows inequality
- Gini provides standard inequality measure
- Comparable across countries and time

---

## 🦠 COVID-19 Severity Comparison

### Total Impact (2020-2025)

| Country | Total Cases | Total Deaths | Deaths per 100k |
|---------|-------------|--------------|-----------------|
| Germany | ~38M cases  | ~180K deaths | Moderate impact |
| France  | ~35M cases  | ~165K deaths | High impact     |
| Slovenia| ~1.3M cases | ~7K deaths   | Concentrated    |

### Key Observations

- Germany: Highest absolute numbers, moderate per-capita
- France: Severe outbreak with high mortality
- Slovenia: Lower totals but concentrated waves

---

## 📉 Wealth Inequality Trends

### Gini Coefficient Changes (2020 Q1 → 2025 Q2)

**Germany:**

- 2020 Q1: 0.71
- 2025 Q2: 0.73
- **Change**: +0.02 (slight increase)

**France:**

- Relatively stable
- Minor fluctuations
- Resilient inequality structure

**Slovenia:**

- Lower baseline inequality
- Maintained stability
- Structural resilience

---

## 🔗 Correlation Analysis

### COVID-19 Severity vs. Wealth Metrics

**Overall Findings:**

- **Weak to moderate** correlations (|r| < 0.5)
- No consistent cross-country patterns
- Temporal lags complicate relationships

**Specific Observations:**

- **Gini vs. Deaths**: Mixed signals, country-dependent
- **Mean Wealth vs. Cases**: Slight positive correlations
- **Median Wealth vs. Deaths**: Varied responses

### Interpretation

Asset price effects > Labor market disruptions

---

## 💡 Key Finding #1: Model Selection Matters

### Prediction Accuracy

- Pre-pandemic **linear models underestimated** volatility
- **Polynomial models** captured non-linear trends better
- **Best model varies** by country and metric

### Practical Implications

✅ **Use polynomial models** for Germany & Slovenia  
✅ **Linear sufficient** for stable France trends  
✅ **Model comparison** essential for accuracy  
⚠️ **Simple extrapolation fails** during crises

---

## 💡 Key Finding #2: Wealth Inequality Resilience

### Surprising Discovery

Despite massive economic disruption:

- Gini coefficients **remained relatively stable**
- Structural factors **outweighed** short-term shocks
- Inequality **increased slightly** in some countries

### Why?

1. **Asset price effects** (stocks, real estate appreciated)
2. **Policy interventions** (wage subsidies, transfers)
3. **Wealth concentration** at the top cushioned volatility
4. **Delayed reporting** may mask immediate impacts

---

## 💡 Key Finding #3: Country-Specific Responses

### Divergent Outcomes

**Germany:**

- Moderate prediction errors
- Slight inequality increase
- Economic structure buffered shocks

**France:**

- Most predictable patterns
- Stable inequality
- Strong policy response

**Slovenia:**

- Highest prediction errors initially
- Maintained lower baseline inequality
- Smaller economy = higher volatility

---

## 💡 Key Finding #4: Pandemic Disrupted Trends

### Pre-COVID Models Failed

- **15-25% average MAPE** across countries
- Significant deviations from expected trajectories
- Crisis periods require different modeling

### What This Means

❌ Long-term trend extrapolation inadequate  
✅ Need dynamic, adaptive models  
✅ Non-linear patterns emerge during shocks  
✅ Historical baselines informative but insufficient

---

## 🎨 Visualization Highlights

### Our Analysis Includes

1. **Time Series Plots** - Pre-pandemic trends by country
2. **Prediction Comparisons** - Actual vs. forecasted values
3. **Model Performance Charts** - MAPE comparison across models
4. **Correlation Heatmaps** - COVID severity vs. wealth metrics
5. **Dual-Axis Overlays** - Pandemic waves with wealth changes
6. **Integrated Dashboard** - 5-panel comprehensive summary

### Design Principles

- Clear, professional styling
- Color-coded by country
- Quantitative labels
- Matplotlib-based for reproducibility

---

## ⚠️ Limitations & Caveats

### Data Limitations

1. **Correlation ≠ Causation** - Associations, not causal claims
2. **Timing Misalignment** - Quarterly reporting with lags
3. **Country Sample** - Only 3 countries (not representative of all EU)
4. **Missing Variables** - No fiscal policy, monetary intervention controls

### Methodological Limitations

1. **Model Complexity** - More sophisticated methods possible (ARIMA, VAR)
2. **Sample Size** - Only 16 quarters pre-pandemic training data
3. **Measurement Issues** - Wealth accounts subject to revision

---

## 🔮 Future Research Directions

### Data Expansion

- **More countries** - Full Euro Area coverage
- **Income data** - EU-SILC household microdata
- **Asset decomposition** - Housing vs. financial wealth
- **Policy timeline** - Stimulus packages, lockdown stringency

### Methodological Improvements

- **Time series models** - ARIMAX, VAR, Prophet
- **Machine learning** - Gradient boosting, neural networks
- **Causal inference** - DiD, synthetic controls, IV methods
- **Panel analysis** - Fixed effects across countries

### Metric Extensions

- **Theil index**, Palma ratio, 90/10 percentiles
- **Wealth mobility** - Transition matrices
- **Interactive dashboards** - Plotly/Dash, Streamlit

---

## 🛠️ Technical Stack

### Tools & Libraries

**Python 3.x** - Core environment  
**pandas** - Data manipulation  
**numpy** - Numerical operations  
**matplotlib** - Visualization  

**scikit-learn:**

- LinearRegression - Baseline models
- PolynomialFeatures - Non-linear patterns
- Ridge - Regularization
- Metrics - MAE, RMSE, MAPE, R²

**Jupyter Notebook** - Interactive analysis

---

## 📁 Project Structure

```plain
covid-19-wealth-distribution/
├── Covid-19 - Wealth Distribution.ipynb  # Main analysis
├── README.md                              # Documentation
├── PRESENTATION.md                        # This file
├── requirements.txt                       # Dependencies
└── datasets/
    ├── Distributional Wealth Accounts.csv # ECB data
    └── EU Covid-19.csv                    # ECDC data
```

### Repository Features

- Clean, documented code
- Comprehensive README
- Reproducible analysis
- Professional visualizations

---

## 🚀 How to Run the Analysis

### Prerequisites

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Execute Analysis

```bash
# Launch Jupyter
jupyter notebook "Covid-19 - Wealth Distribution.ipynb"

# Run cells sequentially (1-57):
# - Cells 1-21: Setup & helper functions
# - Cells 22-28: Exploratory analysis
# - Cells 29-34: Enhanced modeling
# - Cells 35-44: Baseline & evaluation
# - Cells 45-54: COVID integration
# - Cells 55-56: Dashboard & summary
```

---

## 🎯 Research Implications

### Academic Contributions

1. **Methodology** - Multi-model comparison for crisis prediction
2. **Evidence** - Quantified pandemic impact on wealth inequality
3. **Cross-country** - Comparative analysis of policy responses
4. **Temporal** - Short to medium-term inequality dynamics

### Policy Implications

1. **Monitoring** - Real-time wealth tracking during crises
2. **Intervention** - Targeted policies for vulnerable segments
3. **Forecasting** - Improved crisis impact predictions
4. **Evaluation** - Assess effectiveness of fiscal responses

---

## 📊 Summary Statistics

### Analysis Scope

- **3 Countries** analyzed in depth
- **10 Years** of data (2016-2025)
- **5 Wealth Metrics** tracked
- **3 Model Types** compared
- **40 Quarters** of observations
- **15 Metric-Country** combinations evaluated

### Computational Effort

- **57 Code Cells** in main notebook
- **15 Visualizations** generated
- **~500 Lines** of Python code
- **Fully Reproducible** analysis pipeline

---

## 🎓 Key Takeaways

### For Researchers

1. ✅ Non-linear models essential for crisis periods
2. ✅ Model comparison improves accuracy 20-60%
3. ✅ Wealth inequality more resilient than expected
4. ✅ Country context matters significantly

### For Policymakers

1. ✅ Asset prices drive wealth more than labor markets
2. ✅ Monitor real-time distributional impacts
3. ✅ Targeted interventions may be necessary
4. ✅ Structural inequality persists through shocks

### For Data Scientists

1. ✅ Always compare multiple model types
2. ✅ Domain knowledge crucial for interpretation
3. ✅ Visualizations essential for communication
4. ✅ Simple models can fail during regime changes

---

## 📚 References

### Data Sources

1. **European Central Bank** (2025). *Distributional Wealth Accounts*. <https://data.ecb.europa.eu/>

2. **European Centre for Disease Prevention and Control** (2025). *COVID-19 Data*. <https://www.ecdc.europa.eu/en/covid-19/data>

### Academic Literature

3. **Piketty, T.** (2014). *Capital in the Twenty-First Century*. Harvard University Press.

4. **OECD** (2021). *Inequalities in Household Wealth and Financial Insecurity*. OECD Report.

---

## 🙏 Acknowledgments

### Data Providers

- **European Central Bank** - Distributional wealth accounts
- **European Centre for Disease Prevention and Control** - COVID-19 epidemiological data

### Tools & Community

- **Python Software Foundation** - Core language
- **NumFOCUS** - pandas, numpy, matplotlib
- **scikit-learn developers** - Machine learning tools
- **Open source community** - Countless contributions

---

## 📧 Contact & Collaboration

### Project Information

- **Repository**: github.com/clement-antoine-xavier/covid-19-wealth-distribution
- **License**: Educational and research purposes
- **Status**: Active analysis (December 2025)

### Future Collaboration

- Open to feedback and suggestions
- Interested in extending analysis
- Seeking additional data sources
- Welcome methodological improvements

---

## 🎬 Thank You

### Questions & Discussion

**What we learned:**

- COVID-19 disrupted but didn't destroy wealth distribution patterns
- Model selection critically impacts prediction accuracy
- Country-specific factors drive divergent outcomes
- Asset effects dominate labor market impacts

**What's next:**

- Expand country coverage
- Incorporate policy variables
- Apply advanced time series methods
- Build interactive dashboards

---

## 📖 Appendix: Methodology Details

### Train-Test Split

**Training Period (2016-2019):**

- 16 quarters of pre-pandemic data
- Establish baseline trends
- Train all model types

**Testing Period (2020-2025):**

- 22 quarters of pandemic data
- Evaluate predictions
- Quantify disruption

### Error Metrics Explained

**MAE** - Mean Absolute Error (absolute magnitude)  
**RMSE** - Root Mean Squared Error (penalizes large errors)  
**MAPE** - Mean Absolute Percentage Error (relative %)  
**R²** - Proportion of variance explained (0-1)

---

## 📖 Appendix: Wealth Metrics Details

### Gini Coefficient

- **Range**: 0 (perfect equality) to 1 (perfect inequality)
- **Interpretation**:
  - < 0.3: Relatively equal
  - 0.3-0.4: Moderate inequality
  - > 0.4: High inequality
- **Our data**: 0.70-0.75 (high wealth inequality typical for Euro Area)

### Median vs. Mean Wealth

- **Median**: Middle household (50th percentile)
- **Mean**: Average across all households
- **Gap**: Mean >> Median indicates concentration at top
- **Trend**: Growing gap = increasing inequality

---

## End of Presentation

*For detailed analysis, please refer to:*

- **Main Notebook**: `Covid-19 - Wealth Distribution.ipynb`
- **Documentation**: `README.md`
- **Repository**: Full code and data available

