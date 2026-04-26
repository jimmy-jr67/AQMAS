import pandas as pd

class FileHandler:
    def __init__(self, filename="data/air_quality.csv"):
        self.filename = filename

    def save_to_csv(self, data):
        if not data:
            print("No data to save.")
            return
        df = pd.DataFrame(data)
        df.to_csv(self.filename, index=False)
        print(f"Data saved to {self.filename}")

    def load_as_dataframe(self):
        try:
            df = pd.read_csv(self.filename)
            print("\n--- STORED DATA ---")
            print(df)
            return df
        except FileNotFoundError:
            print("File not found! Save data first.")
            return None