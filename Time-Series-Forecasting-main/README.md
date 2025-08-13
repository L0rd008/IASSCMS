# Time-Series-Forecasting
This repository contains all necessary training methods, datasets, and works related to the development of Intelligent Demand Forecasting for Supply Chain Management.

## Running the Backend Service

### Setup Environment

Before running the service, you need to set up a Python virtual environment:

#### Create and Activate Virtual Environment

On Windows:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

On macOS/Linux:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment (or Git Bash)
source .venv/Scripts/activate
```

#### Install Dependencies
```bash
# Install requirements
cd forecasting_service
pip install -r requirements.txt
```

### Django Commands

The project includes a Makefile with the following commands to manage the Django backend service:

- Ensure that you are in the project's root directory where the `Makefile` is located.

#### Starting the Server
```bash
# Start the Django server with migrations
make run-server
```
This will:
1. Create migrations for the forecastApp
2. Apply migrations to the database
3. Start the Django server at http://localhost:8000/

### Other Commands

#### Access Django Shell
```bash
make shell
```

#### Run Tests
```bash
make test
```

#### Clear and Recreate Migrations
```bash
make clear-migrations
```
This will delete all migration files (except `__init__.py`), then recreate and apply migrations.

#### Start Server with Fake Migrations
```bash
make run-server-fake
```
Use this when you need to run the server with `--fake-initial` flag for migrations.