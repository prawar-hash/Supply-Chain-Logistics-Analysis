CREATE DATABASE IF NOT EXISTS supply_chain_analysis;

USE supply_chain_analysis;

CREATE TABLE IF NOT EXISTS supply_chain_orders (
    order_item_id INT PRIMARY KEY,

    transaction_type VARCHAR(20),
    days_for_shipping_real INT,
    days_for_shipment_scheduled INT,

    delivery_status VARCHAR(30),
    late_delivery_risk TINYINT,

    category_id INT,
    category_name VARCHAR(100),

    customer_segment VARCHAR(50),

    department_id INT,
    department_name VARCHAR(100),

    market VARCHAR(50),

    order_city VARCHAR(100),
    order_country VARCHAR(100),
    order_customer_id INT,

    order_id INT,

    order_item_discount DECIMAL(12,2),
    order_item_discount_rate DECIMAL(8,4),

    order_item_product_price DECIMAL(12,2),
    order_item_profit_ratio DECIMAL(8,4),
    order_item_quantity INT,

    sales DECIMAL(14,2),
    order_item_total DECIMAL(14,2),

    order_region VARCHAR(100),
    order_state VARCHAR(100),
    order_status VARCHAR(50),

    product_card_id INT,
    product_category_id INT,
    product_name VARCHAR(150),
    product_price DECIMAL(12,2),
    product_status TINYINT,

    shipping_mode VARCHAR(50),

    order_date DATETIME,
    shipping_date DATETIME,

    shipping_delay INT,

    order_year INT,
    order_month INT,
    order_month_name VARCHAR(20),
    order_year_month CHAR(7),

    INDEX idx_order_id (order_id),
    INDEX idx_order_date (order_date),
    INDEX idx_delivery_status (delivery_status),
    INDEX idx_shipping_mode (shipping_mode),
    INDEX idx_market (market),
    INDEX idx_category_name (category_name),
    INDEX idx_order_status (order_status)
);