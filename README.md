# Air Quality Monitoring and Analysis System (AQMAS)

Rapid urbanization and industrial growth have led to significant deterioration in air quality. While government agencies operate large-scale monitoring stations, these are often centralized and inaccessible for small-scale or educational use. 

**AQMAS** is a Python-based, intelligent air-quality assessment platform designed to bridge this gap. It provides a complete workflow for collecting, processing, analyzing, and visualizing air-quality data to help users understand pollution behavior quantitatively.

## 🎯 High-Level Functions
1. **Data Collection:** Records pollutant concentrations (PM2.5, PM10, CO2, etc.) associated with timestamps.
2. **AQI Computation:** Calculates individual sub-indices, overall AQI, and categorizes health risks (Good, Moderate, Poor).
3. **Trend Tracking:** Enables daily and weekly analysis to identify pollution spikes or prolonged hazardous exposure.
4. **Analytical Insights:** Uses `NumPy` and `Pandas` to compute average concentrations, max/min levels, and short-term forecasting using moving averages.
5. **Visual Dashboards:** Leverages `Matplotlib` to generate line charts for trends and bar charts for category distribution.
6. **Robust Validation:** Implements strict exception handling to reject invalid inputs and prevent system crashes.

## 🏗️ Detailed System Architecture

AQMAS follows a modular, layered, and maintainable architecture, developed progressively across 12 stages, mirroring professional software systems.

```text
AQMAS_Project/
├── main.py              → Entry point and menu control
├── models/              
│   ├── __init__.py
│   └── pollutant.py     → OOP classes for AirData, Environment, and AQIRecord
├── services/            
│   ├── __init__.py
│   └── aq_service.py    → Core business logic (add, compute, analyze)
├── utils/               
│   ├── __init__.py
│   └── validators.py    → Input validation & custom exceptions
├── storage/             
│   ├── __init__.py
│   └── file_handler.py  → CSV read & write via Pandas
├── analysis/            
│   ├── __init__.py
│   └── stats.py         → Analytics & statistical summaries
├── visual/              
│   ├── __init__.py
│   └── charts.py        → Matplotlib visualizations
└── data/                
    └── air_quality.csv  → Persistent storage
