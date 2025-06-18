# Step 1: Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load the Iris dataset from seaborn
df = sns.load_dataset("iris")

# Step 3: Save the dataset as a CSV file
df.to_csv("iris.csv", index=False)
print("✔️ CSV file 'iris.csv' saved successfully.")

# Step 4: Display dataset structure
print("Dataset Shape:", df.shape)
print("Column Names:", df.columns.tolist())
print("\nFirst 5 Rows:\n", df.head())

# ============================
# Step 5: Scatter Plot (Pairplot)
# ============================
sns.pairplot(df, hue="species")
plt.suptitle("Scatter Plot - Pairwise Relationships", y=1.02)
plt.show()

# ============================
# Step 6: Histogram
# ============================
df.hist(figsize=(10, 8), edgecolor="black")
plt.suptitle("Histogram - Feature Distributions")
plt.tight_layout()
plt.show()

# ============================
# Step 7: Box Plot
# ============================
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, orient="h")
plt.title("Box Plot - Spread and Outliers")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='sepal_width', data=df)
plt.title("Sepal Width by Species")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='species', y='petal_width', data=df)
plt.title("Petal Width by Species")
plt.show()

