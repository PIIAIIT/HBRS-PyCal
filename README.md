# HBRS-PyCal
Willkommen zu einem kleinen Python-Projekt für das Webscraping der Website https://eva2.olotl.net/. Es extrahiert Daten, analysiert sie und erstellt eine iCal-Datei, die in Ihre Kalenderanwendung importiert werden kann. Bitte habt Nachsicht mit dem unprofessionellen Python-Code und dem Design der App. Diese App wurde nur kurzfristig erstellt und eher aus Spaß. 😄

# Requirements
Um dieses Projekt auszuführen, benötigen Sie [Python](https://www.python.org/) und das Python-Modul customtkinter. Hier ist ein Link, wie Sie [customtkinter](https://pypi.org/project/customtkinter/0.3/) installieren können. Weitere offensichtliche Anforderungen finden Sie in der [requirements.txt](./requirements.txt).

# How to use
- Über die Konsole:
  + Geben Sie `git clone https://github.com/PIIAIIT/HBRS-PyCal.git` in Ihre Konsole ein
  + Wechseln Sie in das Verzeichnis `cd HBRS-PyCal`
  + Starten Sie dann die Datei frame.py mit `python frame.py`
- Download der .zip-Datei
  + Laden Sie zunächst die Zip-Datei [hier](https://github.com/PIIAIIT/HBRS-PyCal/archive/refs/heads/main.zip) herunter
  + Entpacken Sie die Zip-Datei in einem beliebigen Verzeichnis
  + Wechseln Sie in das Verzeichnis
  + Führen Sie die Python-Datei frame.py aus
- Nachdem die `frame.py` Datei ausgeführt wurde ist die .ical-Datei in dem selben Verzeichnis wie die python-Dateien als `calendar.ical`.

# How it works
Die App besteht aus zwei Dateien der `frame.py` und der `app.py`<br>
Die `app.py` gibt die Grundlage für die App und kann auch ohne GUI ausgeführt werden.<br>
+ Um mit der app.py eine ical Datei zu generieren muss zuerst eine OptionList Instanzieren werden.
+ Die OptionList kann mehrere Option Objekte beinhaltet die auch vorher instanziert werden müssen. (Siehe app.py Datei)
+ Außerdem besteht die Möglichkeit mit der update Funktion die `data.json` Datei erneut zu generieren
+ Schließlich kann mit der ical Funktion die .ical Datei in den aktuellen Verzeichnis geschrieben werden und das war's!<br>
<br>

Die `frame.py` ergibt die Grafische Oberfläche und macht sie zu einer vollständigen Anwendung.<br>
* Die `frame.py` Datei bietet weniger Flexibilität. Am Besten wird diese Datei einfach nur ausgeführt.

# Problems
Bei Problemen gerne ein Issue erstellen.
