#!/bin/bash

# config
export PROJECT_DIR=$(pwd)

# Pfad zur Python-Datei
PYTHON_FILE="./__main__.py"

if [ -f "$PYTHON_FILE" ]; then
  echo "Starte $PYTHON_FILE..."
  python3 "$PYTHON_FILE"
else
  echo "Datei $PYTHON_FILE nicht gefunden"
fi
