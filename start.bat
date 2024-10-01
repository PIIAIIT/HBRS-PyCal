@echo off

REM Set the project directory
set PROJECT_DIR=%cd%

REM Path to the Python File
set PYTHON_FILE=PyCal.py

REM Check if Python is installed
if exist "%PYTHON_FILE%" (
  echo Starte %PYTHON_FILE%...

  REM Run Python File
  python %PYTHON_FILE%

) else (
  echo "Python is not installed"
)
