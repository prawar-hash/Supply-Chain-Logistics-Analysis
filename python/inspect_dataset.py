
import csv
from pathlib import Path
import pandas as pd

# Dataset location
file_path = Path("dataset/supply_chain.csv")

# Check whether the file exists
if not file_path.exists():
    raise FileNotFoundError(f"Dataset not found: {file_path.resolve()}")

# Detect the CSV delimiter
with open(file_path, "r", encoding="latin1") as file:
    sample = file.read(10000)

try:
    delimiter = csv.Sniffer().sniff(
        sample, delimiters=",;\t|"
    ).delimiter
except csv.Error:
    delimiter = ","

# Load dataset
df = pd.read_csv(
    file_path,
    sep=delimiter,
    encoding="latin1",
    low_memory=False
)

# 1. Dataset dimensions
print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. First five records
print("\n--- FIRST FIVE ROWS ---")
print(df.head().to_string())

# 3. Column names
print("\n--- COLUMN NAMES ---")
for column in df.columns:
    print(column)

# 4. Data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# 5. Missing values
print("\n--- MISSING VALUES ---")
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

if missing.empty:
    print("No missing values found.")
else:
    print(missing)

# 6. Duplicate records
print("\n--- DUPLICATE RECORDS ---")
print("Duplicate rows:", df.duplicated().sum())

# 7. Unique values per column
print("\n--- UNIQUE VALUES ---")
print(df.nunique().sort_values(ascending=False).head(15))

print("\nDataset inspection completed!")


# 8. Check date formats
print("\n--- DATE SAMPLES ---")
print("Order Dates:")
print(df["order date (DateOrders)"].head().to_list())

print("\nShipping Dates:")
print(df["shipping date (DateOrders)"].head().to_list())

# 9. Check unique orders and order items
print("\n--- ORDER INFORMATION ---")
print("Unique Orders:", df["Order Id"].nunique())
print("Unique Order Items:", df["Order Item Id"].nunique())

# 10. Important categorical values
print("\n--- BUSINESS CATEGORIES ---")

columns = [
    "Delivery Status",
    "Shipping Mode",
    "Order Status",
    "Market",
    "Customer Segment",
    "Department Name"
]

for col in columns:
    print(f"\n{col}:")
    print(df[col].value_counts().head(10).to_string())

# 11. Important numerical statistics
print("\n--- NUMERICAL SUMMARY ---")

numeric_columns = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Sales",
    "Order Item Quantity",
    "Order Profit Per Order",
    "Late_delivery_risk"
]

print(df[numeric_columns].describe())


# 12. Date range
print("\n--- DATE RANGE ---")

order_dates = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

shipping_dates = pd.to_datetime(
    df["shipping date (DateOrders)"],
    errors="coerce"
)

print("First Order Date:", order_dates.min())
print("Last Order Date:", order_dates.max())
print("Invalid Order Dates:", order_dates.isna().sum())
print("Invalid Shipping Dates:", shipping_dates.isna().sum())


# 13. Sales and profit summary
print("\n--- SALES & PROFIT ---")

print("Total Sales:", df["Sales"].sum())
print("Average Sales per Item:", df["Sales"].mean())
print("Total Profit:", df["Order Profit Per Order"].sum())
print("Average Profit per Order Item:", df["Order Profit Per Order"].mean())


# 14. Delivery performance percentage
print("\n--- DELIVERY PERFORMANCE ---")

delivery_counts = df["Delivery Status"].value_counts()
delivery_percentage = df["Delivery Status"].value_counts(normalize=True) * 100

print(delivery_counts)
print("\nPercentage:")
print(delivery_percentage.round(2))


# 15. Shipping mode performance
print("\n--- SHIPPING MODE ---")

shipping_summary = df.groupby("Shipping Mode").agg(
    Orders=("Order Id", "nunique"),
    Items=("Order Item Id", "count"),
    Avg_Shipping_Days=("Days for shipping (real)", "mean"),
    Avg_Scheduled_Days=("Days for shipment (scheduled)", "mean")
).sort_values("Orders", ascending=False)

print(shipping_summary)


# 16. Market performance
print("\n--- MARKET PERFORMANCE ---")

market_summary = df.groupby("Market").agg(
    Orders=("Order Id", "nunique"),
    Sales=("Sales", "sum"),
    Profit=("Order Profit Per Order", "sum"),
    Avg_Shipping_Days=("Days for shipping (real)", "mean")
).sort_values("Sales", ascending=False)

print(market_summary)


# 17. Top product categories
print("\n--- TOP PRODUCT CATEGORIES ---")

category_summary = df.groupby("Category Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Order Profit Per Order", "sum"),
    Quantity=("Order Item Quantity", "sum")
).sort_values("Sales", ascending=False)

print(category_summary.head(10))