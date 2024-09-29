from calendar import Calender
import json
import os
from option import Option, OptionContains, OptionSemester, OptionVL, OptionLecturer, OptionType, OptionGroup, OptionWeekday


class CalendarFilter:
    def __init__(self, cal: Calender) -> None:
        self.cal = cal
        if not isinstance(self.cal, Calender):
            raise TypeError("The calender has to be of type Calender")

        self.availableOptions = self.extractAvailableOptions(cal)

        self.options: list[Option] = []

    def addOption(self, option: Option) -> None:
        """Adds an option to the filter"""
        # TODO: check if the option is valid
        # - check every Option subtype
        if not isinstance(option, Option):
            raise TypeError("The option has to be of type Option")
        if not option.isValid():
            raise ValueError("The option is not valid")
        self.options.append(option)

    def addContains(self, filter: str, option: str, contains: bool = True) -> None:
        """Adds the courses that contains the arg to the filter """
        self.addOption(OptionContains(filter, option, contains))

    def addSemester(self, semester: str, semesterNumber: int, contains: bool = True) -> None:
        """Adds the semester to the filter"""
        self.addOption(OptionSemester(semester, semesterNumber, contains))

    def addVL(self, titleVL: str, contains: bool = True) -> None:
        """Adds the VL to the filter"""
        self.addOption(OptionVL(titleVL, contains))

    def addLecturer(self, lecturer: str, contains: bool = True) -> None:
        """Adds the lecturer to the filter"""
        self.addOption(OptionLecturer(lecturer, contains))

    def addType(self, type_: str, contains: bool = True) -> None:
        """Adds the type to the filter"""
        self.addOption(OptionType(type_, contains))

    def addGroup(self, group: str, contains: bool = True) -> None:
        """Adds the group to the filter"""
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
        with open("./cache/semester.json", "w", encoding="utf-8") as f:
            json.dump(self.possibleOptions, f, indent=4, ensure_ascii=False)

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
                    include.append(course)
                else:
                    exclude.append(course)

        # logic for include and exclude
        for course in include:
            if course not in exclude:
                newData.append(course)

        # write the new data to a cache file
        cache_dir = os.path.abspath(__file__).split("test")[0] + "cache/"
        f = open(cache_dir + "after.json",
                 "w", encoding="utf-8")
        json.dump(newData, f, indent=4, ensure_ascii=False)
        f.close()

        return newData


def getDataFromJson() -> list[dict]:
    cache_dir = os.path.abspath(__file__).split("test")[0] + "cache/"
    with open(cache_dir + "data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    cal = Calender()
    data = getDataFromJson()
    cal.fill(data)

    filter = CalendarFilter(cal)
    filter.addSemester("BI", 3)
    filter.addSemester("BI", 1)
    filter.addVL("Diskrete Mathematik und Lineare Algebra")
    filter.addContains("Projekt-Seminar", "title", False)
    filter.addVL("Competitive Bots")
    newData = filter.filterCoursesByOptions()

    # for i in range(newData.__len__()):
    #     print(newData[i]["title"])
