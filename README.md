# HBRS-PyCal
Das ist ein kleines Python-Projekt, um ein Stundenplan für die Hochschule Bonn-Rhein-Sieg zu generieren.
Diese Datei kann dann in eine beliebiges Kalender-Programm importiert werden.

# !!! IN DEVELEOPMENT !!! 
Das ist zur Zeit nur ein Prototyp und wird noch weiter entwickelt. \
Es kann sein, dass es noch einige Bugs gibt.

# Voraussetzungen
Für die Ausführung dieses Projekts benötigen Sie [Python](https://www.python.org/).

<br><br>
# Anleitung zur Verwendung

*   ## Github repository klonen
    - Über die Konsole:
    ```python
    git clone https://github.com/PIIAIIT/HBRS-PyCal.git
    cd HBRS-PyCal
    ```
    - Alternativ als `.zip` Datei herunterladen
        + Klicken Sie oben auf `<> Code` und wählen Sie `Download ZIP`.
        + Entpacken Sie die Dateien in einem Ordner Ihrer Wahl.

*   ## Dein eigenen Stundenplan erstellen
    - Im dem Ordner finden Sie verschiedene Dateien darunter die `PyCal.py` Datei. 
      Öffnen Sie diese mit einer beliebigen IDE.
    - Zeile 29 erstellt den `CalenderFilter`.
    ```python
        # Create a Chooser object and adds options to it
        filter = CalenderFilter(cal) # DONT CHANGE THIS
    ```
    - Ab der Zeile 32 können Sie Ihren Fachbereich und Semester eingeben.
    ```python
        # USE addSemester to add a Semester that you want to include in your ical file
        # you can add a boolean value at the end of the function to decide if the semester should be included or not
        # addSemester(<SemsterName>, <SemesterNr>, <IncludeSemester>)
        filter.addSemester("BI", 3)
        # or
        filter.addSemester("BWI", 3, False) # So you dont want BWI 3 in your calender file
    ```
    - Ab der Zeile 42 können Sie einzelne Vorlesungen hinzufügen:
      + Beachten Sie, dass die Funktion `addVL` nur auf Ähnlichkeit prüft. Falls eine Vorlesung nicht hinzugefügt wird, sehen Sie in der `cache/semester.json` Datei nach allen VL-Namen. \
    **Hinweis:** Die `semester.json` Datei wird erst beim ersten mal Ausführen generiert.
    ```python
        # addVL(<VLName>, <IncludeVL>)
        # For <VLName> you can look at the "cache/semester.json" file
        filter.addVL("Diskrete Mathematik und Lineare Algebra")
    ```
      + Um sicherzustellen, dass eine Vorlesung **nicht** hinzugefügt wird:
    ```python
        filter.addVL("Competitive Bots", False)
    ```
    - Auf der Zeile 52 können Sie nach einem \<String> in einem bestimmten Kurs\<Key> suchen.
    Die \<Key>-Argumente finden Sie in der `cache/data.json` Datei. \
    **Hinweis:** Die `data.json` Datei wird ebenfalls erst beim ersten Ausführen generiert.
    ```python
        # addContains(<String>, <Key>, <IncludeString>)
        # <String> is the string that should be contained
        # <Key> is the key of the dictionary of the course data
    
        filter.addContains("Projekt-Seminar", "title", False)
    ```
*   ## Ausführen der `PyCal.py` Datei
    - Nachdem Sie die gewünschten Optionen bearbeitet haben, können Sie das Start-Script ausführen:
      + Windows:
      ```sh
          start.bat
      ```
      + Linux/MacOS:
      ```sh
          ./start.sh
      ```


*   ## Output 
    - Die Datei ```<name>.ics``` wird im Ordner ```ouput/``` abgelegt.

    - Diese Datei kann in ein beliebiges Kalenderprogramm importiert werden. Eine Anleitung für den Google Kalender finden Sie [hier](./src/docs/IMPORT.md).


# Problems
Bei Problemen mit dem Script erstellen Sie bitte ein [Issue](https://github.com/PIIAIIT/HBRS-PyCal/issues), um Unterstützung zu erhalten.
