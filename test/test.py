from src.CalCourse import Calender
from src.chooser import CalendarFilter
from src.exportData.option import Option
from src.importData.parser import WebDataParser
import os

if __name__ == "__main__":
    # This is the main function
    # It is the entry point of the program
    # It is the first function that is called

    # URL of the website
    URL: str = "https://eva2.olotl.net/"
    # Create a Parser object
    p = WebDataParser()
    p.parseWebsite(URL)

    # Create a Calender object
    cal = Calender()
    cal.fill(p.getData())

    # Create a Chooser object and adds options to it
    filter = CalendarFilter()
    filter.addOption(Option("BI 3"))
    filter.addOption(
        Option("Einführung in Diskrete Mathematik und Lineare Algebra"))
    newData = filter.by_options(cal)

    # Set the new data to the parser object and create the new ics file
    p.setData(newData)

    p.writeJSON(os.path.dirname(__file__) + "/")
    p.create(os.path.dirname(__file__) + "/")
