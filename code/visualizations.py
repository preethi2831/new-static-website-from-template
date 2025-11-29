```
import matplotlib.pyplot as plt

def generate_graphs(df):
    print("\n✔ Generating graphs...")

    # Weather vs Delay
    df.groupby("weather")["delay_minutes"].mean().plot(kind="bar")
    plt.title("Weather vs Average Delay")
    plt.xlabel("Weather")
    plt.ylabel("Average Delay (min)")
    plt.savefig("images/weather_vs_delay.png")
    plt.show()

    # Congestion vs Delay
    plt.scatter(df["congestion_level"], df["delay_minutes"])
    plt.title("Congestion Level vs Delay")
    plt.xlabel("Congestion Level")
    plt.ylabel("Delay (min)")
    plt.savefig("images/congestion_vs_delay.png")
    plt.show()

    # Hour vs Delay
    df.groupby("scheduled_dep_hour")["delay_minutes"].mean().plot()
    plt.title("Hour of Day vs Delay")
    plt.xlabel("Hour")
    plt.ylabel("Average Delay (min)")
    plt.savefig("images/hour_vs_delay.png")
    plt.show()

def print_feature_description():
    print("""
FEATURE DESCRIPTION:
train_name: Type of train
source: Start station
destination: End station
scheduled_dep_time: Planned departure
weather: Weather condition
congestion_level: Congestion scale (1–10)
maintenance_issue: Maintenance (0/1)
scheduled_dep_hour: Extracted hour
delay_minutes: Target delay value
""")
```
