import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd

def build_and_train_model(X, y):

    categorical = ["train_name", "source", "destination", "weather"]
    numeric = ["congestion_level", "maintenance_issue", "scheduled_dep_hour"]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ("num", "passthrough", numeric)
    ])

    model = XGBRegressor(
        objective="reg:squarederror",
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5
    )

    pipeline = Pipeline([
        ("preprocess", preprocessor),
        ("model", model)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    print("\nMODEL PERFORMANCE")
    print("MAE :", mean_absolute_error(y_test, predictions))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, predictions)))
    print("R2  :", r2_score(y_test, predictions))

    return pipeline

def sample_predictions(model):
    sample = pd.DataFrame({
        "train_name": ["Express"],
        "source": ["Chennai"],
        "destination": ["Mumbai"],
        "weather": ["Rain"],
        "congestion_level": [7],
        "maintenance_issue": [0],
        "scheduled_dep_hour": [15]
    })

    print("\nSAMPLE INPUT:")
    print(sample)

    pred = model.predict(sample)[0]
    print("\nPredicted Delay:", round(pred, 2), "minutes")

