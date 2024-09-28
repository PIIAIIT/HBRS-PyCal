import requests
import os
import json
import datetime
from src.exportData.createFile import createCalendarFile


class WebDataParser:
    def __init__(self):
        self.URL = "https://eva2.olotl.net/"
        self.data: list[dict] = None

        pwd = os.getenv("PROJECT_DIR") + "/"
        os.makedirs(pwd + "cache", exist_ok=True)
        if os.path.exists(pwd + "cache/lastUpdate.txt"):
            with open(pwd + "cache/lastUpdate.txt", "r") as f:
                self.lastUpdate = f.read()
        else:
            self.lastUpdate = ""

    def extractDataFromWebsite(self) -> None:
        if self.lastUpdate == str(datetime.date.today()):
            print("Data is already up to date")
            return

        print("Reading data from " + self.URL)
        response = requests.get(
            self.URL, headers={'User-Agent': 'Mozilla/5.0'})

        # Parse the HTML content
        # soup = BeautifulSoup(response.text, 'html.parser') # old version
        # Perform your desired parsing operations on the soup object
        # Example: Extract all the links from the webpage

        # Check if the response was successful
        if (not response.ok):
            print("Fehler Code: " + str(response.status_code))
            return

        try:
            self.data = response.json()
            self.lastUpdate = str(datetime.date.today())
            print("Data was successfully extracted")
        except json.JSONDecodeError:
            print("Error: Could not parse the json data")
        # self.data = json.loads(soup.text)  # pareses the json data

    def getParsedData(self) -> list[dict]:
        """
        @return: a python object containing the data from the json file
        """
        return self.data

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

    def writeDataToJSON(self, maindir: str) -> None:
        # file already exists
        if not os.path.exists(maindir + "/cache/data.json"):
            f = open(maindir + "/cache/data.json", "w", encoding="utf-8")
            json.dump(self.data, f, ensure_ascii=False, indent=4)
            f.close()

        if not os.path.exists(maindir + "/cache/lastUpdate.txt"):
            with open(maindir + "/cache/lastUpdate.txt", "w") as f:
                f.write(self.lastUpdate)

    def generateCalendarFile(self) -> None:
        """
        Writes the data from the website to a json file
        """
        # old version
        # creator = Creator(self.currentWorkingDir, "calendar.ical")
        # creator.createFile(self.data)
        createCalendarFile(self.data)
