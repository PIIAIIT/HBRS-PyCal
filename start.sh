#!/bin/bash

# config
export PROJECT_DIR=$(pwd)

# path to python file and requirements file
PYTHON_FILE="PyCal.py"

# Create a virtual environment
if [ ! -d 'venv' ]; then
  echo "Erstelle virtuelle Umgebung..."
  python3 -m venv venv
fi

echo "Aktiviere virtuelle Umgebung..."
source venv/bin/activate

# Install requirements
if [ -f "requirements.txt" ]; then
  echo "Installiere requirements..."
  pip install -r requirements.txt --quiet
fi

# Start python file
python $PYTHON_FILE
