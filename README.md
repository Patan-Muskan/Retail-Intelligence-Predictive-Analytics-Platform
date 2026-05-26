# Retail-Intelligence-Predictive-Analytics-Platform

A modern retail analytics and machine learning platform built using Python, Streamlit, Plotly, Scikit-learn, SQL, and AWS concepts to analyze retail product data, monitor inventory risks, and generate predictive business insights through an interactive dashboard.

Overview

This project focuses on building an end-to-end retail intelligence solution that combines:

Retail analytics
Inventory monitoring
Interactive business dashboards
Machine learning-based price prediction
Forecasting and KPI tracking

The platform simulates enterprise retail analytics workflows by integrating data processing, visualization, cloud analytics concepts, and predictive modeling into a single dashboard application.

Features
Retail Analytics Dashboard
Category-wise pricing analysis
Product rating insights
Inventory tracking
KPI monitoring
Interactive filters and charts
Inventory Intelligence
Low-stock product detection
Inventory risk analysis
Product availability monitoring
Machine Learning
Retail price prediction using Random Forest Regression
Forecasting insights
Model evaluation using MAE
Data Visualization
Interactive Plotly charts
Category distribution analysis
Price trend analysis
Retail performance insights
Cloud Analytics Workflow
AWS S3 integration concepts
AWS Athena SQL querying
Structured retail dataset analysis
Tech Stack
Languages & Libraries
Python
Pandas
NumPy
Scikit-learn
Dashboard & Visualization
Streamlit
Plotly
Cloud & Analytics
AWS S3
AWS Athena
SQL
Dashboard Preview

The dashboard includes:

KPI cards
Inventory alerts
Forecasting insights
Retail analytics visualizations
Machine learning prediction outputs
Interactive category filters
Machine Learning Model

Implemented a Random Forest Regressor model for retail price prediction using:

Product categories
Brand features
Inventory-related attributes
Model Performance
Mean Absolute Error (MAE): 82.19
Project Structure
Retail-Intelligence-Platform/
│
├── dashboards/
│   └── app.py
│
├── data/
│   └── historical/
│       └── live_products_history.csv
│
├── ml/
│   └── price_prediction.py
│
├── scripts/
│   └── ingestion/
│       └── live_product_ingestion.py
│
├── notebooks/

Mean Absolute Error (MAE): 82.19
AWS Integration

Integrated AWS cloud services to simulate enterprise-scale analytics workflows:

AWS S3 for retail dataset storage
AWS Athena for SQL-based analytics querying
