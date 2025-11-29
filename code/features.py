```
def feature_engineering(df):
    X = df[[
        "train_name", "source", "destination", "weather",
        "congestion_level", "maintenance_issue", "scheduled_dep_hour"
    ]]
    y = df["delay_minutes"]
    return X, y
```
