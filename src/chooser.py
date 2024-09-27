
from src.CalCourse import Calender


class CalendarFilter:
    def __init__(self):
        self.options: list[str] = []

    def addOption(self, option: str) -> None:
        self.options.append(option)

    def _check(self, course: dict, option: str) -> bool:
        """Checks if the course fits the option"""
        for key, value in course.items():
            if value == option:
                return True
        return False

    def by_options(self, cal: Calender) -> list[dict]:
        """Filters the data of the calender by the options

        @Args: cal: Calender    The calender that should be filtered
        @return: list[dict]     The data that fits the options
        """
        if not isinstance(cal, Calender):
            raise TypeError("The calender has to be of type Calender")

        newData: list[dict] = []

        if not self.options:
            return cal.termine

        for course in cal:
            # look at every value in the course
            # compare it to every option
            # if it fits, add it to the new data
            for option in self.options:
                if self._check(course, option):
                    newData.append(course)
                    break

        return newData
