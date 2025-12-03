"""Data loading and preprocessing utilities."""

import pandas as pd
from .config import DF_PATH, COVID_PATH, WEALTH_METRICS


def load_wealth_data(path=DF_PATH):
    """
    Load wealth distribution dataset and parse dates.

    Parameters:
    -----------
    path : str
        Path to wealth distribution CSV file

    Returns:
    --------
    DataFrame
        Wealth data with parsed DATE column
    """
    df = pd.read_csv(path)
    df["DATE"] = pd.to_datetime(df["DATE"])
    return df


def filter_wealth_data(df, start_date="2016-01-01", end_date="2025-12-31"):
    """
    Filter wealth data by date range and add time features.

    Parameters:
    -----------
    df : DataFrame
        Raw wealth data
    start_date : str
        Start date for filtering (YYYY-MM-DD)
    end_date : str
        End date for filtering (YYYY-MM-DD)

    Returns:
    --------
    DataFrame
        Filtered data with 'days_since_start' feature for modeling
    """
    df_filtered = df[(df["DATE"] >= start_date) & (df["DATE"] <= end_date)].copy()
    df_filtered["days_since_start"] = (
        df_filtered["DATE"] - df_filtered["DATE"].min()
    ).dt.days
    return df_filtered


def split_train_test(df, split_date="2020-01-01"):
    """
    Split data into training (pre-COVID) and test (COVID period) sets.

    Parameters:
    -----------
    df : DataFrame
        Full dataset with DATE column
    split_date : str
        Date to split train/test (default: start of 2020)

    Returns:
    --------
    tuple
        (train_df, test_df) DataFrames
    """
    train = df[df["DATE"] < split_date].copy()
    test = df[df["DATE"] >= split_date].copy()
    return train, test


def load_covid_data(path=COVID_PATH):
    """
    Load COVID-19 dataset and parse dates.

    Parameters:
    -----------
    path : str
        Path to COVID-19 CSV file

    Returns:
    --------
    DataFrame
        COVID-19 data with parsed date column
    """
    df_c = pd.read_csv(path)
    # Parse date from European format (DD/MM/YYYY)
    df_c["date"] = pd.to_datetime(df_c["dateRep"], format="%d/%m/%Y")
    return df_c


def aggregate_covid_quarterly(df_c, countries):
    """
    Aggregate daily COVID-19 data to quarterly totals for specific countries.

    This matches the quarterly frequency of wealth distribution data for proper merging.

    Parameters:
    -----------
    df_c : DataFrame
        Raw COVID-19 data with daily records
    countries : list
        List of country names to include

    Returns:
    --------
    DataFrame
        Quarterly aggregated data with cases/deaths per 100k population
    """
    # Filter for countries of interest
    filtered = df_c[df_c["countriesAndTerritories"].isin(countries)].copy()
    filtered = filtered.sort_values("date")

    # Extract year and quarter from date
    filtered["year"] = filtered["date"].dt.year
    filtered["quarter"] = filtered["date"].dt.quarter

    # Aggregate to quarterly level: sum cases and deaths, keep population
    quarterly = (
        filtered.groupby(["countriesAndTerritories", "year", "quarter"])
        .agg(
            {
                "cases": "sum",  # Total cases in the quarter
                "deaths": "sum",  # Total deaths in the quarter
                "popData2020": "first",  # Population (constant)
            }
        )
        .reset_index()
    )

    # Normalize by population to enable cross-country comparisons
    quarterly["cases_per_100k"] = (
        quarterly["cases"] / quarterly["popData2020"]
    ) * 100000
    quarterly["deaths_per_100k"] = (
        quarterly["deaths"] / quarterly["popData2020"]
    ) * 100000

    # Create DATE column matching wealth data format (end of quarter)
    quarterly["DATE"] = pd.to_datetime(
        quarterly["year"].astype(str)
        + "-"
        + (quarterly["quarter"] * 3).astype(str)
        + "-01"
    ) + pd.offsets.MonthEnd(0)

    return quarterly
