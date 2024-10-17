import requests
import os
import json
# import datetime
from src.exportData.createFile import createiCalFile

PROJECT_DIR = os.getenv("PROJECT_DIR")
if PROJECT_DIR is None:
    PROJECT_DIR = os.getcwd()
cache_dir = PROJECT_DIR + "/cache/"


class WebDataParser:
    def __init__(self):
        self.URL = "https://eva2.olotl.net/"
        self.data: list[dict] = []
        self.stud: list[str] = []

        # lastUpdate updates every day
        os.makedirs(cache_dir, exist_ok=True)
        if os.path.exists(cache_dir + "lastUpdate.txt"):
            with open(cache_dir + "lastUpdate.txt", "r") as f:
                self.lastUpdate = f.read()
        else:
            self.lastUpdate = ""

    def extractDataFromWebsite(self) -> None:
        # if self.lastUpdate == str(datetime.date.today()):
        #     print("Data is already up to date")
        #     return

        print("Reading data from " + self.URL)
        response = requests.get(
            self.URL, headers={'User-Agent': 'Mozilla/5.0'})

        # Parse the HTML content
        # soup = BeautifulSoup(response.text, 'html.parser')  # old version
        # Perform your desired parsing operations on the soup object
        # Example: Extract all the links from the webpage

        # Check if the response was successful
        if (not response.ok):
            print("Fehler Code: " + str(response.status_code))
            return

        try:
            # self.data = json.loads(soup.text)  # pareses the json data
            self.data = response.json()
            for d in self.data:
                if d["semesterName"] not in self.stud:
                    self.stud.append(d["semesterName"])
            # self.writeDataToJSON()
            # self.lastUpdate = str(datetime.date.today())
            print("Data was successfully extracted")
        except json.JSONDecodeError:
            print("Error: Could not parse the json data")

    def getParsedData(self) -> list[dict]:
        """
        @return: a python object containing the data from the json file
        """
        if self.data is None:
            raise ValueError("No data was extracted yet")
        return self.data

    def getStudiengaenge(self) -> list[str]:
        return self.stud

    def getLehrveranstaltungVonSemester(self, semesterName:str) -> list[dict]:
        return sorted([d for d in self.data if d["semesterName"] == semesterName], key=lambda x: x["title"])

    def updateData(self, data: list[dict]) -> None:
        """
        Sets the data of the parser object
        """
        self.data = data

    def showData(self) -> None:
        """
        Prints the data of the parser object
        """
        print(self.data)

    def writeDataToJSON(self) -> None:
        # file already exists
        # if not os.path.exists(maindir + "/cache/data.json"):
        f = open(cache_dir + "data.json", "w", encoding="utf-8")
        json.dump(self.data, f, ensure_ascii=False, indent=4)
        f.close()

        if not os.path.exists(cache_dir + "lastUpdate.txt"):
            with open(cache_dir + "lastUpdate.txt", "w") as f:
                f.write(self.lastUpdate)

    def generateCalendarFile(self, abfrage=True) -> None:
        """
        Writes the data from the website to a json file
        """
        # old version
        # creator = Creator(self.currentWorkingDir, "calendar.ical")
        # creator.createFile(self.data)
        createiCalFile(self.data, abfrage)
