import requests
from bs4 import BeautifulSoup
import os
import json
from src.exportData.createFile import createCalendarFile


class WebDataParser:
    def __init__(self):
        self.currentWorkingDir = os.path.dirname(__file__) + "/"
        self.data: list[dict] = None

    def extractDataFromWebsite(self, url: str) -> None:
        response = requests.get(
            url, headers={'User-Agent': 'Mozilla/5.0'})

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Perform your desired parsing operations on the soup object
        # Example: Extract all the links from the webpage

        # Check if the response was successful
        if (not response.ok):
            print("Fehler Code: " + response.status_code)
            return

        self.data = json.loads(soup.text)  # pareses the json data

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

    def writeDataToJSON(self, maindir: str) -> None:
        # file already exists
        if not os.path.exists(maindir + "/cache/data.json"):
            with open(maindir + "/cache/data.json", "w") as f:
                json.dump(self.data, f, indent=4)

    def generateCalendarFile(self, maindir: str) -> None:
        """
        Writes the data from the website to a json file
        """
        # old version
        # creator = Creator(self.currentWorkingDir, "calendar.ical")
        # creator.createFile(self.data)
        createCalendarFile(maindir, "calendar.ical", self.data)
