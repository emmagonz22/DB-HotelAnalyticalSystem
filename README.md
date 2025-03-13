# Los Chuletas - Hotel Analytical System

## Project Brief

The Hotel Analytical System is a comprehensive data management and analytics platform designed for hotel operations. This system processes, analyzes, and visualizes data from various aspects of hotel management including reservations, guest services, inventory, and financial transactions.

Key features:
- Guest information management and reservation tracking
- Room occupancy and availability analytics
- Revenue and expense monitoring dashboards
- Trend analysis for seasonal booking patterns
- Performance metrics for hotel services and amenities

This system aims to provide hotel management with actionable insights to optimize operations, enhance guest experiences, and maximize revenue opportunities.

## ETL Process Documentation

The ETL (Extract, Transform, Load) pipeline handles data from multiple sources and formats:

### Data Sources
- **Excel files (.xlsx)**: Chain and login information
- **CSV files (.csv)**: Hotel metadata, client information, and room unavailability schedules
- **JSON files (.json)**: Employee data and room details
- **SQLite databases (.db)**: Room information and reservation data

### ETL Components

1. **Extract**:
   - Custom parsers for each file format (xlsx, csv, json, db)
   - Connection handlers for database sources
   - Raw data extraction with appropriate error handling

2. **Transform**:
   - Data cleaning: Removing null values with `.dropna()`
   - Column renaming for database compatibility
   - Type conversion and validation
   - Filtering invalid records (e.g., payment methods validation)

3. **Load**:
   - PostgreSQL database loading via parameterized SQL queries
   - Transaction management with commits and rollbacks
   - Error logging and exception handling

### ETL Flow
1. Chain data load (xlsx)
2. Hotel data load (csv)
3. Employee data load (json)
4. Login data load (xlsx)
5. Room description load (json)
6. Room data load (db)
7. Room unavailability load (csv)
8. Client data load (csv)
9. Reservation data load (db)

## Tech Stack

### Backend
- **Python**: Core programming language
- **Flask**: Web application framework
- **PostgreSQL**: Primary database
- **SQLite**: Source database for some datasets
- **Pandas**: Data manipulation and analysis
- **Gunicorn**: WSGI HTTP server for production

### Frontend
- **Jupyter Notebook**: Interactive computing platform
- **Voila**: Turns Jupyter notebooks into standalone web applications
- **ipywidgets**: Interactive HTML widgets for Jupyter notebooks
- **matplotlib/seaborn**: Data visualization libraries
- **Plotly**: Interactive graphing library
- **pandas**: Data manipulation and analysis

## MVC Design Pattern

The application follows a modified MVC architecture:

### Model
- Database schemas and models
- Data access layer
- Business logic for hotel analytics
- Data validation rules

### Controller
- Flask routes and API endpoints
- Request handling and validation
- Service layer orchestrating data flow
- Authentication and authorization logic

### Presentation (replacing traditional View)
- Jupyter notebooks containing:
  - Data processing logic
  - Visualization cells
  - Interactive widgets via ipywidgets
  - User interface elements
- Voila converts these notebooks into web applications

## Running the Project

### Prerequisites
- Python 3.7+
- PostgreSQL database
- Git

### Backend Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   cd DB-HotelAnalyticalSystem
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure the database connection in `.env` file:
   ```
   DB_HOST=localhost
   DB_NAME=hotel_analytical_system
   DB_USER=postgres
   DB_PASS=your_password
   DB_PORT=5432
   ```

5. Run the ETL process to populate the database:
   ```
   cd ETL
   python main.py
   ```

6. Start the backend server:
   ```
   cd ..
   python -m gunicorn --chdir backend main:app
   ```
   Or use the provided Procfile:
   ```
   gunicorn --chdir backend main:app
   ```

### Frontend Setup
1. Install Jupyter and Voila:
   ```
   pip install notebook voila ipywidgets
   ```

2. Launch the Jupyter notebook server:
   ```
   jupyter notebook
   ```

3. Navigate to the notebook files in your browser.

4. To run the application as a web app using Voila:
   ```
   voila notebooks/dashboard.ipynb
   ```

5. Access the application at the URL provided by Voila (typically http://localhost:8866)

### Deployment
The application can be deployed using platforms like Heroku:
```
heroku create
git push heroku main
```

## Project Structure
```
DB-HotelAnalyticalSystem/
├── ETL/                    # ETL scripts
│   ├── main.py             # Main ETL orchestration 
│   ├── etl_xlsx_files.py   # Excel files processor
│   ├── etl_csv_files.py    # CSV files processor
│   ├── etl_json_files.py   # JSON files processor
│   └── etl_db_files.py     # Database extraction scripts
├── backend/                # Flask application
│   ├── models/             # Data models
│   ├── controllers/        # Route controllers
│   ├── services/           # Business logic
│   └── main.py             # App entry point
├── notebooks/              # Jupyter notebooks
│   ├── dashboard.ipynb     # Main dashboard notebook
│   ├── analytics.ipynb     # Analytics notebook
│   └── reports.ipynb       # Report generation notebook
├── database/               # Database scripts
│   └── schema.sql          # Database schema
├── Procfile                # Deployment configuration
└── README.md               # Project documentation
```
