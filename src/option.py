import difflib


class Option:
    threshold = 0.55

    def __init__(self, name: str, include: bool) -> None:
        self.name = name  # 'Competitive Bots'
        self.include = include  # True

    def getName(self) -> str:
        return self.name

    def getInclude(self) -> bool:
        return self.include

    def isValid(self) -> bool:
        """Checks if the option is valid"""
        if self.name is not None and self.name != "":
            return True
        return False


class OptionContains(Option):
    def __init__(self, name: str, include: bool) -> None:
        super().__init__(name, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        for key, value in course.items():
            if self.name in value:
                return True
        return False


class OptionSemester(Option):
    def __init__(self, semName: str, semester: int, include: bool) -> None:
        super().__init__(str.join(" ", [semName, str(semester)]), include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        return course["semesterName"] == self.name


class OptionVL(Option):
    def __init__(self, name: str, include: bool) -> None:
        super().__init__(name, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        ratio = difflib.SequenceMatcher(
            None, course["title"].lower(), self.name.lower()).ratio()
        # print(course["title"], "==", self.name, ratio)
        return ratio >= Option.threshold


class OptionLecturer(Option):
    def __init__(self, name: str, include: bool) -> None:
        super().__init__(name, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        return course["lecturer"] == self.name


class OptionType(Option):
    def __init__(self, _type: str, include: bool) -> None:
        super().__init__(_type, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        if course["type"] is not None and course["type"] is not []:
            for t in course["type"]:
                if self.name in t:
                    return True
            return False
        return False


class OptionGroup(Option):
    def __init__(self, group: str, include: bool) -> None:
        super().__init__(group, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        if course["group"] is not None and self.name in course["group"]:
            return True
        return False


class OptionWeekday(Option):
    def __init__(self, weekday: str, include: bool) -> None:
        super().__init__(weekday, include)

    def checkCourse(self, course: dict[str, str]) -> bool:
        return course["weekday"] == self.name
