# HBRS-PyCal
Das ist ein kleines Python-Projekt, um ein Stundenplan für die Hochschule Bonn-Rhein-Sieg zu generieren.
Diese Datei kann dann in eine beliebiges Kalender-Programm importiert werden.

# !!! IN DEVELEOPMENT !!! 

Das ist zur Zeit nur ein Prototyp und wird noch weiter entwickelt. \
Es kann sein, dass es noch einige Bugs gibt.
# !!! Programm funktioniert momentan nicht auf Windows !!!

# Voraussetzungen
Für die Ausführung dieses Projekts benötigen Sie [Python](https://www.python.org/).

<br>

# Anleitung zur Verwendung

## Github repository klonen
- Über die Konsole:
    ```python
    git clone https://github.com/PIIAIIT/HBRS-PyCal.git &&
    cd HBRS-PyCal &&
    git checkout dev
    ```
- Alternativ als `.zip` Datei herunterladen
    + Klicken Sie oben auf [`<> Code`](https://github.com/PIIAIIT/HBRS-PyCal/archive/refs/heads/dev.zip) und wählen Sie `Download ZIP`.
    + Entpacken Sie die Dateien in einem Ordner Ihrer Wahl.

## Ausführen des Scripts
    
- Nachdem Sie die gewünschten Optionen bearbeitet haben, können Sie das Start-Script ausführen:
    + Windows:
      ```
          start.bat
      ```
    + Linux/MacOS:
      ```sh
          ./start.sh
      ```

## Output 
+ Die Datei ```Stundenplan.ics``` wird standardmäßig im Ordner ```ouput/``` abgelegt.


# Kalender importieren

+ Diese Datei kann in ein beliebiges Kalenderprogramm importiert werden. Eine Anleitung für den Google Kalender finden Sie [hier](./src/docs/IMPORT.md).


# Problems
Bei Problemen mit dem Script erstellen Sie bitte ein [Issue](https://github.com/PIIAIIT/HBRS-PyCal/issues), um Unterstützung zu erhalten.

