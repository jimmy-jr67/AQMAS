from models.pollutant import AirData, Environment, AQIRecord
from utils.validators import validate_positive, get_valid_float


class AirQualityService:
    def __init__(self):
        self.records = []

    def add_record_from_input(self):
        date = input("Enter date: ")
        location = input("Enter location: ")

        co2 = get_valid_float("Enter CO2: ")
        pm25 = get_valid_float("Enter PM2.5: ")
        pm10 = get_valid_float("Enter PM10: ")
        temp = get_valid_float("Enter Temperature: ")
        humidity = get_valid_float("Enter Humidity: ")

        if not all([
            validate_positive(co2, "CO2"),
            validate_positive(pm25, "PM2.5"),
            validate_positive(pm10, "PM10")
        ]):
            return

        air = AirData(co2, pm25, pm10)
        env = Environment(temp, humidity)
        record = AQIRecord(date, location, air, env)

        self.records.append(record)
        print("Record added successfully!")

    def get_all_records(self):
        return self.records