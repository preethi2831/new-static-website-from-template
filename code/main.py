```
from data_generator import generate_synthetic_data, export_dataset
from visualizations import generate_graphs, print_feature_description
from features import feature_engineering
from model import build_and_train_model, sample_predictions

def main():
    print("✔ Generating dataset...")
    df = generate_synthetic_data()

    print("\nSAMPLE ROWS:")
    print(df.head())

    export_dataset(df)
    print_feature_description()
    generate_graphs(df)

    X, y = feature_engineering(df)
    model = build_and_train_model(X, y)

    sample_predictions(model)

if __name__ == "__main__":
    main()
```
