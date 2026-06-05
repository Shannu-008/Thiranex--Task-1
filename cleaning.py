import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. CREATE DIRECTORIES
# Ensures your project stays organized by creating an output folder automatically
os.makedirs("output", exist_ok=True)

# 2. CREATE DUMMY DATA (For testing purposes)
# Replace this entire section with: df = pd.read_csv('your_data.csv') when you have real data
data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 101],  # 101 is a duplicate
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Alice"],
    "Age": [25, 30, np.nan, 45, 22, 35, 25],  # Charlie has a missing age
    "Salary": [50000, 60000, 75000, -1000, 52000, 80000, 50000],  # David has an error (-1000)
    "Department": ["HR", "IT", "IT", "Sales", "HR", "Sales", "HR"],
}
df = pd.DataFrame(data)
print("--- RAW DATA ---")
print(df)

# 3. DATA CLEANING PROCESS

# Step 3a: Remove exact duplicate rows
df = df.drop_duplicates()

# Step 3b: Handle missing values (Fill Charlie's missing age with the average age)
average_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(average_age)

# Step 3c: Fix data errors / outliers (Fix David's negative salary by making it positive)
df["Salary"] = df["Salary"].abs()

# Step 3d: Fix Data Types (Ensure IDs and Ages are integers)
df["Age"] = df["Age"].astype(int)

print("\n--- CLEANED DATA ---")
print(df)

# 4. DATA VISUALIZATION

# Set the visual style
sns.set_theme(style="whitegrid")

# Create a Bar Plot: Average Salary per Department
plt.figure(figsize=(8, 5))
sns.barplot(x="Department", y="Salary", data=df, estimator=np.mean, errorbar=None, palette="Blues_d")

# Add titles and labels
plt.title("Average Salary by Department", fontsize=14, fontweight="bold")
plt.xlabel("Department", fontsize=12)
plt.ylabel("Average Salary ($)", fontsize=12)

# Save the visualization to your output folder
output_path = os.path.join("output", "salary_by_department.png")
plt.savefig(output_path, bbox_inches="tight", dpi=300)
print(f"\n[Success] Visualization saved safely to: {output_path}")

# Close the plot to free up memory
plt.close()