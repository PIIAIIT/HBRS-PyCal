class Calender:
    """
    This class represents a calendar
    """

    def __init__(self) -> None:
        self.termine: list[dict] = []

    def addCourse(self, c: dict) -> None:
        self.termine.append(c)

    def fill(self, data: list[dict]) -> None:
        for d in data:
            self.addCourse(d)

    def __iter__(self):
        return iter(self.termine)

    def __str__(self) -> str:
        return str(self.termine)
