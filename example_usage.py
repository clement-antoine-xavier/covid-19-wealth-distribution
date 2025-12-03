#!/usr/bin/env python3
"""
Example usage of the refactored COVID-19 Wealth Distribution analysis modules.

This script demonstrates how to use the modular components independently
outside of the Jupyter notebook environment.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Import custom modules
from helpers.config import WEALTH_METRICS, COUNTRY_NAMES, DF_PATH, COVID_PATH
from helpers.data_loader import load_wealth_data, filter_wealth_data, split_train_test
from helpers.data_loader import load_covid_data, aggregate_covid_quarterly
from helpers.modeling import train_predict_country, compare_models
from helpers.visualization import plot_country_wealth_panels, plot_prediction_vs_actual
from helpers.evaluation import calculate_metrics, compare_model_performance
from helpers.analysis import (merge_wealth_covid, calculate_correlations, 
                          plot_wealth_distribution_comparison, 
                          calculate_wealth_concentration_ratios)


def main():
    """Main analysis workflow."""
    
    # 1. Load and prepare data
    print("Loading wealth data...")
    df = load_wealth_data()
    df = filter_wealth_data(df, start_date='2016-01-01', end_date='2025-12-31')
    train_df, test_df = split_train_test(df, split_date='2020-01-01')
    
    print(f"Dataset: {df.shape[0]} quarters, {df.shape[1]} columns")
    print(f"Training: {len(train_df)} quarters (2016-2019)")
    print(f"Testing: {len(test_df)} quarters (2020-2025)")
    
    # 2. Exploratory visualization
    print("\nGenerating wealth distribution panels for Germany...")
    plot_country_wealth_panels(train_df, 'DE')
    
    # 3. Train predictive models
    print("\nTraining predictive models for Germany...")
    predictions = train_predict_country(train_df, test_df, 'DE', model_type='linear')
    
    # 4. Evaluate model performance
    print("\nCalculating model metrics...")
    metrics = calculate_metrics(test_df, predictions, 'DE')
    print(metrics)
    
    # 5. Compare multiple models
    print("\nComparing Linear, Polynomial, and Ridge models...")
    models = compare_models(train_df, test_df, 'DE')
    comparison = compare_model_performance(train_df, test_df, 'DE', models)
    print(comparison)
    
    # 6. Load and merge COVID-19 data
    print("\nLoading COVID-19 data...")
    df_covid = load_covid_data()
    covid_countries = ['Germany', 'France', 'Slovenia']
    covid_quarterly = aggregate_covid_quarterly(df_covid, covid_countries)
    
    merged = merge_wealth_covid(df, covid_quarterly, 'DE', 'Germany')
    print(f"Merged dataset: {merged.shape}")
    
    # 7. Calculate correlations
    print("\nCalculating wealth-COVID correlations...")
    correlations = calculate_correlations(merged)
    for key, value in correlations.items():
        print(f"{key}: {value:.3f}")
    
    # 8. Distributional analysis
    print("\nCalculating wealth concentration ratios...")
    ratios = calculate_wealth_concentration_ratios(df)
    
    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
