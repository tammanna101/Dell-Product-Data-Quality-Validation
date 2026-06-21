import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("product_validation.csv")

# -----------------------------
# Data Quality Summary
# -----------------------------
total_records = len(df)

valid_records = len(
    df[df["Validation_Status"] == "Valid"]
)

missing_records = len(
    df[df["Source_Value"].isnull()]
)

not_found_records = len(
    df[df["Validation_Status"] == "Not Found"]
)

success_rate = round(
    (valid_records / total_records) * 100,
    2
)

print("========== DATA QUALITY SUMMARY ==========")
print(f"Total Records      : {total_records}")
print(f"Valid Records      : {valid_records}")
print(f"Missing Records    : {missing_records}")
print(f"Not Found Records  : {not_found_records}")
print(f"Success Rate (%)   : {success_rate}")

# -----------------------------
# Top Missing Attributes
# -----------------------------
missing_attributes = (
    df[df["Source_Value"].isnull()]
    .groupby("Attribute_Name")
    .size()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Missing Attributes")
print(missing_attributes)

# -----------------------------
# Visualization
# -----------------------------
plt.figure(figsize=(8,5))

missing_attributes.plot(
    kind="bar"
)

plt.title("Top 5 Attributes with Missing Values")
plt.xlabel("Attribute Name")
plt.ylabel("Missing Count")

plt.tight_layout()
plt.show()
