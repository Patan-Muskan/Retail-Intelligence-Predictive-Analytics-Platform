# 🛒 AI-Powered Retail Intelligence Platform

> Cloud Analytics • Inventory Intelligence • Machine Learning

A full-stack retail analytics dashboard built on AWS, providing real-time KPI monitoring, category-level pricing insights, inventory management, and ML-based price prediction across 11 product categories.

---

## 📸 Screenshots

| Dashboard Overview | Analytics Overview |
|---|---|
| ![Overview](<img width="1838" height="919" alt="Screenshot 2026-05-26 151134" src="https://github.com/user-attachments/assets/0a7e2830-fb8e-4fe3-9040-1d4dcfc35ed0" />
) | ![Analytics](<img width="1464" height="837" alt="Screenshot 2026-05-26 151211" src="https://github.com/user-attachments/assets/b093d824-2d6a-4696-9ecb-a44398419291" />
) |

| Product Insights | ML & Forecasting |
|---|---|
| ![Products](<img width="1432" height="600" alt="Screenshot 2026-05-26 151233" src="https://github.com/user-attachments/assets/ce20f2a5-b1b0-48d0-a1da-7a004be23ec8" />
) | ![ML](<img width="1465" height="841" alt="Screenshot 2026-05-26 151254" src="https://github.com/user-attachments/assets/e45f4f3c-5e58-46ad-adfe-53637a485a69" />
) |

---

## ✨ Features

### 🏠 Overview
- Real-time **KPI cards** — Total Products, Average Price, Average Rating, Low Stock Alerts
- **Date range selector** for time-based filtering
- **Multi-select category filters** (fragrances, home-watches, kitchen-accessories, mobile-accessories, and more)

### 📦 Products
- Full product catalogue with category, rating, and pricing data
- Top-Rated Products ranked by customer satisfaction score

### 🗃️ Inventory
- Live inventory tracking across all product categories
- **Low Stock Alerts** — flags products requiring immediate restocking (97 alerts)

### 📊 Analytics
- **Average Price by Category** — horizontal bar chart across 11 categories
- **Category Distribution** — donut chart showing product share per category
- Price range: $4,626 (fragrances) → $5,844 (ladies)

### 🤖 ML Insights
- **Retail Price Distribution** histogram (price range $0–$10K)
- **Price Prediction Model** with MAE of 82.19 (Status: Good)
- Prediction samples table — actual vs predicted price comparison

### 📋 Reports
- Aggregated reporting view across all modules

---

## 📊 Key Metrics (Sample Data)

| Metric | Value |
|--------|-------|
| Total Products | 9 |
| Average Price | $5,027.60 |
| Average Rating | 4.00 |
| Low Stock Alerts | 97 |
| ML Model MAE | 82.19 |
| ML Model Status | ✅ Good |

---

## 🗂️ Product Categories

`groceries` • `mens-watches` • `mens-shirts` • `fragrances` • `home-watches` • `ladies` • `home-decoration` • `others` • `kitchen-accessories` • `mobile-accessories` • `beauty`

---

## ☁️ AWS Architecture

| Service | Usage |
|---------|-------|
| **AWS S3** | Data lake storage — raw and processed retail dataset files |
| **AWS Athena** | Serverless SQL querying on S3 data for analytics and KPI computation |

> Data flows: Raw data → S3 → Athena SQL queries → Dashboard visualizations

---

## 🧠 ML Model

- **Task:** Retail price prediction
- **Evaluation Metric:** Mean Absolute Error (MAE) = **82.19**
- **Status:** Good
- **Output:** Predicted prices for product input samples

### Prediction Samples

| Input Price | Predicted Price |
|-------------|-----------------|
| $24.95 | $42.23 |
| $8.99 | $32.27 |
| $59.99 | $12.87 |
| $24.99 | $43.81 |
| $38.99 | $43.76 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React / HTML/CSS |
| Charts | Recharts / Chart.js / D3 |
| Cloud Storage | AWS S3 |
| Query Engine | AWS Athena |
| ML Model | Python (scikit-learn / similar) |


## 🗺️ Navigation Pages

| Page | Description |
|------|-------------|
| Overview | KPI dashboard with filters and summary metrics |
| Products | Product catalogue with ratings and pricing |
| Inventory | Stock levels and low-stock alerts |
| Analytics | Price and category distribution charts |
| ML Insights | Price prediction model and distribution analysis |
| Reports | Consolidated reporting across all modules |

---

## 🚀 Getting Started

### Prerequisites

```bash
node >= 16
npm or yarn
python >= 3.8
AWS CLI configured with appropriate IAM permissions
```

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/retail-intelligence-platform.git

# Navigate to the project directory
cd retail-intelligence-platform

# Install dependencies
npm install

# Start the development server
npm start
```

### AWS Setup

```bash
# Configure AWS credentials
aws configure

# Sync data to S3
aws s3 cp ./data/ s3://your-bucket-name/retail-data/ --recursive

# Run Athena queries (update workgroup and output location as needed)
aws athena start-query-execution \
  --query-string "SELECT * FROM retail_products LIMIT 10" \
  --result-configuration OutputLocation=s3://your-bucket-name/athena-results/
```

### Running the ML Model

```bash
cd ml/
pip install -r requirements.txt
python train_model.py
```

---

## 📁 Project Structure

```
retail-intelligence-platform/
├── src/
│   ├── components/
│   │   ├── KPICards/
│   │   ├── Charts/
│   │   ├── ProductInsights/
│   │   ├── Inventory/
│   │   └── MLForecasting/
│   ├── pages/
│   │   ├── Overview.jsx
│   │   ├── Products.jsx
│   │   ├── Inventory.jsx
│   │   ├── Analytics.jsx
│   │   ├── MLInsights.jsx
│   │   └── Reports.jsx
│   └── App.jsx
├── ml/
│   ├── train_model.py
│   └── requirements.txt
├── aws/
│   ├── athena_queries/
│   └── s3_config/
├── public/
└── README.md
```

---

## 🔮 Future Improvements

- [ ] Real-time data streaming with AWS Kinesis
- [ ] Demand forecasting model
- [ ] Anomaly detection for price outliers
- [ ] Export reports as PDF / CSV
- [ ] User authentication with AWS Cognito
- [ ] Mobile responsive design
- [ ] CI/CD pipeline with AWS CodePipeline

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Your Name**
  - GitHub: [@Patan-Muskan](https://github.com/Patan-Muskan)
- LinkedIn: [Patan Muskan](https://linkedin.com/in/patan-muskan-934117333/)
