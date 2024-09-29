import difflib
import datetime as dt


class Option:
    threshold = 0.55

    def __init__(self, name: str, include: bool) -> None:
        self.optionName = name  # 'Competitive Bots'
        self.include = include  # True

    def getOptionName(self) -> str:
        return self.optionName

    def getInclude(self) -> bool:
        return self.include

    def checkCourse(self, course: dict[str, str]) -> bool:
        raise NotImplementedError("Subclass must implement abstract method")

    def isValid(self) -> bool:
        """Checks if the option is valid"""
        if self.optionName is not None and self.optionName != "":
            return True
        return False


class OptionContains(Option):
    def __init__(self, name: str, option: str, include: bool) -> None:
        """
        @Args: name:    str        The contains string
               include: bool       If the option should be included or excluded
               option:  str        The Option that should be checked
        """
        super().__init__(name, include)
        self.option = option

    def checkCourse(self, course: dict[str, str]) -> bool:
        b = course[self.option] is not None and self.optionName \
            in course[self.option]
        return b


class OptionSemester(Option):
    def __init__(self, semName: str, semester: int, include: bool) -> None:
        super().__init__(str.join(" ", [semName, str(semester)]), include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        b = course["semesterName"] == self.optionName
        return b


class OptionVL(Option):
    def __init__(self, name: str, include: bool) -> None:
        super().__init__(name, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        # print(course["title"], "does not match", self.name, ratio)
        b = difflib.SequenceMatcher(None, course["title"].lower(),
                                    self.optionName.lower()).ratio() \
            >= Option.threshold
        return b


class OptionLecturer(Option):
    def __init__(self, name: str, include: bool) -> None:
        super().__init__(name, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        return course["lecturer"] == self.optionName


class OptionType(Option):
    def __init__(self, _type: str, include: bool) -> None:
        super().__init__(_type, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        if course["type"] is not None and course["type"] is not []:
            for t in course["type"]:
                if self.optionName in t:
                    return True
            return False
        return False


class OptionGroup(Option):
    def __init__(self, group: str, include: bool) -> None:
        super().__init__(group, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        return course["group"] is not None and \
            self.optionName.upper() in course["group"]


class OptionWeekday(Option):
    def __init__(self, weekday: str, include: bool) -> None:
        super().__init__(weekday, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        a = dt.datetime.strptime(course["weekday"], "%A")
        b = dt.datetime.strptime(self.optionName, "%A")
        return a == b
