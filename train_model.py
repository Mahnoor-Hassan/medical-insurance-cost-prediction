import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("insurance.csv")

# Remove duplicates
df = df.drop_duplicates()

# Encode categorical variables
df_encoded = pd.get_dummies(
    df,
    columns=["sex", "smoker", "region"],
    drop_first=True,
    dtype=int
)

# Separate features and target
X = df_encoded.drop("charges", axis=1)
y = df_encoded["charges"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "insurance_model.pkl")

print("New model trained and saved successfully!")