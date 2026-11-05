import pandas as pd
from pathlib import Path

# -----------------------------
# File paths
# -----------------------------
input_file = Path("../dataset/supply_chain.csv")
output_file = Path("../dataset/clean_supply_chain.csv")

# -----------------------------
# Load original dataset
# -----------------------------
df = pd.read_csv(
    input_file,
    encoding="latin1",
    low_memory=False
)

print("Original shape:", df.shape)

# -----------------------------
# Select relevant columns
# -----------------------------
columns_to_keep = [
    "Type",
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Delivery Status",
    "Late_delivery_risk",
    "Category Id",
    "Category Name",
    "Customer Segment",
    "Department Id",
    "Department Name",
    "Market",
    "Order City",
    "Order Country",
    "Order Customer Id",
    "order date (DateOrders)",
    "Order Id",
    "Order Item Discount",
    "Order Item Discount Rate",
    "Order Item Id",
    "Order Item Product Price",
    "Order Item Profit Ratio",
    "Order Item Quantity",
    "Sales",
    "Order Item Total",
    "Order Profit Per Order",
    "Order Region",
    "Order State",
    "Order Status",
    "Product Card Id",
    "Product Category Id",
    "Product Name",
    "Product Price",
    "Product Status",
    "shipping date (DateOrders)",
    "Shipping Mode"
]

df = df[columns_to_keep].copy()

# -----------------------------
# Convert dates
# -----------------------------
df["Order Date"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

df["Shipping Date"] = pd.to_datetime(
    df["shipping date (DateOrders)"],
    errors="coerce"
)

# Remove old date columns
df.drop(
    columns=[
        "order date (DateOrders)",
        "shipping date (DateOrders)"
    ],
    inplace=True
)

# -----------------------------
# Create useful derived fields
# -----------------------------
df["Shipping Delay"] = (
    df["Days for shipping (real)"]
    - df["Days for shipment (scheduled)"]
)

df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.month_name()
df["Order Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

# -----------------------------
# Standardize text columns
# -----------------------------
text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()

# -----------------------------
# Remove duplicate rows
# -----------------------------
before_duplicates = len(df)

df.drop_duplicates(inplace=True)

after_duplicates = len(df)

print("Duplicates removed:", before_duplicates - after_duplicates)

# -----------------------------
# Check missing values
# -----------------------------
print("\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# -----------------------------
# Final information
# -----------------------------
print("\nCleaned shape:", df.shape)

print("\nShipping Delay summary:")
print(df["Shipping Delay"].describe())

# -----------------------------
# Save cleaned dataset
# -----------------------------
df.to_csv(
    output_file,
    index=False,
    encoding="utf-8"
)

print(f"\nCleaned dataset saved to: {output_file}")