# author @patrick
# github @PIIAIIT
# date 2024-04-19
# version 1.0
# description: This script is used to parse the student plan from the website: "https://eva2.olotl.net/" and save it as a json file
#              The script also creates an ical file from the json file. The ical file can be imported into a calendar application.


# importing the necessary libraries
import requests
import os
from bs4 import BeautifulSoup
from datetime import datetime
import json
import uuid
from option import Option, OptionList

class App:

    def __init__(self) -> None:
        """Initializes the app object.
        :param _options: The _options for the app as an OptionList object"""
        # check last update
        self._options = None
        self.studiengang = None
        self.semester = None

        # working directory
        self.workingdir = os.path.dirname(os.path.abspath(__file__)) + "/"

        # two dimensional table for the degrees and their terms
        ## OPTIMIZE: use the file to get the data
        self.data = self.read_file('data.json')

        # last update information
        self.last_update = self.__check_update(self.data[-1])

    def update(self) -> None:
        """Check if the file is up to date and update it if necessary."""
        if self.last_update is None or self.__isLastWeek(self.last_update):
            print("(1/2) Updating the data...")
            self.__write_json()
            print("(2/2) Done.")
        
    def ical(self, veranstaltungen: list[dict]=[]) -> None:
        """Create the ical file.
        The ical file is created based on the _options given by the user."""
        if not veranstaltungen:
            for lv in self.data[:-1]:
                if lv["semesterName"] == self.studiengang + " " + str(self.semester):
                    veranstaltungen.append(lv)

        self.__write_ics(veranstaltungen)

        print("\nDone. Your Ical file is ready.")
        print("You can now import it into your calendar application.")

    def read_file(self, file:str) -> list[dict] | None:
        """Reads a file and returns the content as a string"""
        if not os.path.exists(self.workingdir+file):
            return None
        file: str = open(self.workingdir+file, 'r').read()
        return json.loads(file)

    def getStudiengaenge(self) -> set[str]:
        """Returns the degrees as a set of strings."""
        return sorted(set([e["semesterName"] for e in self.data[:-1]]))
    
    def getVeranstaltungen(self, studiengang: str) -> list[dict]:
        """Returns the events as a list of dictionaries"""
        ver = []
        for e in self.data[:-1]:
            if e["semesterName"] == studiengang:
                ver.append(e)
        return self.__sort(ver)   

    def setOption(self, options: OptionList) -> None:
        """Set the _options for the app.
        :param options: The _options for the app as an OptionList object"""
        self._options = options.get_options()
        self.studiengang = self._options[0].studiengang
        self.semester = self._options[0].semester

    def __sort(self, data: list[dict]) -> list[dict]:
        """Sorts the data by semesterName alphabetically.
        :param data: The data to sort as a list of dictionaries"""
        return sorted(data, key=lambda x: x["semesterName"])    

    def __write_json(self) -> None:
        """Writes the data from the website to a json file"""
        URL = "https://eva2.olotl.net/"
        response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Perform your desired parsing operations on the soup object
        # Example: Extract all the links from the webpage

        pre = soup.text
        f = open(self.workingdir+'data.json', 'w')
        f.write(pre[:-1])
        f.write(",{ \"last-update\": \""+datetime.now().strftime("%d/%m/%YT%H%M%S") + "\"}]")
        f.close()

    def __check_update(self, data: dict) -> None | datetime:
        """Check if the file is up to date.
        :param data: The data to check as a dictionary"""
        if data is None: return

        last_update = data["last-update"]
        return datetime.strptime(last_update, "%d/%m/%YT%H%M%S")

    def __isLastWeek(self, date:datetime) -> bool:
        """Check if the date is within the current week.
        :param date: The date to check as a datetime object"""
        date = date.split(" ")[2]
        file_date = datetime.strptime(date, "%d/%m/%YT%H%M%S")
        today = datetime.now()
        differenz = today - file_date
        if differenz.days < 7:
            return True
        return False

    def __write_ics(self, data: list[dict]) -> None:
        """Writes the ical file
        :param data: The data to write as a list of dictionaries"""
        # all conventions are based on the icalendar standard
        print("(1/2) Writing ical file...")

        # check if the file already exists
        # and create a new one if necessary
        filename = "calender.ical"
        if os.path.exists(self.workingdir + filename):
            for i in range(1, 100):
                if not os.path.exists(self.workingdir + f"calender ({i}).ical"):
                    filename = f"calender ({i}).ical"
                    break

        with open(self.workingdir + filename, "w") as f:
            # Calender Header
            f.write("BEGIN:VCALENDAR\n")

            f.write("VERSION:2.0\n")
            f.write("PRODID:Patrick Saft @PIIAIIT\n")
            f.write("CALSCALE:GREGORIAN\n")
            f.write("METHOD:PUBLISH\n")
            f.write("X-WR-CALNAME:Stundenplan H-brs\n")
            f.write("X-WR-TIMEZONE:Europe/Berlin\n")
            f.write("X-WR-CALDESC:Stundenplan von der www.kalenderapp.aptinstall.de\\nSeite\n")

            # Events
            for lv in data:
                startDate = datetime.strptime(lv["parsedDate"]["start"], "%d.%m.%Y")
                endDate = datetime.strptime(lv["parsedDate"]["end"], "%d.%m.%Y")
                weeks = endDate - startDate
                eventTime1 = datetime(startDate.year, startDate.month, startDate.day, int(lv["startTime"].split(":")[0]), int(lv["startTime"].split(":")[1]))
                eventTime2 = datetime(startDate.year, startDate.month, startDate.day, int(lv["endTime"].split(":")[0]), int(lv["endTime"].split(":")[1]))
                interval = 1 if lv["parsedDate"]["info"].split(" ")[0].startswith("KW") else 2
                
                f.write("BEGIN:VEVENT\n")
                f.write("DTSTART;TZID=Europe/Berlin:" + eventTime1.strftime("%Y%m%dT%H%M%S") + "\n")
                f.write("DTEND;TZID=Europe/Berlin:" + eventTime2.strftime("%Y%m%dT%H%M%S") + "\n")
                f.write(f"RRULE:FREQ=WEEKLY;COUNT={weeks.days//7};INTERVAL={interval}\n")
                f.write(f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n")
                f.write("UID:"+str(uuid.uuid4())+"\n")
                f.write("CREATED:"+datetime.now().strftime('%Y%m%dT%H%M%SZ')+"\n")
                f.write("DESCRIPTION:"+lv.get("title") + " in Raum: " + lv.get("room") + " bei: " + lv.get("lecturer") + "\n")
                f.write("LOCATION:"+lv.get("room")+"\n")
                f.write("SUMMARY:"+lv.get("title")+"\n")
                f.write("END:VEVENT\n")

            ## Events

            ## Calender Footer
            f.write("END:VCALENDAR")

        print("(2/2) Writing done.")


if __name__ == '__main__':

    ## _options for the app
    # verbesserungsidee Professoren, Lehrveranstaltungen
    o = Option("BI", 2)

    ## create the option list
    # add more _options if needed by 
    # calling the add_option method or by adding them to the constructor
    _options = OptionList(o)
    # _options.add_option()

    # create the app object
    app = App()
    app.setOption(_options)

    # write the json file
    # takes a while
    # app.update()

    # write the ical file
    app.ical()