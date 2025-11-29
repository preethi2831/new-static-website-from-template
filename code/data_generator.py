```
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_synthetic_data(n_samples=1000):
    np.random.seed(42)

    train_names = ["Express", "Superfast", "Local", "Intercity"]
    sources = ["Chennai", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
    destinations = ["Chennai", "Mumbai", "Delhi", "Bangalore", "Hyderabad"]
    weather_conditions = ["Clear", "Rain", "Fog", "Storm"]

    data = []
    start_date = datetime(2024, 1, 1)

    for _ in range(n_samples):
        train = np.random.choice(train_names)
        source = np.random.choice(sources)
        dest = np.random.choice(destinations)

        dep_time = start_date + timedelta(minutes=np.random.randint(0, 1440))
        weather = np.random.choice(weather_conditions)

        congestion = np.random.randint(1, 11)
        maintenance = np.random.randint(0, 2)
        delay = np.random.randint(-5, 120)

        data.append([train, source, dest, dep_time, weather, congestion, maintenance, delay])

    df = pd.DataFrame(data, columns=[
        "train_name", "source", "destination", "scheduled_dep_time",
        "weather", "congestion_level", "maintenance_issue", "delay_minutes"
    ])

    df["scheduled_dep_hour"] = df["scheduled_dep_time"].dt.hour
    return df

def export_dataset(df):
    df.to_csv("data/train_delay_synthetic_data.csv", index=False)
    print("✔ Dataset exported as train_delay_synthetic_data.csv")
```
