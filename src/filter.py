from src.calendar import Calender
import json
import os
from src.option import Option, OptionContains, OptionSemester, OptionVL
from src.option import OptionLecturer, OptionType, OptionGroup, OptionWeekday

    

class CalenderFilter:
    def __init__(self, cal: Calender) -> None:
        self.cal = cal
        if not isinstance(self.cal, Calender):
            raise TypeError("The calender has to be of type Calender")

        self.availableOptions = self.extractAvailableOptions(cal)

        self.generateOptionFile()
        self.options: list[Option] = []

    def addOption(self, option: Option) -> None:
        """Adds an option to the filter"""
        if not option.isValid():
            raise ValueError("The option is not valid")
        self.options.append(option)

    def addContains(self, filter: str, option: str, contains: bool = True) -> None:
        """
        @Args: filter:      str        The contains string  
        @Args: option:      str        The Option that should be checked  
        @Args: contains:    bool       If the option should be included or excluded
        """
        self.addOption(OptionContains(filter, option, contains))

    def addSemester(self, semester: str, semesterNumber: int, contains: bool = True) -> None:
        """ 
        @Args: semName:     str        The name of the semester
        @Args: semester:    int        The number of the semester
        @Args: contains:    bool       If the option should be included or excluded
        """
        self.addOption(OptionSemester(semester, semesterNumber, contains))

    def addVL(self, titleVL: str, contains: bool = True, group: str = "") -> None:
        """ 
        @Args: titleVL:     str       The title of the VL
        @Args: contains:    bool      If the option should be included or excluded
        @Args: group:       str       (Optional) The group of the VL: will not include VL only Ü
        """
        self.addOption(OptionVL(titleVL, contains, group))

    def addLecturer(self, lecturer: str, contains: bool = True) -> None:
        """
        @Args: lecturer:    str      The name of the lecturer
        @Args: contains:    bool     If the option should be included or excluded
        """
        self.addOption(OptionLecturer(lecturer, contains))

    def addType(self, type_: str, contains: bool = True) -> None:
        """
        @Args: type_:       str      The type of the course: Vorlesung(V), Übung(Ü), Praktikum(P)
        @Args: contains:    bool     If the option should be included or excluded
        """
        self.addOption(OptionType(type_, contains))

    def addGroup(self, group: str, contains: bool = True) -> None:
        """Adds the group to the filter"""
        print("This function is not yet implemented")
        exit(1)
        self.addOption(OptionGroup(group, contains))

    def addWeekday(self, weekday: str, contains: bool = True) -> None:
        """Adds the weekday to the filter"""
        self.addOption(OptionWeekday(weekday, contains))

    def extractAvailableOptions(self, cal: Calender) -> dict[str, list[str]]:
        _semester = {}
        tmp = ""
        for course in cal.termine:
            if tmp != course["semesterName"] and tmp != "":
                _semester[tmp].sort()
            if course["semesterName"] not in _semester:
                _semester[course["semesterName"]] = [course["title"]]
            else:
                _semester[course["semesterName"]].append(
                    course["title"])
            tmp = course["semesterName"]

        return _semester

    def generateOptionFile(self) -> None:
        """Generates the option file"""
        cache_dir = os.getenv("PROJECT_DIR") if os.getenv("PROJECT_DIR") is None else os.getcwd() + "/cache/"
        assert cache_dir is not None
        with open(cache_dir + "semester.json", "w", encoding="utf-8") as f:
            json.dump(self.availableOptions, f, indent=4, ensure_ascii=False)

    def __contains(self, dupe: dict, courses: list[dict]) -> bool:
        """Checks if the course is already in the list"""
        for course in courses:
            if course["title"] == dupe["title"] and \
                    course["weekday"] == dupe["weekday"] and \
                    course["startTime"] == dupe["startTime"] and \
                    course["endTime"] == dupe["endTime"] and \
                    course["room"] == dupe["room"]:
                return True
        return False

    def filterCoursesByOptions(self) -> list[dict]:
        """Filters the data of the calender by the options

        @Args: cal: Calender    The calender that should be filtered
        @return: list[dict]     The data that fits the options
        """
        newData: list[dict] = []

        # default case it no options are set
        if len(self.options) == 0:
            return self.cal.termine

        include = []
        exclude = []
        # iterate through the courses
        for course in self.cal:
            # look at every value in the course
            # compare it to every option
            # if it fits, add it to the new data
            # if include is False, the course has not to match
            for opt in self.options:
                # if include is True, the course has to match the option
                # matches = self.__matchesOption(course, opt.getName())
                matches = opt.checkCourse(course)  # valid
                bInclude = opt.getInclude()

                if not matches:
                    continue
                if bInclude:
                    if not self.__contains(course, include):
                        include.append(course)
                    if course in exclude:
                        exclude.remove(course)
                else:
                    exclude.append(course)

        # logic for include and exclude
        for course in include:
            if course not in exclude:
                newData.append(course)

        if len(newData) == 0:
            print("No courses found")
            exit(1)

        # write the new data to a cache file
        cache_dir = os.getenv("PROJECT_DIR") if os.getenv("PROJECT_DIR") is None else os.getcwd() + "/cache/"
        assert cache_dir is not None
        f = open(cache_dir + "after.json",
                 "w", encoding="utf-8")
        json.dump(newData, f, indent=4, ensure_ascii=False)
        f.close()

        return newData
