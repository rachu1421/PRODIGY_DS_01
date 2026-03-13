import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("population.csv", skiprows=4)

# Convert 2024 column to numeric
df["2024"] = pd.to_numeric(df["2024"], errors="coerce")

# Select top 10 countries by population
top10 = df[["Country Name", "2024"]].dropna().sort_values(by="2024", ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(top10["Country Name"], top10["2024"])

plt.title("Top 10 Countries by Population (2024)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()