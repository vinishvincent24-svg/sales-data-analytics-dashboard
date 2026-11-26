
import pandas as pd

# Load sales dataset
data = pd.read_csv("data/train.csv")

# Display first 5 rows
print("SALES DATASET")
print(data.head())

# Dataset information
print("\nDATASET SHAPE:")
print(data.shape)

print("\nCOLUMN NAMES:")
print(data.columns.tolist())

print("\nDATASET INFORMATION:")
data.info()

import pandas as pd

# Load dataset
data = pd.read_csv("data/train.csv")

# Convert date columns
data["Order Date"] = pd.to_datetime(
    data["Order Date"], format="mixed", dayfirst=True
)

data["Ship Date"] = pd.to_datetime(
    data["Ship Date"], format="mixed", dayfirst=True
)

# Check missing values
print("MISSING VALUES:")
print(data.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS:")
print(data.duplicated().sum())

# Remove duplicate records
data = data.drop_duplicates()

# Check final dataset
print("\nCLEANED DATASET SHAPE:")
print(data.shape)

print("\nDATA TYPES:")
print(data.dtypes)

# Save cleaned dataset
data.to_csv("data/cleaned_sales.csv", index=False)

print("\nDATA CLEANING COMPLETED!")

# SALES DATA ANALYSIS

print("\n========== SALES ANALYSIS ==========")

# 1. Total Sales
total_sales = data["Sales"].sum()
print("Total Sales:", round(total_sales, 2))

# 2. Total Orders
total_orders = data["Order ID"].nunique()
print("Total Orders:", total_orders)

# 3. Total Customers
total_customers = data["Customer ID"].nunique()
print("Total Customers:", total_customers)

# 4. Average Order Value
average_order = total_sales / total_orders
print("Average Order Value:", round(average_order, 2))

# 5. Sales by Category
print("\nSALES BY CATEGORY:")
print(data.groupby("Category")["Sales"].sum())

# 6. Sales by Region
print("\nSALES BY REGION:")
print(data.groupby("Region")["Sales"].sum())

import matplotlib.pyplot as plt
import seaborn as sns

# Create images folder if needed
import os
os.makedirs("images", exist_ok=True)

# 1. Sales by Category
plt.figure(figsize=(8, 5))
data.groupby("Category")["Sales"].sum().plot(
    kind="bar", color="skyblue"
)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("images/sales_by_category.png")
plt.close()

# 2. Sales by Region
plt.figure(figsize=(8, 5))
data.groupby("Region")["Sales"].sum().plot(
    kind="bar", color="orange"
)
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("images/sales_by_region.png")
plt.close()

# 3. Monthly Sales Trend
data["Month"] = data["Order Date"].dt.to_period("M")
monthly_sales = data.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/monthly_sales_trend.png")
plt.close()

print("\n3 GRAPHS CREATED SUCCESSFULLY!")

import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load cleaned data
data = pd.read_csv("data/cleaned_sales.csv")
data["Order Date"] = pd.to_datetime(data["Order Date"])

# Title
st.title("📊 Sales Data Analytics Dashboard")
st.markdown("### Interactive Superstore Sales Analysis")

# Sidebar filters
st.sidebar.header("Filter Options")

regions = ["All"] + sorted(data["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

categories = ["All"] + sorted(data["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

filtered_data = data.copy()

if selected_region != "All":
    filtered_data = filtered_data[
        filtered_data["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_data = filtered_data[
        filtered_data["Category"] == selected_category
    ]

# KPI metrics
total_sales = filtered_data["Sales"].sum()
total_orders = filtered_data["Order ID"].nunique()
total_customers = filtered_data["Customer ID"].nunique()
average_order = total_sales / total_orders if total_orders else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Total Customers", f"{total_customers:,}")
col4.metric("Average Order Value", f"${average_order:,.2f}")

# Sales by Category
st.subheader("Sales by Category")
category_sales = filtered_data.groupby("Category", as_index=False)["Sales"].sum()
fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Category-wise Sales"
)
st.plotly_chart(fig1, use_container_width=True)

# Sales by Region
st.subheader("Sales by Region")
region_sales = filtered_data.groupby("Region", as_index=False)["Sales"].sum()
fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Region-wise Sales Distribution"
)
st.plotly_chart(fig2, use_container_width=True)

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")
monthly_data = filtered_data.copy()
monthly_data["Month"] = monthly_data["Order Date"].dt.to_period("M").astype(str)
monthly_sales = monthly_data.groupby("Month", as_index=False)["Sales"].sum()

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)
st.plotly_chart(fig3, use_container_width=True)

# Data table
st.subheader("Sales Data")
st.dataframe(filtered_data, use_container_width=True)

# Download filtered data
csv = filtered_data.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Filtered Data",
    csv,
    "filtered_sales.csv",
    "text/csv"
)


