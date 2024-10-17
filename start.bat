@echo off

:: Set the project directory
set PROJECT_DIR=%cd%

:: Path to the Python File
set PYTHON_FILE=PyCal.py

if not exist "venv" (
  echo "Creating Virtual Environment..."
  python -m venv venv
)

:: Activate the Virtual Environment
echo "Activating Virtual Environment..."
call venv\Scripts\activate

:: Install the required packages
if exist "requirements.txt" (
  echo "Installing the required packages..."
  pip install -r requirements.txt
) else (
  echo "requirements.txt not found"
)

:: Check if Python is installed
echo "Starte %PYTHON_FILE%..."
python %PYTHON_FILE%
