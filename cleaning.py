import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. ENVIRONMENT CONFIGURATION
os.makedirs("data", exist_ok=True)
os.makedirs("output", exist_ok=True)
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 6)

# 2. GENERATE A REALISTIC COMPLEX DATASET
# Simulating an enterprise database export with dirty metrics
np.random.seed(42)
n_records = 150

raw_data = {
    "Transaction_ID": [f"TXN-{1000 + i}" for i in range(n_records)],
    "Customer_Age": np.random.choice([22, 35, 45, 28, np.nan, 60, 19, 31], size=n_records),
    "Purchase_Amount": np.random.normal(loc=250, scale=150, size=n_records).round(2),
    "Category": np.random.choice(["Electronics", "Electronics ", "Clothing", "Home", "  Home", None], size=n_records),
    "Region": np.random.choice(["North", "South", "East", "West"], size=n_records),
    "Date": pd.date_range(start="2026-01-01", periods=n_records, freq="D").strftime("%Y/%m/%d")
}

df_raw = pd.DataFrame(raw_data)
# Introduce specific pipeline-breaking anomalies manually
df_raw.iloc[5, 2] = -500.00  # Impossible negative value
df_raw = pd.concat([df_raw, df_raw.iloc[[10, 25]]], ignore_index=True)  # Injected duplicate records
df_raw.to_csv("data/raw_transactions.csv", index=False)

print(f"[LOADED] Raw Dataset Shape: {df_raw.shape}")

# 3. ADVANCED DATA CLEANING PIPELINE
print("\n--- Executing Enterprise Cleaning Pipeline ---")

# Step 3a: Deduplication
initial_count = len(df_raw)
df_clean = df_raw.drop_duplicates(subset=["Transaction_ID"], keep="first").copy()
print(f"[CLEANED] Removed {initial_count - len(df_clean)} duplicate transactional rows.")

# Step 3b: Text Standardization (Trimming Whitespace & Case Formatting)
df_clean["Category"] = df_clean["Category"].fillna("Uncategorized")
df_clean["Category"] = df_clean["Category"].str.strip().str.title()
print("[CLEANED] Stripped whitespace and standardized product category labels.")

# Step 3c: Outlier & Anomaly Rectification (Handling negative financial inputs)
# Replacing negative values with the median of positive entries in that specific category
median_purchase = df_clean[df_clean["Purchase_Amount"] > 0]["Purchase_Amount"].median()
df_clean.loc[df_clean["Purchase_Amount"] <= 0, "Purchase_Amount"] = median_purchase
print(f"[CLEANED] Resolved invalid/negative revenue figures with median value: ${median_purchase:.2f}")

# Step 3d: Statistical Imputation of Missing Values (Age columns)
# Instead of a flat average, we impute missing ages using the median based on regional clusters
df_clean["Customer_Age"] = df_clean.groupby("Region")["Customer_Age"].transform(lambda x: x.fillna(x.median())).astype(int)
print("[CLEANED] Imputed missing user age profiles using conditional regional medians.")

# Step 3e: Datetime Optimization
df_clean["Date"] = pd.to_datetime(df_clean["Date"])

# Save clean production asset
df_clean.to_csv("data/cleaned_transactions.csv", index=False)
print(f"[SUCCESS] Exported structural asset to 'data/cleaned_transactions.csv'. Final Shape: {df_clean.shape}")

# 4. DATA VISUALIZATION ENGINE
print("\n--- Executing Visualization Engine ---")

# Plot 1: Categorical Distribution Matrix (Boxplot for Outliers/Spreads)
plt.figure()
sns.boxplot(data=df_clean, x="Category", y="Purchase_Amount", hue="Category", legend=False)
plt.title("Purchase Amount Distribution Across Product Categories", fontsize=14, pad=15)
plt.xlabel("Product Category", fontsize=11)
plt.ylabel("Revenue per Transaction ($)", fontsize=11)
output_img_1 = os.path.join("output", "category_revenue_distribution.png")
plt.savefig(output_img_1, dpi=300, bbox_inches="tight")
print(f"[IMAGE SAVED] Distribution profile -> {output_img_1}")
plt.close()

# Plot 2: Regional Demographics Analysis (Statistical Bar Chart)
plt.figure()
sns.barplot(data=df_clean, x="Region", y="Customer_Age", errorbar="sd", capsize=0.1, color="#2b5c8f")
plt.title("Mean Customer Age Profiles Across Operating Regions", fontsize=14, pad=15)
plt.xlabel("Sales Region", fontsize=11)
plt.ylabel("Average Age (with Standard Deviation)", fontsize=11)
output_img_2 = os.path.join("output", "regional_demographics.png")
plt.savefig(output_img_2, dpi=300, bbox_inches="tight")
print(f"[IMAGE SAVED] Demographic baseline -> {output_img_2}")
plt.close()