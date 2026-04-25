import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    sea_level_df = df[["Year", "CSIRO Adjusted Sea Level"]].dropna()

    fig, ax = plt.subplots()
    ax.scatter(sea_level_df["Year"], sea_level_df["CSIRO Adjusted Sea Level"])

    first_fit = linregress(
        sea_level_df["Year"],
        sea_level_df["CSIRO Adjusted Sea Level"],
    )
    years_to_2050 = range(sea_level_df["Year"].min(), 2051)
    ax.plot(
        list(years_to_2050),
        [first_fit.slope * year + first_fit.intercept for year in years_to_2050],
        color="red",
    )

    recent_df = sea_level_df[sea_level_df["Year"] >= 2000]
    recent_fit = linregress(
        recent_df["Year"],
        recent_df["CSIRO Adjusted Sea Level"],
    )
    recent_years_to_2050 = range(2000, 2051)
    ax.plot(
        list(recent_years_to_2050),
        [recent_fit.slope * year + recent_fit.intercept for year in recent_years_to_2050],
        color="green",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return ax
