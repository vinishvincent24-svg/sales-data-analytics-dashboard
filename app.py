
import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load Dataset
data = pd.read_csv("data/cleaned_sales.csv")
data["Order Date"] = pd.to_datetime(data["Order Date"])

# Dashboard Title
st.title("📊 Sales Data Analytics Dashboard")
st.markdown("### Superstore Sales Performance Analysis")
st.divider()

# Sidebar Filters
st.sidebar.title("Filter Options")

regions = ["All"] + sorted(data["Region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Select Region", regions)

categories = ["All"] + sorted(data["Category"].dropna().unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

# Date Range Filter
st.sidebar.subheader("Date Filter")

min_date = data["Order Date"].min().date()
max_date = data["Order Date"].max().date()

start_date = st.sidebar.date_input(
    "Start Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date
)

end_date = st.sidebar.date_input(
    "End Date",
    value=max_date,
    min_value=min_date,
    max_value=max_date
)

# Welcome Screen
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    st.markdown("""
    <style>
    .welcome-box {
        text-align: center;
        padding: 60px 20px;
        border-radius: 25px;
        background: linear-gradient(135deg, #241044, #10172F, #071C35);
        border: 2px solid #8B5CF6;
        box-shadow: 0 0 30px rgba(139, 92, 246, 0.3);
    }
    .welcome-title {
        font-size: 42px;
        font-weight: bold;
        color: #C4B5FD;
    }
    .welcome-subtitle {
        font-size: 23px;
        color: #54E8FF;
    }
    .welcome-description {
        font-size: 17px;
        color: white;
        line-height: 2;
    }
    </style>
    <div class="welcome-box"><h1 class="welcome-title">📊 SALES ANALYTICS</h1><p class="welcome-subtitle">Welcome to Your Business Dashboard</p><p class="welcome-description">Explore your sales performance.<br>Discover valuable business insights.<br>Make smarter data-driven decisions.</p><p style="color:#A78BFA;">ANALYZE • EXPLORE • GROW</p></div>
    """, unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🚀 GET STARTED", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.stop()

# Back to Welcome Screen
if st.sidebar.button("🏠 Back to Home"):
    st.session_state.started = False
    st.rerun()

# Welcome Screen
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    st.markdown("""
    <style>
    .welcome-box {
        text-align: center;
        padding: 65px 20px;
        border-radius: 25px;
        background: linear-gradient(135deg, #241044, #10172F, #071C35);
        border: 1px solid #8B5CF6;
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.25);
    }

    .welcome-title {
        font-size: 45px;
        font-weight: bold;
        color: #C4B5FD;
    }

    .welcome-subtitle {
        font-size: 22px;
        color: #54E8FF;
    }

    .welcome-description {
        font-size: 17px;
        color: #E2E8F0;
        line-height: 1.8;
    }
    </style>

    <div class="welcome-box">
        <div class="welcome-title">
            📊 SALES ANALYTICS
        </div>

        <div class="welcome-subtitle">
            Welcome to Your Business Dashboard
        </div>

        <br>

        <div class="welcome-description">
            Explore your sales performance.<br>
            Discover valuable business insights.<br>
            Make smarter data-driven decisions.
        </div>

        <br>

        <p style="color:#A78BFA;">
            ANALYZE • EXPLORE • GROW
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🚀 GET STARTED", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.stop()

# Welcome Screen
if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    st.markdown(
        "<h1 style='text-align:center; color:#A78BFA;'>"
        "Welcome to Sales Analytics Dashboard 📊"
        "</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='text-align:center;'>"
        "Discover Your Business Performance"
        "</h3>",
        unsafe_allow_html=True
    )

    st.write("")

    st.markdown(
        "<p style='text-align:center; font-size:18px;'>"
        "Analyze sales, explore business insights, "
        "track performance and make smarter decisions."
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.stop()

# Filter Dataset
filtered_data = data.copy()

if start_date > end_date:
    st.sidebar.error("Start Date must be before End Date")
    filtered_data = filtered_data.iloc[0:0]
else:
    filtered_data = filtered_data[
        (filtered_data["Order Date"].dt.date >= start_date) &
        (filtered_data["Order Date"].dt.date <= end_date)
    ]

if selected_region != "All":
    filtered_data = filtered_data[
        filtered_data["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_data = filtered_data[
        filtered_data["Category"] == selected_category
    ]

# KPI Metrics
total_sales = filtered_data["Sales"].sum()
total_orders = filtered_data["Order ID"].nunique()
total_customers = filtered_data["Customer ID"].nunique()

average_order = (
    total_sales / total_orders if total_orders > 0 else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📦 Total Orders", f"{total_orders:,}")
col3.metric("👥 Total Customers", f"{total_customers:,}")
col4.metric("🛒 Average Order Value", f"${average_order:,.2f}")

st.divider()

# Sales by Category
st.subheader("📊 Sales by Category")

category_sales = (
    filtered_data.groupby("Category", as_index=False)["Sales"].sum()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Category-wise Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# Sales by Region
st.subheader("🌍 Sales by Region")

region_sales = (
    filtered_data.groupby("Region", as_index=False)["Sales"].sum()
)

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Region-wise Sales Distribution",
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")

monthly_data = filtered_data.copy()

monthly_data["Month"] = (
    monthly_data["Order Date"].dt.to_period("M").astype(str)
)

monthly_sales = (
    monthly_data.groupby("Month", as_index=False)["Sales"].sum()
)

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Top 10 Best-Selling Products
st.subheader("🏆 Top 10 Best-Selling Products")

top_products = (
    filtered_data.groupby("Product Name")["Sales"]
    .sum()
    .nlargest(10)
    .reset_index()
    .sort_values("Sales", ascending=True)
)

fig4 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales",
    color="Sales",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig4, use_container_width=True)

# Sales by Sub-Category
st.subheader("📦 Sales by Sub-Category")

subcategory_sales = (
    filtered_data.groupby("Sub-Category", as_index=False)["Sales"]
    .sum()
    .sort_values("Sales", ascending=False)
)

fig5 = px.bar(
    subcategory_sales,
    x="Sales",
    y="Sub-Category",
    orientation="h",
    title="Sub-Category Sales Performance",
    color="Sales",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig5, use_container_width=True)

# Sales Data Table
st.subheader("📋 Sales Records")

st.dataframe(filtered_data, use_container_width=True)

# Download Button
csv = filtered_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Sales Data",
    data=csv,
    file_name="filtered_sales.csv",
    mime="text/csv"
)

st.success("Sales Dashboard Loaded Successfully!")
