# HBRS-PyCal
Das ist ein kleines Python-Projekt, um ein Stundenplan für die Hochschule Bonn-Rhein-Sieg zu generieren.
Diese Datei kann dann in eine beliebiges Kalender-Programm importiert werden.

# !!! IN DEVELEOPMENT !!! 
Das ist zur Zeit nur ein Prototyp und wird noch weiter entwickelt. \
Es kann sein, dass es noch einige Bugs gibt.

# Requirements
Um dieses Projekt auszuführen, benötigen Sie [Python](https://www.python.org/). \
Außerdem benötigen sie die folgenden Python-Module:
- requests
<br><br>
# How to use

+   ## Github repository klonen
    - Per Konsole:
    ```python
    git clone https://github.com/PIIAIIT/HBRS-PyCal.git
    cd HBRS-PyCal
    ```
    - Als `.zip` Datei herunterladen
        + Oben auf `<> Code` drücken und auf `Download zip` drücken
        + Die Dateien in ein beliebigen Ordner entpacken.

+   ## Dein eigenen Stundenplan erstellen
    - Im dem Ordner finden Sie verschiedene Dateien unteranderem die `PyCal.py` Datei. 
      Öffnen Sie die Datei mit einer von Ihnen beliebigen IDE.
    - Zeile 29 erstellt den CalenderFilter.
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
    - Ab der Zeile 41 können Sie einzelne Vorlesungen hinzufügen: <br>
     Es ist zu beachten, dass die addVL Funktion nicht den String auf Gleichheit überprüft sondern nur auf Ähnlichkeit. Wenn eine VL nicht hinzugefügt wird schauen Sie bitte in der `cache/semester.json` Datei für alle VL's und SemesterNamen. \
    !! Die `semester.json` Datei wird erst beim ersten mal Ausführen generiert. !!
    ```python
        # addVL(<VLName>, <IncludeVL>)
        # For <VLName> you can look at the "cache/semester.json" file
        filter.addVL("Diskrete Mathematik und Lineare Algebra")
    ```
     oder dafür sorgen dass eine Vorlesung nicht hinzugefügt werden soll:
    ```python
        filter.addVL("Competitive Bots", False)
    ```
    
    
    - Auf der Zeile 52 kann man nach einem \<String> suchen in einer speziellen Course \<Key>
    die \<Key> Argumente finden Sie in der `cache/data.json` Datei. \
    !! Die `data.json` Datei wird erst beim ersten mal Ausführen generiert. !!
    ```python
        # addContains(<String>, <Key>, <IncludeString>)
        # <String> is the string that should be contained
        # <Key> is the key of the dictionary of the course data
    
        filter.addContains("Projekt-Seminar", "title", False)
    ```
+ ## Ausführen der PyCal.py Datei
    - Nach der Bearbeitung der Optionen kannst du das Start-Script `start.*` einfach ausführen. \
      + Windows:
      ```sh
          ./start.bat
      ```
      oder für Powershell:
      ```sh
          ./start.ps1
      ```

      + Linux/MacOS:
      ```sh
          ./start.sh
      ```


+ ## Output
    - Deine ```<name>.ical``` liegt nun im ```ouput/``` Ordner bereit.

    - Diese Datei kann in ein beliebiges Kalender-Programm importiert werden. [Hier](./src/docs/IMPORT.md) ist ein Beispiel für den Google Kalender:


# Problems
Bei Problemen gerne ein Issue erstellen.
