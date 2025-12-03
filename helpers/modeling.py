"""Machine learning models for wealth prediction."""

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from .config import WEALTH_METRICS


def train_predict_country(train_df, test_df, country_code, model_type="linear"):
    """
    Train regression models for all wealth metrics of a country and generate predictions.

    Supports multiple model types for comparison:
    - Linear: Simple trend extrapolation (baseline)
    - Polynomial: Captures non-linear patterns (degree 2)
    - Ridge: Regularized polynomial to prevent overfitting

    Parameters:
    -----------
    train_df : DataFrame
        Training data with 'days_since_start' column
    test_df : DataFrame
        Test data with 'days_since_start' column
    country_code : str
        Country code ('DE', 'FR', or 'SI')
    model_type : str, default='linear'
        Type of model: 'linear', 'polynomial', or 'ridge'

    Returns:
    --------
    dict
        Dictionary with metric keys and predicted values arrays
    """
    metrics = WEALTH_METRICS[country_code]
    results = {}

    # Train a separate model for each wealth metric
    for key, col in metrics.items():
        # Remove rows with missing values
        clean = train_df[["days_since_start", col]].dropna()
        if len(clean) < 3:  # Need at least 3 points for polynomial
            continue

        X_train = clean[["days_since_start"]]
        y_train = clean[col]
        X_test = test_df[["days_since_start"]]

        # Select and train model based on type
        if model_type == "linear":
            # Simple linear regression: y = a*x + b
            model = LinearRegression()
            model.fit(X_train, y_train)
        elif model_type == "polynomial":
            # Polynomial regression (degree 2): y = a*x^2 + b*x + c
            model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
            model.fit(X_train, y_train)
        elif model_type == "ridge":
            # Ridge regression with polynomial features (regularized)
            model = make_pipeline(PolynomialFeatures(degree=2), Ridge(alpha=1.0))
            model.fit(X_train, y_train)
        else:
            raise ValueError(f"Unknown model_type: {model_type}")

        # Generate predictions for the test period
        preds = model.predict(X_test)
        results[key] = preds

    return results


def compare_models(train_df, test_df, country_code):
    """
    Compare multiple prediction models for a country and visualize results.

    Trains and evaluates Linear, Polynomial, and Ridge models to identify
    which approach best captures pre-pandemic trends.

    Parameters:
    -----------
    train_df : DataFrame
        Training data with 'days_since_start' column
    test_df : DataFrame
        Test data with 'days_since_start' column
    country_code : str
        Country code ('DE', 'FR', or 'SI')

    Returns:
    --------
    dict
        Dictionary with model names as keys and prediction dictionaries as values
    """
    models = {
        "Linear": train_predict_country(train_df, test_df, country_code, "linear"),
        "Polynomial": train_predict_country(
            train_df, test_df, country_code, "polynomial"
        ),
        "Ridge": train_predict_country(train_df, test_df, country_code, "ridge"),
    }
    return models
