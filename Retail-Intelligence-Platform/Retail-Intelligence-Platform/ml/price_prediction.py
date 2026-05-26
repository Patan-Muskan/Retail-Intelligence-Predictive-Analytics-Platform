import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error


# -----------------------------
# LOAD DATA
# -----------------------------

df = pd.read_csv(
    "Retail-Intelligence-Platform/data/historical/live_products_history.csv"
)

print("\nDataset Loaded Successfully!")

print(df.head())


# -----------------------------
# DATA PREPROCESSING
# -----------------------------

# Convert categorical columns
df_encoded = pd.get_dummies(
    df,
    columns=["Category", "Brand"]
)

# Features
X = df_encoded.drop(
    columns=[
        "Price",
        "Product_Name",
        "Timestamp"
    ],
    errors="ignore"
)

# Target
y = df_encoded["Price"]


# -----------------------------
# TRAIN TEST SPLIT
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# -----------------------------
# MODEL
# -----------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# -----------------------------
# TRAIN MODEL
# -----------------------------

model.fit(
    X_train,
    y_train
)

print("\nModel Training Completed!")


# -----------------------------
# PREDICTIONS
# -----------------------------

predictions = model.predict(X_test)


# -----------------------------
# EVALUATION
# -----------------------------

mae = mean_absolute_error(
    y_test,
    predictions
)

print("\nMean Absolute Error:", round(mae, 2))


# -----------------------------
# RESULTS
# -----------------------------

results = pd.DataFrame({

    "Actual_Price": y_test.values,

    "Predicted_Price": predictions

})

print("\nPrediction Samples:\n")

print(results.head(10))