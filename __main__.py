from src.calendar import Calender
from src.filter import CalendarFilter
from src.importData.parser import WebDataParser
import os

PROJECT_DIR = os.getenv("PROJECT_DIR")

if __name__ == "__main__":
    # This is the main function
    # It is the entry point of the program
    # It is the first function that is called

    # Create a Parser object
    p = WebDataParser()
    p.extractDataFromWebsite()

    # Create a Calender object
    cal = Calender()
    cal.fill(p.getParsedData())

    # Create a Chooser object and adds options to it
    filter = CalendarFilter(cal)
    filter.addSemester("BI", 3)
    filter.addVL("Einführung in Diskrete Mathematik und Lineare Algebra")
    filter.addVL("Projekt-Seminar", False)
    filter.addVL("Competitive Bots")
    newData = filter.filterCoursesByOptions()

    # Set the new data to the parser object and create the new ics file
    p.updateData(newData)

    p.writeDataToJSON(PROJECT_DIR)
    p.generateCalendarFile()
