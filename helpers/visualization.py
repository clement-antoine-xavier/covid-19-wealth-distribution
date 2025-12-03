"""Visualization utilities for wealth distribution analysis."""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.patches import Patch
from .config import WEALTH_METRICS, COUNTRY_NAMES


def plot_country_wealth_panels(df_slice, country_code):
    """
    Create a 2x2 panel plot showing all wealth metrics for a specific country.

    Parameters:
    -----------
    df_slice : DataFrame
        Filtered DataFrame containing the data to plot
    country_code : str
        Country code ('DE', 'FR', or 'SI')

    Displays:
    ---------
    A figure with 4 subplots showing:
    - Median Wealth, Mean Wealth (top row)
    - Net Wealth, Gini Coefficient (bottom row)
    """
    metrics = WEALTH_METRICS[country_code]
    name = COUNTRY_NAMES[country_code]

    # Create 2x2 subplot grid
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        f"{name} - Wealth Distribution Metrics (2016-2019)",
        fontsize=16,
        fontweight="bold",
    )

    # Plot 1: Median Wealth
    axes[0, 0].plot(
        df_slice["DATE"],
        df_slice[metrics["median_wealth"]],
        color="#ff7f0e",
        linewidth=2,
        marker="o",
    )
    axes[0, 0].set_title("Net Wealth - Median", fontweight="bold")
    axes[0, 0].set_ylabel("EUR")
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis="x", rotation=45)

    # Plot 2: Mean Wealth
    axes[0, 1].plot(
        df_slice["DATE"],
        df_slice[metrics["mean_wealth"]],
        color="#2ca02c",
        linewidth=2,
        marker="o",
    )
    axes[0, 1].set_title("Net Wealth - Mean", fontweight="bold")
    axes[0, 1].set_ylabel("EUR")
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].tick_params(axis="x", rotation=45)

    # Plot 3: Net Wealth
    axes[1, 0].plot(
        df_slice["DATE"],
        df_slice[metrics["net_wealth"]],
        color="#d62728",
        linewidth=2,
        marker="o",
    )
    axes[1, 0].set_title("Adjusted Net Wealth", fontweight="bold")
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].set_ylabel("EUR (millions)")
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].tick_params(axis="x", rotation=45)

    # Plot 4: Gini Coefficient (inequality measure: higher = more inequality)
    axes[1, 1].plot(
        df_slice["DATE"],
        df_slice[metrics["gini"]],
        color="#9467bd",
        linewidth=2,
        marker="o",
    )
    axes[1, 1].set_title("Gini Coefficient", fontweight="bold")
    axes[1, 1].set_xlabel("Date")
    axes[1, 1].set_ylabel("Gini")
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()


def plot_prediction_vs_actual(
    test_df, preds_country, country_code, model_name="Linear"
):
    """
    Plot predicted vs actual values for all wealth metrics to visualize COVID-19 impact.

    Parameters:
    -----------
    test_df : DataFrame
        Test data containing actual values
    preds_country : dict
        Dictionary of predictions from train_predict_country()
    country_code : str
        Country code ('DE', 'FR', or 'SI')
    model_name : str, default='Linear'
        Name of the model for the title

    Displays:
    ---------
    A 2x3 panel plot comparing predicted (dotted line) vs actual (solid line) values.
    Deviations indicate COVID-19 disruption to pre-pandemic trends.
    """
    name = COUNTRY_NAMES[country_code]
    metrics = WEALTH_METRICS[country_code]

    # Titles for each metric
    mapping_titles = {
        "total_assets": "Adjusted Total Assets",
        "median_wealth": "Net Wealth - Median",
        "mean_wealth": "Net Wealth - Mean",
        "net_wealth": "Adjusted Net Wealth",
        "gini": "Gini Coefficient",
    }
    order = ["total_assets", "median_wealth", "mean_wealth", "net_wealth", "gini"]

    # Create subplot grid
    fig, axes = plt.subplots(2, 3, figsize=(20, 10))
    fig.suptitle(
        f"{name} - {model_name} Prediction vs Actual (2020-2025)",
        fontsize=16,
        fontweight="bold",
    )

    # Plot each metric
    for idx, metric_key in enumerate(order):
        if metric_key not in preds_country:
            continue
        r, c = divmod(idx, 3)  # Calculate subplot position
        ax = axes[r, c]
        col = metrics[metric_key]

        # Plot actual values (solid line with circles)
        ax.plot(
            test_df["DATE"],
            test_df[col],
            "o-",
            label="Actual",
            linewidth=2,
            markersize=6,
            color="#1f77b4",
        )
        # Plot predicted values (dashed line with squares)
        ax.plot(
            test_df["DATE"],
            preds_country[metric_key],
            "s--",
            label="Predicted",
            linewidth=2,
            markersize=6,
            color="#ff7f0e",
        )

        ax.set_title(mapping_titles[metric_key], fontweight="bold")
        ax.grid(True, alpha=0.3)
        ax.tick_params(axis="x", rotation=45)

        # Set appropriate y-axis label based on metric type
        if metric_key in ["total_assets", "net_wealth"]:
            ax.set_ylabel("EUR (millions)")
        elif metric_key in ["median_wealth", "mean_wealth"]:
            ax.set_ylabel("EUR")
        else:
            ax.set_ylabel("Gini")

        ax.legend()

    # Hide unused subplot
    axes[1, 2].axis("off")
    plt.tight_layout()
    plt.show()


def plot_config_summary():
    """
    Visualize configuration summary showing available countries and metrics.
    
    Displays:
    ---------
    A 2-panel figure showing:
    - Available countries in the analysis
    - Metrics per country with category color coding
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

    # Display countries
    countries = list(COUNTRY_NAMES.keys())
    country_names = [COUNTRY_NAMES[code] for code in countries]
    ax1.barh(country_names, [1]*len(countries), color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax1.set_xlabel('Countries in Analysis', fontweight='bold')
    ax1.set_title('Available Countries', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1.2)
    ax1.set_xticks([])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)

    # Display metrics
    metrics = list(WEALTH_METRICS['DE'].keys())
    metric_labels = ['Median\nWealth', 'Mean\nWealth', 'Net\nWealth', 'Gini', 
                     'Top 10%', 'Bottom 50%', 'Share\nB50%', 'Share\nT10%', 'Share\nT5%']
    colors = ['#ff7f0e']*4 + ['#2ca02c']*2 + ['#d62728']*3
    bars = ax2.bar(range(len(metrics)), [1]*len(metrics), color=colors, alpha=0.7)
    ax2.set_xticks(range(len(metrics)))
    ax2.set_xticklabels(metric_labels, fontsize=9, rotation=0)
    ax2.set_ylabel('Metric Categories', fontweight='bold')
    ax2.set_title(f'Metrics per Country (n={len(metrics)})', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 1.5)
    ax2.set_yticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    # Add legend
    legend_elements = [
        Patch(facecolor='#ff7f0e', alpha=0.7, label='Aggregate'),
        Patch(facecolor='#2ca02c', alpha=0.7, label='Distributional'),
        Patch(facecolor='#d62728', alpha=0.7, label='Shares')
    ]
    ax2.legend(handles=legend_elements, loc='upper right', fontsize=9)

    plt.tight_layout()
    plt.show()


def plot_dataset_summary(df, train_df, test_df):
    """
    Visualize comprehensive dataset summary with multiple panels.
    
    Parameters:
    -----------
    df : DataFrame
        Full dataset
    train_df : DataFrame
        Training dataset
    test_df : DataFrame
        Test dataset
    
    Displays:
    ---------
    A 2x2 panel figure showing:
    - Dataset dimensions
    - Data timeline
    - Train/test split
    - Summary information
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # Dataset size
    ax1 = axes[0, 0]
    categories = ['Rows', 'Columns']
    values = [df.shape[0], df.shape[1]]
    bars = ax1.bar(categories, values, color=['#1f77b4', '#ff7f0e'], alpha=0.7)
    ax1.set_ylabel('Count', fontweight='bold')
    ax1.set_title('Dataset Dimensions', fontsize=12, fontweight='bold')
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(val)}', ha='center', va='bottom', fontweight='bold')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Timeline visualization
    ax2 = axes[0, 1]
    timeline_dates = [df['DATE'].min(), pd.Timestamp('2020-01-01'), df['DATE'].max()]
    timeline_labels = ['Start\n' + df['DATE'].min().strftime('%Y-%m'), 
                       'COVID Split\n2020-01', 
                       'End\n' + df['DATE'].max().strftime('%Y-%m')]
    ax2.plot([0, 1, 2], [0, 0, 0], 'o-', markersize=12, linewidth=3, color='#2ca02c')
    ax2.set_xticks([0, 1, 2])
    ax2.set_xticklabels(timeline_labels, fontsize=9)
    ax2.set_ylim(-0.5, 0.5)
    ax2.set_yticks([])
    ax2.set_title('Data Timeline', fontsize=12, fontweight='bold')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.grid(True, axis='x', alpha=0.3)

    # Train/Test split
    ax3 = axes[1, 0]
    split_data = {'Training\n(2016-2019)': len(train_df), 'Test\n(2020-2025)': len(test_df)}
    colors_split = ['#1f77b4', '#ff7f0e']
    bars = ax3.bar(split_data.keys(), split_data.values(), color=colors_split, alpha=0.7)
    ax3.set_ylabel('Number of Quarters', fontweight='bold')
    ax3.set_title('Train/Test Split', fontsize=12, fontweight='bold')
    for bar, val in zip(bars, split_data.values()):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(val)}', ha='center', va='bottom', fontweight='bold')
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)

    # Period breakdown
    ax4 = axes[1, 1]
    period_info = [
        f"Full Dataset: {df.shape[0]} quarters",
        f"Training: {len(train_df)} quarters",
        f"Testing: {len(test_df)} quarters",
        f"Date Range: {df['DATE'].min().strftime('%Y-%m')} to {df['DATE'].max().strftime('%Y-%m')}"
    ]
    ax4.text(0.1, 0.7, '\n'.join(period_info), fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.axis('off')
    ax4.set_title('Dataset Summary', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.show()


def plot_covid_summary(covid_quarterly):
    """
    Visualize COVID-19 dataset summary.
    
    Parameters:
    -----------
    covid_quarterly : DataFrame
        Quarterly aggregated COVID-19 data
    
    Displays:
    ---------
    A 3-panel figure showing:
    - COVID dataset dimensions
    - Date range
    - Countries included
    """
    fig, axes = plt.subplots(1, 3, figsize=(16, 4))

    # COVID data dimensions
    ax1 = axes[0]
    dims = ['Rows', 'Columns']
    vals = [covid_quarterly.shape[0], covid_quarterly.shape[1]]
    bars = ax1.bar(dims, vals, color=['#d62728', '#9467bd'], alpha=0.7)
    ax1.set_ylabel('Count', fontweight='bold')
    ax1.set_title('COVID Dataset Dimensions', fontsize=12, fontweight='bold')
    for bar, val in zip(bars, vals):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(val)}', ha='center', va='bottom', fontweight='bold')
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # Date range
    ax2 = axes[1]
    date_info = [
        ('Start', covid_quarterly['DATE'].min().strftime('%Y-%m')),
        ('End', covid_quarterly['DATE'].max().strftime('%Y-%m'))
    ]
    positions = [0, 1]
    ax2.barh(positions, [1, 1], color=['#2ca02c', '#d62728'], alpha=0.7)
    ax2.set_yticks(positions)
    ax2.set_yticklabels([d[1] for d in date_info], fontsize=10)
    ax2.set_xlabel('Timeline', fontweight='bold')
    ax2.set_title('COVID Data Date Range', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1.2)
    ax2.set_xticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    for i, (label, date) in enumerate(date_info):
        ax2.text(-0.1, i, label + ':', ha='right', va='center', fontweight='bold')

    # Countries
    ax3 = axes[2]
    countries_list = covid_quarterly['countriesAndTerritories'].unique()
    country_colors = {'Germany': '#1f77b4', 'France': '#ff7f0e', 'Slovenia': '#2ca02c'}
    colors_c = [country_colors.get(c, '#gray') for c in countries_list]
    ax3.barh(range(len(countries_list)), [1]*len(countries_list), color=colors_c, alpha=0.7)
    ax3.set_yticks(range(len(countries_list)))
    ax3.set_yticklabels(countries_list, fontsize=10)
    ax3.set_xlabel('Countries in Dataset', fontweight='bold')
    ax3.set_title(f'Countries (n={len(countries_list)})', fontsize=12, fontweight='bold')
    ax3.set_xlim(0, 1.2)
    ax3.set_xticks([])
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['bottom'].set_visible(False)

    plt.tight_layout()
    plt.show()
