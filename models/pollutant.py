class AirData:
    def __init__(self, co2, pm25, pm10):
        self.co2 = co2
        self.pm25 = pm25
        self.pm10 = pm10

    def __str__(self):
        return f"CO2: {self.co2}, PM2.5: {self.pm25}, PM10: {self.pm10}"


class Environment:
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity

    def __str__(self):
        return f"Temp: {self.temp}, Humidity: {self.humidity}"


class Record:
    def __init__(self, date):
        self.date = date


class AQIRecord(Record):
    def __init__(self, date, location, air, env):
        super().__init__(date)
        self.location = location
        self.air = air
        self.env = env
        self.aqi = self.calculate_aqi()

    def calculate_aqi(self):
        return (self.air.co2 + self.air.pm25 + self.air.pm10) / 3

    def category(self):
        if self.aqi <= 50:
            return "Good"
        elif self.aqi <= 100:
            return "Moderate"
        else:
            return "Poor"

    def to_dict(self):
        return {
            "Date": self.date,
            "Location": self.location,
            "CO2": self.air.co2,
            "PM2.5": self.air.pm25,
            "PM10": self.air.pm10,
            "Temperature": self.env.temp,
            "Humidity": self.env.humidity,
            "AQI": round(self.aqi, 2),
            "Category": self.category()
        }

    def __str__(self):
        return f"{self.date} | {self.location} | {self.air} | {self.env} | AQI: {self.aqi:.2f} ({self.category()})"