from src.calendar import Calender
from src.filter import CalenderFilter
from src.importData.parser import WebDataParser
import os

PROJECT_DIR = os.getenv("PROJECT_DIR")

################################################
# This is experimental code
# use at your own risk
# This code is not fully tested yet
################################################

if __name__ == "__main__":
    # This is the main function
    ################################################
    # DON'T CHANGE THIS CODE
    # Create a Parser object
    p = WebDataParser()
    p.extractDataFromWebsite()
    # Create a Calender object
    cal = Calender()
    cal.fill(p.getParsedData())
    # DONT CHANGE THIS CODE
    ################################################

    # YOU CAN CHANGE THIS CODE
    # Create a Chooser object and adds options to it
    filter = CalenderFilter(cal) # DONT CHANGE THIS

    # TODO: ADD YOUR CODE HERE
    # USE addSemester to add a Semester that you want to include in your ical file
    # you can add a boolean value at the end of the function to decide if the semester should be included or not
    # addSemester(<SemsterName>, <SemesterNr>, <IncludeSemester>)
    filter.addSemester("BI", 3)
    # filter.addSemester("BCSP", 3)
    # filter.addSemester("BI", 2)
    # filter.addSemester("BI", 1)

    # TODO: ADD YOUR CODE HERE
    # USE addVL to add a Vorlesung that you want to include in your ical file
    # you can add a boolean value at the end of the function to decide if the VL should be included or not
    # addVL(<VLName>, <IncludeVL>)
    # For <VLName> you can look at the "cache/semester.json" file
    # filter.addVL("Diskrete Mathematik und Lineare Algebra")
    # filter.addVL("Grundlagen von Wahrscheinlichkeitstheorie und Statistik", group="4")
    # filter.addVL("Betriebssysteme", group="4")
    # filter.addVL("Einführung in die Automatentheorie und Formale Sprachen", group="4")
    # filter.addVL("Competitive Bots")

    # TODO: ADD YOUR CODE HERE
    # USE addContains to add the containing String to the ical file
    # addContains(<String>, <Key>, <IncludeString>)
    # <String> is the string that should be contained
    # <Key> is the key of the dictionary of the course data
    # for the <Key> you can look at the "cache/data.json" file
    # <IncludeString> is a boolean value that decides if the string should be contained or not
    # filter.addContains("Projekt-Seminar", "title", False)

    ################################################
    # DONT CHANGE THIS CODE
    # Apply the filter to the data
    newData = filter.filterCoursesByOptions()
    # Set the new data to the parser object
    p.updateData(newData)
    # Generate the calendar file
    p.generateCalendarFile()
    # DONT CHANGE THIS CODE
