import matplotlib.pyplot as plt

class AQIVisualizer:
    def plot_trends(self, df):
        if df is None: return
        try:
            df.plot(x="Date", y=["PM2.5", "PM10"], kind="line", title="Pollution Trends")
            plt.show()
        except KeyError:
            print("Missing required columns in data.")

    def plot_categories(self, df):
        if df is None: return
        try:
            df['Category'].value_counts().plot(kind='bar', color=['green', 'yellow', 'red'])
            plt.title("AQI Category Breakdown")
            plt.show()
        except KeyError:
            print("Missing required columns in data.")