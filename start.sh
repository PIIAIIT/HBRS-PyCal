#!/bin/bash

# config
export PROJECT_DIR=$(pwd)

# path to python file and requirements file
PYTHON_FILE="__main__.py"
REQUIRED_PKG="requirements.txt"

# Start python file
if [ -f "$PYTHON_FILE" ]; then
  echo "Starte $PYTHON_FILE..."
  python3 "$PYTHON_FILE"
else
  echo "Datei $PYTHON_FILE nicht gefunden"
fi
