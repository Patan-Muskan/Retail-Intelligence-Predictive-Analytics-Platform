import requests
import pandas as pd
from datetime import datetime
import os

# Store product data
all_products = []

# API URL
url = "https://dummyjson.com/products?limit=100"

# Fetch live data
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Extract products
products = data["products"]

# Process each product
for product in products:

    all_products.append({

        "Product_ID": product.get("id"),

        "Product_Name": product.get("title"),

        "Category": product.get("category"),

        "Brand": product.get("brand", "Unknown"),

        "Price": product.get("price"),

        "Discount_Percentage": product.get("discountPercentage"),

        "Rating": product.get("rating"),

        "Stock": product.get("stock"),

        "Timestamp": datetime.now()

    })

# Create dataframe
df = pd.DataFrame(all_products)

# Historical file path
file_path = (
    "Retail-Intelligence-Platform/"
    "data/historical/live_products_history.csv"
)

# Append historical data if file exists
if os.path.exists(file_path):

    existing_df = pd.read_csv(file_path)

    combined_df = pd.concat(
        [existing_df, df],
        ignore_index=True
    )

    # Remove duplicates
    combined_df.drop_duplicates(
    subset=[
        "Product_ID",
        "Price",
        "Stock"
    ],
    inplace=True
)

    # Save updated dataset
    combined_df.to_csv(
        file_path,
        index=False
    )

    final_df = combined_df

else:

    # Create new historical dataset
    df.to_csv(
        file_path,
        index=False
    )

    final_df = df

# Display sample rows
print(final_df.head())

# Display dataset size
print("\nFinal Dataset Shape:", final_df.shape)

print("\nHistorical live retail ingestion completed successfully!")