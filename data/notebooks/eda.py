# notebooks/eda.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # optional for heatmap

df = pd.read_csv("data/consumption.csv", parse_dates=["timestamp"])
df.set_index("timestamp", inplace=True)

# 1. Basic cleaning
print(df.info())
df = df.sort_index()
# Fill missing numeric with interpolation
num_cols = ["kwh","voltage","current","temperature"]
df[num_cols] = df[num_cols].interpolate().fillna(method="bfill").fillna(method="ffill")

# 2. Create features
df["hour"] = df.index.hour
df["dayofweek"] = df.index.dayofweek
df["is_weekend"] = df["dayofweek"].isin([5,6]).astype(int)

# 3. EDA summaries
print(df.describe())

# 4. Visualizations
plt.figure(figsize=(12,4))
df["kwh"].resample("D").sum().plot(title="Daily kWh consumption")
plt.savefig("outputs/daily_kwh.png")

plt.figure(figsize=(12,4))
df.groupby("hour")["kwh"].mean().plot(kind="bar", title="Average consumption by hour")
plt.savefig("outputs/hourly_avg.png")

# Heatmap of correlations
plt.figure(figsize=(6,5))
sns.heatmap(df[num_cols+["hour","dayofweek"]].corr(), annot=True)
plt.savefig("outputs/heatmap.png")
