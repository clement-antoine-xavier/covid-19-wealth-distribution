"""Model evaluation and metrics calculation."""

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from .config import WEALTH_METRICS, COUNTRY_NAMES


def calculate_metrics(test_df, predictions, country_code):
    """
    Calculate comprehensive error metrics for model predictions.

    Computes MAE, RMSE, and R² for each wealth metric to assess prediction quality.
    Lower MAE/RMSE and higher R² indicate better model performance.

    Parameters:
    -----------
    test_df : DataFrame
        Test data containing actual values
    predictions : dict
        Dictionary of predictions from train_predict_country()
    country_code : str
        Country code ('DE', 'FR', or 'SI')

    Returns:
    --------
    DataFrame
        Metrics table with columns: Metric, MAE, RMSE, R²
    """
    metrics = WEALTH_METRICS[country_code]
    results = []

    for key, col in metrics.items():
        if key not in predictions:
            continue

        # Get actual and predicted values (remove NaN)
        actual = test_df[col].dropna()
        pred = predictions[key][: len(actual)]

        if len(actual) == 0:
            continue

        # Calculate error metrics
        mae = mean_absolute_error(actual, pred)
        rmse = np.sqrt(mean_squared_error(actual, pred))
        r2 = r2_score(actual, pred)

        results.append({"Metric": key, "MAE": mae, "RMSE": rmse, "R²": r2})

    return pd.DataFrame(results)


def compare_model_performance(train_df, test_df, country_code, models_dict):
    """
    Compare performance of multiple models across all metrics.

    Parameters:
    -----------
    train_df : DataFrame
        Training data
    test_df : DataFrame
        Test data
    country_code : str
        Country code ('DE', 'FR', or 'SI')
    models_dict : dict
        Dictionary with model names as keys and prediction dictionaries as values

    Returns:
    --------
    DataFrame
        Combined metrics for all models
    """
    all_metrics = []

    for model_name, predictions in models_dict.items():
        metrics_df = calculate_metrics(test_df, predictions, country_code)
        metrics_df["Model"] = model_name
        all_metrics.append(metrics_df)

    combined = pd.concat(all_metrics, ignore_index=True)
    return combined


def find_best_model_per_metric(comparison_df):
    """
    Identify the best performing model for each wealth metric.

    Best model is determined by lowest MAE (Mean Absolute Error).

    Parameters:
    -----------
    comparison_df : DataFrame
        Output from compare_model_performance()

    Returns:
    --------
    DataFrame
        Best model for each metric with its performance stats
    """
    # Group by metric and find model with minimum MAE
    best = comparison_df.loc[comparison_df.groupby("Metric")["MAE"].idxmin()]
    return best.reset_index(drop=True)
