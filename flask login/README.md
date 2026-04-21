# Flask Web App

This is a basic Flask web application with SQLAlchemy database for accounts.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python run.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/`

## Database

The app uses SQLAlchemy with a SQLite database (`instance/accounts.db`) for storing accounts.

### Account Model
- `account_id` (primary key): Unique 12-digit random number (string)
- `first_name`: String (50 chars)
- `last_name`: String (50 chars)
- `email`: Unique string (120 chars)
- `password`: String (128 chars)

## Project Structure

- `run.py`: Entry point to run the application
- `app/`: Main application package
  - `__init__.py`: Flask app factory
  - `models.py`: Database models (SQLAlchemy)
  - `routes.py`: Flask routes
  - `config.py`: Application configuration
  - `templates/`: HTML templates
  - `static/`: Static files (CSS, JS, images)
- `requirements.txt`: Python dependencies
- `instance/`: Instance-specific data (database)