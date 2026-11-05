# Supply Chain & Logistics Performance Analysis

An end-to-end Data Analyst project using Python, Pandas, MySQL, and Power BI to analyze sales performance, delivery operations, shipping delays, and regional supply chain trends.

## Project Overview

The objective of this project is to analyze supply chain and logistics data and generate meaningful business insights related to sales, profitability, delivery performance, shipping modes, and regional operations.

The project follows a complete data analytics workflow:

**Data Cleaning → Data Preparation → SQL Analysis → Power BI Dashboard → Business Insights**

## Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **MySQL**
- **SQL**
- **Power BI**
- **Matplotlib**
- **Seaborn**

## Project Workflow

### 1. Data Inspection & Cleaning

Python and Pandas were used to:

- Inspect the dataset structure and data types
- Check missing values
- Identify duplicate records
- Validate important fields
- Convert date columns into proper datetime format
- Create additional analytical columns

Additional columns created include:

- Shipping Delay
- Order Year
- Order Month
- Order Month Name
- Order Year-Month

### 2. MySQL Analysis

The cleaned dataset was imported into MySQL for structured analysis.

SQL was used to analyze:

- Total sales and profit
- Delivery status
- Shipping performance
- Market-wise performance
- Product category performance
- Shipping modes
- Monthly sales trends
- Customer segments

### 3. Power BI Dashboard

An interactive Power BI dashboard was developed to monitor key supply chain and logistics KPIs.

The dashboard includes:

- Total Sales
- Total Profit
- Total Orders
- Late Delivery %
- Average Shipping Delay
- Monthly Sales Trend
- Sales by Market
- Sales by Customer Segment
- Shipping Mode Performance
- Product Category Performance

Interactive slicers allow users to explore the data by different business dimensions.

## Key Business Insights

The analysis helped identify:

- Overall sales and profit performance
- Markets contributing the highest sales
- Product categories with strong sales performance
- Monthly sales trends
- Shipping and delivery performance
- Late delivery patterns across shipping modes
- Areas where logistics performance can be improved

## Dashboard

The Power BI dashboard provides an interactive view of supply chain performance and allows users to explore sales and delivery trends.

## Project Structure

```text
Supply-Chain-Logistics-Analysis/
│
├── python/
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── verify_cleaned.py
│   └── prepare_mysql.py
│
├── sql/
│   └── supply_chain_analysis.sql
│
├── powerbi/
│   └── Supply_Chain_Logistics_Performance_Analysis.pbix
│
├── dashboard/
│   └── dashboard_preview.png
│
└── README.md

## Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Python & Pandas
- SQL Querying
- Data Visualization
- Power BI Dashboard Development
- Business Analysis
- Data-driven Decision Making

## Author

**Prawar Karande**

Data Analyst

- LinkedIn: https://www.linkedin.com/in/prawar-karande-b1ab33249
- GitHub: https://github.com/prawar-hash