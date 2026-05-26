"""
Retail Intelligence Platform - Premium Dashboard Application

AI-Powered Retail Intelligence Platform with Cloud Analytics, Inventory Intelligence, and Machine Learning.
Premium, futuristic, and visually impressive dashboard built with Streamlit.

Author: Development Team
Version: 1.0.0
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go


def setup_page():
    """Configure Streamlit page settings with premium dark theme."""
    st.set_page_config(
        page_title="AI-Powered Retail Intelligence Platform",
        page_icon="🛒",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Premium dark theme with glassmorphism and gradients
    st.markdown("""
        <style>
        * {
            margin: 0;
            padding: 0;
        }
        
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1729 100%);
            color: #e0e7ff;
        }
        
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1a1f3a 0%, #0f1729 100%);
            border-right: 1px solid rgba(99, 102, 241, 0.2);
        }
        
        [data-testid="stSidebarNav"] {
            background: transparent;
        }
        
        .main {
            padding: 2rem;
        }
        
        /* Premium Card Styling */
        .premium-card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 41, 0.6) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        
        .premium-card:hover {
            border-color: rgba(99, 102, 241, 0.6);
            box-shadow: 0 12px 48px rgba(99, 102, 241, 0.2);
            transform: translateY(-2px);
        }
        
        /* Metric Cards */
        .metric-card {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(6, 182, 212, 0.05) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 16px;
            padding: 28px;
            box-shadow: 0 8px 32px rgba(99, 102, 241, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .metric-card::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
            border-radius: 50%;
        }
        
        .metric-card:hover {
            border-color: rgba(99, 102, 241, 0.6);
            box-shadow: 0 12px 48px rgba(99, 102, 241, 0.2);
            transform: translateY(-4px);
        }
        
        /* Typography */
        h1 {
            background: linear-gradient(135deg, #e0e7ff 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-size: 3.5rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 0.5rem;
        }
        
        h2 {
            color: #e0e7ff;
            font-size: 1.8rem;
            font-weight: 700;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
            letter-spacing: -0.01em;
        }
        
        h3 {
            color: #c7d2fe;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        
        /* Subtitle */
        .subtitle {
            color: #94a3b8;
            font-size: 1.1rem;
            font-weight: 500;
            letter-spacing: 0.05em;
            margin-bottom: 2rem;
        }
        
        /* Divider */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.3), transparent);
            margin: 2rem 0;
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: transparent;
            border-bottom: 1px solid rgba(99, 102, 241, 0.2);
        }
        
        .stTabs [data-baseweb="tab"] {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.5) 0%, rgba(15, 23, 41, 0.3) 100%);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 12px;
            padding: 12px 24px;
            color: #94a3b8;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.3) 0%, rgba(6, 182, 212, 0.2) 100%);
            border-color: rgba(99, 102, 241, 0.6);
            color: #e0e7ff;
            box-shadow: 0 4px 16px rgba(99, 102, 241, 0.2);
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #6366f1 0%, #06b6d4 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 12px 28px;
            font-weight: 600;
            font-size: 1rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 16px rgba(99, 102, 241, 0.3);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
        }
        
        /* Input Fields */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stMultiSelect > div > div > div {
            background: rgba(30, 41, 59, 0.6);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 12px;
            color: #e0e7ff;
            padding: 12px;
            font-size: 1rem;
        }
        
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div > select:focus {
            border-color: rgba(99, 102, 241, 0.8);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        }
        
        /* Info Box */
        .stInfo {
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 12px;
            padding: 16px;
        }
        
        /* Success Box */
        .stSuccess {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 12px;
        }
        
        /* Dataframe */
        .stDataFrame {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 41, 0.4) 100%);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 12px;
            overflow: hidden;
        }
        
        /* Metric Value */
        .stMetric {
            background: transparent;
        }
        
        .stMetric > div {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(6, 182, 212, 0.08) 100%);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 32px rgba(99, 102, 241, 0.1);
        }
        
        .stMetric > div:first-child {
            color: #94a3b8;
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        .stMetric > div:nth-child(2) {
            color: #e0e7ff;
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #e0e7ff 0%, #06b6d4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* Sidebar Navigation */
        .sidebar-nav {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .nav-item {
            padding: 12px 16px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            color: #94a3b8;
            font-weight: 600;
        }
        
        .nav-item:hover {
            background: rgba(99, 102, 241, 0.2);
            color: #e0e7ff;
        }
        
        .nav-item.active {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.3) 0%, rgba(6, 182, 212, 0.2) 100%);
            color: #e0e7ff;
            border-left: 3px solid #6366f1;
        }
        
        /* Spacer */
        .spacer {
            height: 2rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            color: #64748b;
            font-size: 0.85rem;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(99, 102, 241, 0.1);
        }
        </style>
    """, unsafe_allow_html=True)


def load_sample_data():
    """Load sample data for dashboard."""
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-05-24', freq='D')
    
    categories = ['kitchen-accessories', 'groceries', 'home-watches', 'beauty', 'fragrances', 'furniture', 'home-decoration', 'ladies', 'others', 'mens-shirts', 'mens-watches', 'mobile-accessories']
    products = ['Amazon Echo Plus', 'Smart Headset Pro', 'Rolex Calibre Dials Black Dial', 'Water', 'Eggs', 'Delco Shine Eau de', 'Wooden Sofa With Mirror', 'Apple', 'Cooking Oil']
    
    data = {
        'date': np.random.choice(dates, 500),
        'product_name': np.random.choice(products, 500),
        'category': np.random.choice(categories, 500),
        'price': np.random.uniform(50, 10000, 500),
        'quantity_sold': np.random.randint(1, 100, 500),
        'competitor_price': np.random.uniform(50, 10000, 500),
        'rating': np.random.uniform(3.0, 5.0, 500),
        'reviews': np.random.randint(10, 1000, 500),
        'stock': np.random.randint(0, 100, 500)
    }
    
    return pd.DataFrame(data)


def render_sidebar(df):
    """Render sidebar with navigation and filters."""
    with st.sidebar:
        st.markdown("### 🛒 Retail Intelligence Platform")
        st.divider()
        
        # Navigation
        st.markdown("**NAVIGATION**")
        page = st.radio(
            "Select View",
            ["Overview", "Products", "Inventory", "Analytics", "ML Insights", "Reports"],
            label_visibility="collapsed"
        )
        
        st.divider()
        
        # Filters
        st.markdown("**FILTERS**")
        
        selected_categories = st.multiselect(
            "Select Categories",
            options=df['category'].unique(),
            default=df['category'].unique()[:3],
            key="category_filter"
        )
        
        date_range = st.date_input(
            "Select Date Range",
            value=(df['date'].min().date(), df['date'].max().date()),
            max_value=df['date'].max().date()
        )
        
        st.divider()
        
        # Cloud info
        st.markdown("**Cloud Powered**")
        st.info("AWS • Athena • Python")
        
        return page, selected_categories, date_range


def render_header():
    """Render premium dashboard header."""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("# AI-Powered Retail Intelligence Platform")
        st.markdown('<p class="subtitle">Cloud Analytics • Inventory Intelligence • Machine Learning</p>', unsafe_allow_html=True)
    
    with col2:
        date_range_display = st.selectbox(
            "Date Range",
            ["May 24, 2026 - May 24, 2026", "Last 7 days", "Last 30 days", "Last 90 days"],
            label_visibility="collapsed"
        )


def render_kpis(df):
    """Render premium key performance indicators."""
    col1, col2, col3, col4 = st.columns(4, gap="large")
    
    with col1:
        total_products = df['product_name'].nunique()
        st.metric("Total Products", f"{total_products}", "All active products")
    
    with col2:
        avg_price = df['price'].mean()
        st.metric("Average Price", f"${avg_price:.2f}", "Across all products")
    
    with col3:
        avg_rating = df['rating'].mean()
        st.metric("Average Rating", f"{avg_rating:.2f}", "Customer satisfaction")
    
    with col4:
        low_stock = (df['stock'] < 20).sum()
        st.metric("Low Stock Alerts", f"{low_stock}", "Requires attention")


def render_price_by_category(df):
    """Render average price by category chart."""
    price_by_cat = df.groupby('category')['price'].mean().sort_values(ascending=False).head(10)
    
    fig = go.Figure(data=[
        go.Bar(
            x=price_by_cat.values,
            y=price_by_cat.index,
            orientation='h',
            marker=dict(
                color=price_by_cat.values,
                colorscale='Viridis',
                showscale=False
            ),
            text=[f'${v:.0f}' for v in price_by_cat.values],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Average Price by Category",
        xaxis_title="Price ($)",
        yaxis_title="Category",
        template="plotly_dark",
        height=400,
        margin=dict(l=150, r=20, t=60, b=20),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff', size=12)
    )
    
    return fig


def render_category_distribution(df):
    """Render category distribution pie chart."""
    cat_dist = df['category'].value_counts()
    
    fig = go.Figure(data=[
        go.Pie(
            labels=cat_dist.index,
            values=cat_dist.values,
            hole=0.4,
            marker=dict(
                colors=['#6366f1', '#06b6d4', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#ec4899', '#14b8a6', '#f97316', '#6b7280']
            ),
            textposition='inside',
            textinfo='label+percent'
        )
    ])
    
    fig.update_layout(
        title="Category Distribution",
        template="plotly_dark",
        height=400,
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff', size=12),
        legend=dict(x=1.05, y=1)
    )
    
    return fig


def render_top_rated_products(df):
    """Render top rated products table."""
    top_products = df.nlargest(5, 'rating')[['product_name', 'category', 'rating', 'price', 'stock']]
    top_products = top_products.reset_index(drop=True)
    top_products.index = top_products.index + 1
    top_products.index.name = '#'
    
    return top_products


def render_low_stock_alerts(df):
    """Render low stock alerts table."""
    low_stock = df[df['stock'] < 20].nlargest(5, 'price')[['product_name', 'category', 'stock', 'price']]
    low_stock = low_stock.reset_index(drop=True)
    low_stock.index = low_stock.index + 1
    low_stock.index.name = '#'
    
    return low_stock


def render_price_distribution(df):
    """Render retail price distribution histogram."""
    fig = go.Figure(data=[
        go.Histogram(
            x=df['price'],
            nbinsx=30,
            marker=dict(color='#06b6d4'),
            name='Price Distribution'
        )
    ])
    
    fig.update_layout(
        title="Retail Price Distribution",
        xaxis_title="Price ($)",
        yaxis_title="Count",
        template="plotly_dark",
        height=400,
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e7ff', size=12)
    )
    
    return fig


def render_ml_price_prediction(df):
    """Render ML price prediction section."""
    mae = 82.19
    model_status = "Good"
    
    prediction_samples = pd.DataFrame({
        'Prediction Samples': ['$24.95', '$8.99', '$59.99', '$24.99', '$38.99'],
        'Predicted Price': ['$42.23', '$32.27', '$12.87', '$43.81', '$43.76']
    })
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("**Model Performance**")
        st.markdown(f"**MAE (Mean Absolute Error)**")
        st.markdown(f"# {mae}")
        st.markdown(f"Status: <span style='color: #10b981;'>● {model_status}</span>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Prediction Samples**")
        st.dataframe(prediction_samples, use_container_width=True, hide_index=True)


def render_overview_page(df):
    """Render overview page with proper spacing and layout."""
    st.divider()
    
    # KPIs - Full width
    st.markdown("### Key Performance Indicators")
    render_kpis(df)
    
    st.markdown("")
    st.divider()
    st.markdown("")
    
    # Charts section
    st.markdown("### Analytics Overview")
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("#### Average Price by Category")
        st.plotly_chart(render_price_by_category(df), use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        st.markdown("#### Category Distribution")
        st.plotly_chart(render_category_distribution(df), use_container_width=True, config={'displayModeBar': False})
    
    st.markdown("")
    st.divider()
    st.markdown("")
    
    # Tables section
    st.markdown("### Product Insights")
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("#### Top Rated Products")
        st.dataframe(render_top_rated_products(df), use_container_width=True)
    
    with col2:
        st.markdown("#### Low Stock Alerts")
        st.dataframe(render_low_stock_alerts(df), use_container_width=True)
    
    st.markdown("")
    st.divider()
    st.markdown("")
    
    # ML Section
    st.markdown("### Machine Learning & Forecasting")
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("#### Retail Price Distribution")
        st.plotly_chart(render_price_distribution(df), use_container_width=True, config={'displayModeBar': False})
    
    with col2:
        st.markdown("#### 🤖 Price Prediction Model")
        render_ml_price_prediction(df)


def render_products_page(df):
    """Render products page."""
    st.divider()
    st.markdown("### Products Inventory")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        search = st.text_input("Search products", "")
    with col2:
        sort_by = st.selectbox("Sort by", ["Name", "Price", "Rating", "Stock"])
    with col3:
        st.write("")
    
    filtered_df = df.copy()
    if search:
        filtered_df = filtered_df[filtered_df['product_name'].str.contains(search, case=False)]
    
    st.dataframe(filtered_df[['product_name', 'category', 'price', 'rating', 'stock']], use_container_width=True)


def render_inventory_page(df):
    """Render inventory page."""
    st.divider()
    st.markdown("### Inventory Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Stock Units", df['stock'].sum())
    with col2:
        st.metric("Average Stock per Product", f"{df['stock'].mean():.0f}")
    
    st.divider()
    
    low_stock_df = df[df['stock'] < 20].sort_values('stock')
    st.markdown("### ⚠️ Low Stock Items")
    st.dataframe(low_stock_df[['product_name', 'category', 'stock', 'price']], use_container_width=True)


def render_analytics_page(df):
    """Render analytics page."""
    st.divider()
    st.markdown("### Analytics Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(render_price_by_category(df), use_container_width=True)
    
    with col2:
        st.plotly_chart(render_category_distribution(df), use_container_width=True)
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(render_price_distribution(df), use_container_width=True)
    
    with col2:
        # Rating distribution
        fig = go.Figure(data=[
            go.Histogram(
                x=df['rating'],
                nbinsx=20,
                marker=dict(color='#10b981'),
                name='Rating Distribution'
            )
        ])
        fig.update_layout(
            title="Rating Distribution",
            xaxis_title="Rating",
            yaxis_title="Count",
            template="plotly_dark",
            height=400,
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e7ff', size=12)
        )
        st.plotly_chart(fig, use_container_width=True)


def render_ml_page(df):
    """Render ML Insights page."""
    st.divider()
    st.markdown("### 🤖 Machine Learning Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Price Prediction Model")
        render_ml_price_prediction(df)
    
    with col2:
        st.markdown("### Demand Forecasting")
        st.info("Forecasting demand trends for next 30 days using Prophet model")
        
        # Simulated forecast data
        forecast_data = pd.DataFrame({
            'Date': pd.date_range('2024-05-25', periods=30),
            'Forecast': np.random.uniform(50, 200, 30)
        })
        
        fig = px.line(forecast_data, x='Date', y='Forecast', title='30-Day Demand Forecast')
        fig.update_layout(
            template="plotly_dark",
            height=400,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0e7ff', size=12)
        )
        st.plotly_chart(fig, use_container_width=True)


def render_reports_page(df):
    """Render reports page."""
    st.divider()
    st.markdown("### Reports & Exports")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Generate Daily Report"):
            st.success("Daily report generated successfully!")
    
    with col2:
        if st.button("📈 Generate Weekly Report"):
            st.success("Weekly report generated successfully!")
    
    with col3:
        if st.button("📉 Generate Monthly Report"):
            st.success("Monthly report generated successfully!")
    
    st.divider()
    
    # Export data
    st.markdown("### Export Data")
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name=f"retail_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )


def main():
    """Main application entry point."""
    setup_page()
    
    # Load data
    df = load_sample_data()
    
    # Render sidebar
    page, selected_categories, date_range = render_sidebar(df)
    
    # Filter data
    df_filtered = df[
        (df['category'].isin(selected_categories)) &
        (df['date'].dt.date >= date_range[0]) &
        (df['date'].dt.date <= date_range[1])
    ]
    
    # Render header
    render_header()
    
    # Render selected page
    if page == "Overview":
        render_overview_page(df_filtered)
    elif page == "Products":
        render_products_page(df_filtered)
    elif page == "Inventory":
        render_inventory_page(df_filtered)
    elif page == "Analytics":
        render_analytics_page(df_filtered)
    elif page == "ML Insights":
        render_ml_page(df_filtered)
    elif page == "Reports":
        render_reports_page(df_filtered)
    
    # Footer
    st.divider()
    st.markdown(
        f"""
        <div class="footer">
        Retail Intelligence Platform © 2024 | Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
