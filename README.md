# AQMAS: Air Quality Monitoring & Analysis System

AQMAS is a modular, layered Python application designed for high-integrity environmental data management. It implements a professional software architecture to handle pollutant tracking, statistical forecasting, and multi-format data persistence using standard, efficient libraries.

## 🏗️ Architecture

This system strictly adheres to the **Separation of Concerns**, ensuring scalable and maintainable code. The application is divided into purpose-driven modules:

* **`main.py`**: The central orchestrator and CLI entry point.
* **`models/`**: Object-Oriented data structures encapsulating core entities (Pollutants, Environments, AQI Records).
* **`services/`**: The business logic layer that processes interactions between models and storage.
* **`utils/`**: Robust input validation, timestamp normalization, and data sanitization.
* **`storage/`**: Persistent data management (CSV/JSON) utilizing Pandas DataFrames.
* **`analysis/`**: Statistical operations, trend detection, and moving-average calculations.
* **`visual/`**: Data visualization layer generating charts via Matplotlib.

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.10+ installed. The system relies on a minimalist stack of standard data science libraries.

```bash
pip install pandas numpy matplotlib
