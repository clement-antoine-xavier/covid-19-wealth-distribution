"""Configuration module for COVID-19 Wealth Distribution analysis."""

# File paths
DF_PATH = "datasets/Distributional Wealth Accounts.csv"
COVID_PATH = "datasets/EU Covid-19.csv"

# Country mapping
COUNTRY_NAMES = {"DE": "Germany", "FR": "France", "SI": "Slovenia"}

# Dictionary mapping country codes to their wealth metric column names in the dataset
# Each country has aggregate metrics plus distributional breakdowns by decile
WEALTH_METRICS = {
    "DE": {  # Germany
        # Aggregate metrics
        "median_wealth": "Net wealth of households, median (DWA.Q.DE.S14.N.LE.NWA._Z.EUR_MD.S.N)",
        "net_wealth": "Adjusted wealth (net) of households (DWA.Q.DE.S14.N.LE.NWA._Z.EUR.S.N)",
        "gini": "Gini coefficient of households (DWA.Q.DE.S14._Z._Z.NWA._Z.GI.S.N)",
        # Distributional breakdowns - Wealth by percentile groups
        "net_wealth_top10": "Adjusted wealth (net) of households - Decile 10 based on net wealth concept (DWA.Q.DE.S14.N.LE.NWA.D10.EUR.S.N)",
        "net_wealth_bottom50": "Adjusted wealth (net) of households - Bottom 50% based on net wealth concept (DWA.Q.DE.S14.N.LE.NWA.B50.EUR.S.N)",
        # Wealth shares - Percentage of total wealth held by each group
        "share_bottom50": "Net wealth of households, share of bottom 50% (DWA.Q.DE.S14._Z._Z.NWA.B50.PT.S.N)",
        "share_top10": "Net wealth of households, share of top 10% (DWA.Q.DE.S14._Z._Z.NWA.T10.PT.S.N)",
        "share_top5": "Net wealth of households, share of top 5% (DWA.Q.DE.S14._Z._Z.NWA.T5.PT.S.N)",
    },
    "FR": {  # France
        # Aggregate metrics
        "median_wealth": "Net wealth of households, median (DWA.Q.FR.S14.N.LE.NWA._Z.EUR_MD.S.N)",
        "net_wealth": "Adjusted wealth (net) of households (DWA.Q.FR.S14.N.LE.NWA._Z.EUR.S.N)",
        "gini": "Gini coefficient of households (DWA.Q.FR.S14._Z._Z.NWA._Z.GI.S.N)",
        # Distributional breakdowns
        "net_wealth_top10": "Adjusted wealth (net) of households - Decile 10 based on net wealth concept (DWA.Q.FR.S14.N.LE.NWA.D10.EUR.S.N)",
        "net_wealth_bottom50": "Adjusted wealth (net) of households - Bottom 50% based on net wealth concept (DWA.Q.FR.S14.N.LE.NWA.B50.EUR.S.N)",
        # Wealth shares
        "share_bottom50": "Net wealth of households, share of bottom 50% (DWA.Q.FR.S14._Z._Z.NWA.B50.PT.S.N)",
        "share_top10": "Net wealth of households, share of top 10% (DWA.Q.FR.S14._Z._Z.NWA.T10.PT.S.N)",
        "share_top5": "Net wealth of households, share of top 5% (DWA.Q.FR.S14._Z._Z.NWA.T5.PT.S.N)",
    },
    "SI": {  # Slovenia
        # Aggregate metrics
        "median_wealth": "Net wealth of households, median (DWA.Q.SI.S14.N.LE.NWA._Z.EUR_MD.S.N)",
        "net_wealth": "Adjusted wealth (net) of households (DWA.Q.SI.S14.N.LE.NWA._Z.EUR.S.N)",
        "gini": "Gini coefficient of households (DWA.Q.SI.S14._Z._Z.NWA._Z.GI.S.N)",
        # Distributional breakdowns
        "net_wealth_top10": "Adjusted wealth (net) of households - Decile 10 based on net wealth concept (DWA.Q.SI.S14.N.LE.NWA.D10.EUR.S.N)",
        "net_wealth_bottom50": "Adjusted wealth (net) of households - Bottom 50% based on net wealth concept (DWA.Q.SI.S14.N.LE.NWA.B50.EUR.S.N)",
        # Wealth shares
        "share_bottom50": "Net wealth of households, share of bottom 50% (DWA.Q.SI.S14._Z._Z.NWA.B50.PT.S.N)",
        "share_top10": "Net wealth of households, share of top 10% (DWA.Q.SI.S14._Z._Z.NWA.T10.PT.S.N)",
        "share_top5": "Net wealth of households, share of top 5% (DWA.Q.SI.S14._Z._Z.NWA.T5.PT.S.N)",
    },
}
