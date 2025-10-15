# COVID-19 Global Spread

## Research Questions

1. How have COVID-19 infection and mortality rates varied globally over time?
2. What demographic factors (e.g., age distribution, population density) correlate with higher infection and mortality rates?
3. How effective have different countries' public health interventions been in controlling the spread of COVID-19?
4. What is the relationship between vaccination rates and COVID-19 case trends?
5. How do healthcare infrastructure and resource availability impact COVID-19 outcomes in different regions?

## Data Sources

| Category | Sources | Key Metrics | Access Links |
|----------|---------|-------------|--------------|
| COVID-19 Data | World Health Organization (WHO) | Infection rates, mortality rates | [WHO COVID-19 Dashboard](https://covid19.who.int/) |
| Demographic Data | World Bank | Population, age distribution, urbanization rates | [World Bank Data](https://data.worldbank.org/) |

## Datasets

The `datasets/` folder (included with this repository) contains several CSV files used for the analysis. Below is a quick reference describing each file, its likely purpose, and the key columns you can expect. These descriptions were inferred from the filenames — inspect the CSVs for exact column names and data types.

| Filename | Purpose | Likely key columns / notes |
|---|---:|---|
| `COV_VAC_POLICY_2024.csv` | COVID-19 vaccine policy indicators (2024 snapshot or time series) | Country, Date, PolicyMeasure, PolicyValue, Notes — may follow OWID/WHO policy coding conventions |
| `COV_VAC_PROD.csv` | Vaccine production data | Country, Date, Manufacturer, DosesProduced, Batch/Facility |
| `COV_VAC_UPTAKE_2021_2023.csv` | Vaccine uptake / coverage (2021–2023) | Country, Date, AgeGroup, DosesAdministered, PeopleFullyVaccinated, CoveragePercent |
| `COV_VAC_UPTAKE_2024.csv` | Vaccine uptake / coverage (2024) | Country, Date, AgeGroup, DosesAdministered, PeopleFullyVaccinated, CoveragePercent |
| `WHO-COVID-19-global-daily-data.csv` | WHO global daily COVID-19 indicators | Country, Date, NewCases, NewDeaths, CumulativeCases, CumulativeDeaths, TestsPerformed |
| `WHO-COVID-19-global-data.csv` | Aggregated WHO COVID-19 data (cumulative / summary) | Country, Date, Cases, Deaths, Population, Region |
| `WHO-COVID-19-global-hosp-icu-data.csv` | Hospitalization / ICU metrics | Country, Date, HospitalAdmissions, ICUAdmissions, HospitalBedsOccupied |
| `WHO-COVID-19-global-monthly-death-by-age-data.csv` | Monthly deaths broken down by age groups | Country, Month, AgeGroup, Deaths |
| `WHO-COVID-19-global-table-data.csv` | Supplemental WHO table data (various indicators) | Country, IndicatorName, Value, Date — verify specific schema |
