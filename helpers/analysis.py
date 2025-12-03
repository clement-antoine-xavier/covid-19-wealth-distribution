"""Analysis utilities for wealth and COVID-19 correlation."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from .config import WEALTH_METRICS, COUNTRY_NAMES


def merge_wealth_covid(df_wealth, df_covid_quarterly, country_code, country_name):
    """
    Merge wealth and COVID-19 data for a specific country.

    Parameters:
    -----------
    df_wealth : DataFrame
        Wealth distribution data
    df_covid_quarterly : DataFrame
        Quarterly aggregated COVID-19 data
    country_code : str
        Country code ('DE', 'FR', or 'SI')
    country_name : str
        Country name as it appears in COVID dataset

    Returns:
    --------
    DataFrame
        Merged dataset with wealth metrics and COVID-19 statistics
    """
    # Get relevant wealth columns
    metrics = WEALTH_METRICS[country_code]

    # Filter COVID data for this country
    covid_country = df_covid_quarterly[
        df_covid_quarterly["countriesAndTerritories"] == country_name
    ].copy()

    # Select only the columns we need from wealth data
    wealth_cols = ["DATE"] + list(metrics.values())
    wealth_country = df_wealth[wealth_cols].copy()

    # Rename metric columns to simpler names
    rename_dict = {v: k for k, v in metrics.items()}
    wealth_country = wealth_country.rename(columns=rename_dict)

    # Merge on DATE
    merged = pd.merge(
        wealth_country,
        covid_country[["DATE", "cases_per_100k", "deaths_per_100k"]],
        on="DATE",
        how="inner",
    )

    return merged


def calculate_correlations(merged):
    """
    Calculate correlations between wealth metrics and COVID-19 severity.

    Measures linear relationships to identify potential connections between
    pandemic impact and wealth distribution patterns.

    Parameters:
    -----------
    merged : DataFrame
        Merged wealth and COVID data

    Returns:
    --------
    dict : Correlation values for key relationships
    """
    correlations = {
        "Gini vs Cases": merged["gini"].corr(merged["cases_per_100k"]),
        "Gini vs Deaths": merged["gini"].corr(merged["deaths_per_100k"]),
        "Median Wealth vs Cases": merged["median_wealth"].corr(
            merged["cases_per_100k"]
        ),
        "Median Wealth vs Deaths": merged["median_wealth"].corr(
            merged["deaths_per_100k"]
        ),
        "Mean Wealth vs Cases": merged["mean_wealth"].corr(merged["cases_per_100k"]),
        "Mean Wealth vs Deaths": merged["mean_wealth"].corr(merged["deaths_per_100k"]),
    }
    return correlations


def plot_correlation_heatmap(merged_dict):
    """
    Create correlation heatmap visualizations for all countries.

    Visualizes the strength and direction of linear relationships between
    wealth metrics (Gini, median/mean wealth) and COVID-19 severity (cases/deaths).

    Parameters:
    -----------
    merged_dict : dict
        Dictionary with country names as keys and merged DataFrames as values
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(
        "COVID-19 vs Wealth Metrics: Correlation Analysis",
        fontsize=16,
        fontweight="bold",
    )

    for ax, (name, merged) in zip(axes.flatten(), merged_dict.items()):
        # Select numeric columns for correlation
        cols = [
            "gini",
            "median_wealth",
            "mean_wealth",
            "cases_per_100k",
            "deaths_per_100k",
        ]
        corr_matrix = merged[cols].corr()

        # Create heatmap
        im = ax.imshow(corr_matrix, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")

        # Set tick labels
        ax.set_xticks(np.arange(len(corr_matrix.columns)))
        ax.set_yticks(np.arange(len(corr_matrix.columns)))
        ax.set_xticklabels(
            [
                "Gini",
                "Median\nWealth",
                "Mean\nWealth",
                "Cases\nper 100k",
                "Deaths\nper 100k",
            ],
            fontsize=9,
        )
        ax.set_yticklabels(
            [
                "Gini",
                "Median Wealth",
                "Mean Wealth",
                "Cases per 100k",
                "Deaths per 100k",
            ],
            fontsize=9,
        )
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        # Add correlation values as text
        for i in range(len(corr_matrix)):
            for j in range(len(corr_matrix)):
                ax.text(
                    j,
                    i,
                    f"{corr_matrix.iloc[i, j]:.2f}",
                    ha="center",
                    va="center",
                    color="black",
                    fontsize=9,
                )

        ax.set_title(name, fontweight="bold", fontsize=12)

    # Add colorbar
    fig.colorbar(
        im,
        ax=axes,
        orientation="horizontal",
        pad=0.1,
        shrink=0.8,
        label="Correlation Coefficient",
    )
    plt.tight_layout()
    plt.show()


def plot_wealth_distribution_comparison(df, title="Wealth Concentration"):
    """
    Compare wealth distribution metrics across countries.

    Parameters:
    -----------
    df : DataFrame
        Full wealth dataset
    title : str
        Title for the visualization
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for idx, (code, name) in enumerate(COUNTRY_NAMES.items()):
        ax = axes[idx]

        # Get the metric column names for this country
        top10_col = WEALTH_METRICS[code]["net_wealth_top10"]
        bottom50_col = WEALTH_METRICS[code]["net_wealth_bottom50"]

        # Plot both segments
        ax.plot(
            df["DATE"],
            df[top10_col] / 1e9,
            label="Top 10%",
            linewidth=2.5,
            color="#d62728",
            marker="o",
            markersize=3,
        )
        ax.plot(
            df["DATE"],
            df[bottom50_col] / 1e9,
            label="Bottom 50%",
            linewidth=2.5,
            color="#1f77b4",
            marker="s",
            markersize=3,
        )

        # Mark COVID-19 period
        ax.axvline(
            pd.Timestamp("2020-03-01"),
            color="red",
            linestyle="--",
            alpha=0.5,
            linewidth=1.5,
            label="COVID-19 Start",
        )
        ax.axvspan(
            pd.Timestamp("2020-01-01"),
            pd.Timestamp("2021-12-31"),
            alpha=0.1,
            color="red",
        )

        ax.set_title(f"{name}: Wealth by Segment", fontsize=14, fontweight="bold")
        ax.set_xlabel("Date", fontsize=11)
        ax.set_ylabel("Net Wealth (Billion EUR)", fontsize=11)
        ax.legend(loc="upper left", fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()


def calculate_wealth_concentration_ratios(df):
    """
    Calculate and visualize wealth concentration ratios for all countries.

    Parameters:
    -----------
    df : DataFrame
        Full wealth dataset

    Returns:
    --------
    dict
        Dictionary with country names and their concentration metrics
    """
    results = {}
    data_for_plot = []

    for code, name in COUNTRY_NAMES.items():
        top10_col = WEALTH_METRICS[code]["net_wealth_top10"]
        bottom50_col = WEALTH_METRICS[code]["net_wealth_bottom50"]

        # Pre-COVID average (2019)
        pre_covid = df[df["DATE"].dt.year == 2019]
        ratio_2019 = (pre_covid[top10_col] / pre_covid[bottom50_col]).mean()

        # Post-COVID recent (2024)
        post_covid = df[df["DATE"].dt.year == 2024]
        ratio_2024 = (post_covid[top10_col] / post_covid[bottom50_col]).mean()

        change = ((ratio_2024 - ratio_2019) / ratio_2019) * 100

        results[name] = {
            "ratio_2019": ratio_2019,
            "ratio_2024": ratio_2024,
            "change_pct": change,
        }
        data_for_plot.append((name, ratio_2019, ratio_2024, change))

    # Create visualization
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(
        "WEALTH CONCENTRATION: Top 10% to Bottom 50% Ratio",
        fontsize=16,
        fontweight="bold",
        y=1.02,
    )

    countries = [d[0] for d in data_for_plot]
    ratios_2019 = [d[1] for d in data_for_plot]
    ratios_2024 = [d[2] for d in data_for_plot]
    changes = [d[3] for d in data_for_plot]

    # Panel 1: 2019 vs 2024 Ratios
    ax1 = axes[0]
    x = np.arange(len(countries))
    width = 0.35
    bars1 = ax1.bar(
        x - width / 2, ratios_2019, width, label="2019", color="#1f77b4", alpha=0.8
    )
    bars2 = ax1.bar(
        x + width / 2, ratios_2024, width, label="2024", color="#ff7f0e", alpha=0.8
    )
    ax1.set_ylabel("Concentration Ratio (times)", fontweight="bold")
    ax1.set_title("Concentration Ratios: 2019 vs 2024", fontweight="bold")
    ax1.set_xticks(x)
    ax1.set_xticklabels(countries)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis="y")

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(
                bar.get_x() + bar.get_width() / 2.0,
                height,
                f"{height:.1f}x",
                ha="center",
                va="bottom",
                fontsize=9,
            )

    # Panel 2: Change Percentage
    ax2 = axes[1]
    colors_change = ["#2ca02c" if c < 0 else "#d62728" for c in changes]
    bars = ax2.barh(countries, changes, color=colors_change, alpha=0.7)
    ax2.set_xlabel("Change (%)", fontweight="bold")
    ax2.set_title("Percentage Change (2019→2024)", fontweight="bold")
    ax2.axvline(x=0, color="black", linestyle="-", linewidth=0.8)
    ax2.grid(True, alpha=0.3, axis="x")

    # Add value labels
    for i, (bar, val) in enumerate(zip(bars, changes)):
        width = bar.get_width()
        label_x_pos = width + (0.3 if width > 0 else -0.3)
        ax2.text(
            label_x_pos,
            bar.get_y() + bar.get_height() / 2.0,
            f"{val:+.1f}%",
            ha="left" if width > 0 else "right",
            va="center",
            fontweight="bold",
        )

    # Panel 3: Summary Table
    ax3 = axes[2]
    ax3.axis("tight")
    ax3.axis("off")

    table_data = []
    for name, r2019, r2024, chg in data_for_plot:
        trend = "↓ Narrowing" if chg < 0 else "↑ Widening"
        table_data.append([name, f"{r2019:.2f}x", f"{r2024:.2f}x", f"{chg:+.1f}%", trend])

    table = ax3.table(
        cellText=table_data,
        colLabels=["Country", "2019", "2024", "Change", "Trend"],
        cellLoc="center",
        loc="center",
        colColours=["#f0f0f0"] * 5,
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)

    # Color code the change column
    for i in range(1, len(table_data) + 1):
        cell = table[(i, 4)]
        if "↓" in table_data[i - 1][4]:
            cell.set_facecolor("#d5f4e6")
        else:
            cell.set_facecolor("#ffd5d5")

    ax3.set_title("Concentration Ratios Summary", fontweight="bold", pad=20)

    plt.tight_layout()
    plt.show()

    return results

