
import pandas as pd
from pathlib import Path

# File paths
input_file = Path("../dataset/clean_supply_chain.csv")
output_file = Path("../dataset/supply_chain_mysql.csv")

# Load cleaned dataset
df = pd.read_csv(input_file, low_memory=False)

# Rename columns to match MySQL table
column_mapping = {
    "Type": "transaction_type",
    "Days for shipping (real)": "days_for_shipping_real",
    "Days for shipment (scheduled)": "days_for_shipment_scheduled",
    "Delivery Status": "delivery_status",
    "Late_delivery_risk": "late_delivery_risk",
    "Category Id": "category_id",
    "Category Name": "category_name",
    "Customer Segment": "customer_segment",
    "Department Id": "department_id",
    "Department Name": "department_name",
    "Market": "market",
    "Order City": "order_city",
    "Order Country": "order_country",
    "Order Customer Id": "order_customer_id",
    "Order Id": "order_id",
    "Order Item Discount": "order_item_discount",
    "Order Item Discount Rate": "order_item_discount_rate",
    "Order Item Id": "order_item_id",
    "Order Item Product Price": "order_item_product_price",
    "Order Item Profit Ratio": "order_item_profit_ratio",
    "Order Item Quantity": "order_item_quantity",
    "Sales": "sales",
    "Order Item Total": "order_item_total",
    "Order Profit Per Order": "order_profit_per_order",
    "Order Region": "order_region",
    "Order State": "order_state",
    "Order Status": "order_status",
    "Product Card Id": "product_card_id",
    "Product Category Id": "product_category_id",
    "Product Name": "product_name",
    "Product Price": "product_price",
    "Product Status": "product_status",
    "Shipping Mode": "shipping_mode",
    "Order Date": "order_date",
    "Shipping Date": "shipping_date",
    "Shipping Delay": "shipping_delay",
    "Order Year": "order_year",
    "Order Month": "order_month",
    "Order Month Name": "order_month_name",
    "Order Year-Month": "order_year_month"
}

# Check missing columns before renaming
missing_columns = [
    col for col in column_mapping if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing columns: {missing_columns}")

df.rename(columns=column_mapping, inplace=True)

# Keep columns in exactly the same order as MySQL table
mysql_columns = [
    "order_item_id",
    "transaction_type",
    "days_for_shipping_real",
    "days_for_shipment_scheduled",
    "delivery_status",
    "late_delivery_risk",
    "category_id",
    "category_name",
    "customer_segment",
    "department_id",
    "department_name",
    "market",
    "order_city",
    "order_country",
    "order_customer_id",
    "order_id",
    "order_item_discount",
    "order_item_discount_rate",
    "order_item_product_price",
    "order_item_profit_ratio",
    "order_item_quantity",
    "sales",
    "order_item_total",
    "order_profit_per_order",
    "order_region",
    "order_state",
    "order_status",
    "product_card_id",
    "product_category_id",
    "product_name",
    "product_price",
    "product_status",
    "shipping_mode",
    "order_date",
    "shipping_date",
    "shipping_delay",
    "order_year",
    "order_month",
    "order_month_name",
    "order_year_month"
]

df = df[mysql_columns].copy()

# Convert date columns into MySQL-compatible format
for col in ["order_date", "shipping_date"]:
    df[col] = pd.to_datetime(
        df[col], errors="raise"
    ).dt.strftime("%Y-%m-%d %H:%M:%S")

# Validate primary key
if df["order_item_id"].isnull().any():
    raise ValueError("Missing order_item_id values found.")

if df["order_item_id"].duplicated().any():
    raise ValueError("Duplicate order_item_id values found.")

# Export CSV
df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print("MySQL CSV preparation completed!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Duplicate item IDs:", df["order_item_id"].duplicated().sum())
print("Output file:", output_file.resolve())
