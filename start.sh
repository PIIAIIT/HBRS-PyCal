#!/bin/bash

# config
export PROJECT_DIR=$(pwd)

# path to python file and requirements file
PYTHON_FILE="PyCal.py"

# Start python file
if [ -f "$PYTHON_FILE" ]; then
  echo "Starte $PYTHON_FILE..."

  if [[ "$OSTYPE" == "msys" ]]; then
    python "$PYTHON_FILE"
  elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    python3 "$PYTHON_FILE"
  elif [[ "$OSTYPE" == "darwin" ]]; then
    python3 "$PYTHON_FILE"
  else
    echo "OS nicht erkannt"
  fi
else
  echo "Datei $PYTHON_FILE nicht gefunden"
fi
