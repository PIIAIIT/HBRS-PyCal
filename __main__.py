from src.calendar import Calender
from src.filter import CalendarFilter
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
    filter = CalendarFilter(cal)

    # TODO: ADD YOUR CODE HERE
    # USE addSemester to add a Semester that you want to include in your ical file
    # you can add a boolean value at the end of the function to decide if the semester should be included or not
    # addSemester(<SemsterName>, <SemesterNr>, <IncludeSemester>)
    filter.addSemester("BI", 3)
    # filter.addSemester("BI", 1)

    # TODO: ADD YOUR CODE HERE
    # USE addVL to add a Vorlesung that you want to include in your ical file
    # you can add a boolean value at the end of the function to decide if the VL should be included or not
    # addVL(<VLName>, <IncludeVL>)
    # For <VLName> you can look at the "cache/semester.json" file
    filter.addVL("Diskrete Mathematik und Lineare Algebra")

    # TODO: ADD YOUR CODE HERE
    # USE addContains to add the containing String: arg[0] to the ical file
    # arg[1] is the key of the dictionary of the course data
    # arg[2] is a boolean value that decides if the string should be contained or not
    # addContains(<String>, <Key>, <IncludeString>)
    # for the <Key> you can look at the "cache/data.json" file
    filter.addContains("Projekt-Seminar", "title", False)

    # TODO: ADD YOUR CODE HERE
    # YOU CAN include Options that you previously excluded
    filter.addVL("Competitive Bots")

    ################################################
    # DONT CHANGE THIS CODE
    # Apply the filter to the data
    newData = filter.filterCoursesByOptions()
    # Set the new data to the parser object
    p.updateData(newData)
    # Generate the calendar file
    p.generateCalendarFile()
    # DONT CHANGE THIS CODE
