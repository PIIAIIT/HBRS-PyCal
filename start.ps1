# Set the project directory to the current directory
$PROJECT_DIR = Get-Location

# Path to the Python file
$PYTHON_FILE = "PyCal.py"

# Check if the Python file exists
if (Test-Path $PYTHON_FILE) {
    Write-Host "Starte $PYTHON_FILE..."

    # Run Python (assuming python is added to PATH)
    python $PYTHON_FILE
} else {
    Write-Host "Datei $PYTHON_FILE nicht gefunden"
}

