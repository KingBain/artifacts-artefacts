"""
generate_graph.py

Reads data from stats/usage.csv and outputs an XKCD style graph at stats/usage.png.
"""
import os

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

OUTPUT_PATH = "stats/usage.png"

matplotlib.use("Agg")

# Use XKCD style for a hand-drawn effect
plt.xkcd()

# Read the CSV
df = pd.read_csv("stats/usage.csv", parse_dates=["date"])

# Drop duplicate dates (keep last if multiple entries on same day)
df = df.drop_duplicates(subset="date", keep="last")

# Convert datetime to just date (this ensures no time component)
df["just_date"] = df["date"].dt.date

# Get a title from the environment (fallback to a default)
title = os.getenv("CHART_TITLE", "Public Github Usage Over Time")

# Create figure + axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot using the “just_date” column
ax.plot(df["just_date"], df["count"], marker="o")

# Force Y-axis ticks to be integers only
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Force X-axis to show one tick per unique date
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(
    mdates.DateFormatter("%m-%d")
)  # Show only month-day (e.g., 06-01)

# Rotate X-axis labels 45° so they don’t overlap
fig.autofmt_xdate(rotation=45)

# Labels + title
ax.set_xlabel("Date")
ax.set_ylabel("Repo Count")
ax.set_title(title)

plt.tight_layout()

plt.savefig(OUTPUT_PATH)
print(f"Saved graph to {OUTPUT_PATH}")
