import sys
from models.pollutant import AQIRecord
from services.aq_service import AirQualityService
from storage.file_handler import FileHandler
from visual.charts import AQIVisualizer
from analysis.stats import AQIAnalytics


def display_menu():
    print("\n" + "=" * 25)
    print("   AQMAS CONTROL PANEL")
    print("=" * 25)
    print("1. Add Air Quality Record")
    print("2. View All Records (Memory)")
    print("3. Save Data to Persistent Storage")
    print("4. Load Data from Storage")
    print("5. Generate Trend Analysis")
    print("6. Show Category Distribution")
    print("7. Statistical Summary")
    print("8. Exit")
    return input("\nSelect an option (1-8): ")


def main():
    # Initialize Core Components
    service = AirQualityService()
    storage = FileHandler()
    visualizer = AQIVisualizer()
    analytics = AQIAnalytics()

    while True:
        choice = display_menu()

        if choice == "1":
            service.add_record_from_input()

        elif choice == "2":
            records = service.get_all_records()
            if not records:
                print("No records found in current session.")
            for r in records:
                print(r)

        elif choice == "3":
            data = [r.to_dict() for r in service.get_all_records()]
            storage.save_to_csv(data)

        elif choice == "4":
            df = storage.load_as_dataframe()
            if df is not None:
                # Sync memory with loaded data if needed
                print("Data loaded successfully.")

        elif choice == "5":
            df = storage.load_as_dataframe()
            visualizer.plot_trends(df)

        elif choice == "6":
            df = storage.load_as_dataframe()
            visualizer.plot_categories(df)

        elif choice == "7":
            df = storage.load_as_dataframe()
            summary = analytics.calculate_summary(df)
            print("\n--- STATISTICAL SUMMARY ---")
            print(summary)

        elif choice == "8":
            print("Exiting system. Securing data...")
            sys.exit()

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()