class AQIAnalytics:
    def calculate_summary(self, df):
        if df is None: return "No data available."
        try:
            return df[['CO2', 'PM2.5', 'PM10', 'AQI']].describe()
        except KeyError:
            return "Missing required columns for statistical summary."