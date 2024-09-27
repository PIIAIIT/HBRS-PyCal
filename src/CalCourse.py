# from src.exportData.option import Option
# class Course:
#     """
#     The Course class is used to create a Course object.
#     It is used to store the data of a course.
#
#     semesterName: Name of the semester
#     weekday: The weekday of the course
#     startTime: The start time of the course
#     endTime: The end time of the course
#     room: The room of the course
#     title: The title of the course
#     date: The date of the course
#     lecturer: The lecturer of the course
#     cleanTitle: The clean title of the course
#     type: The type of the course
#     group: The group of the course
#     parsedDate: The parsed date of the course
#     """
#
#     def __init__(self, data: dict[str, str]) -> None:
#         self.course: dict[str, str] = data
#         if (data is None):
#             self.course = {}
#
#     def __str__(self) -> str:
#         return str(self.course)
#
#     def __getitem__(self, key: str) -> str:
#         return self.course[key]
#
#     def check(self, option: Option) -> bool:
#         """
#         This function checks if the course fits the option
#         """
#         for key, value in self.course.items():
#             if option == value:
#                 return True
#         return False


class Calender:
    """
    This class represents a calendar
    """

    def __init__(self) -> None:
        self.termine: list[dict] = []

    def addCourse(self, c: dict) -> None:
        self.termine.append(c)

    def __iter__(self):
        return iter(self.termine)

    def fill(self, data: list[dict]) -> None:
        for d in data:
            self.addCourse(d)

    def __str__(self) -> str:
        return str(self.termine)
