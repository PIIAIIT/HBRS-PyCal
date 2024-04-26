
class Option:

    def __init__(self, studiengang: str, semester: int, veranstaltung: str="", professor: str ="") -> None:
        r"""Creates a Option object.
        :param studiengang: Studiengang den du besuchst (BCSP, BI, BWI, ZUSATZ(für Zusatzveranstaltungen)
        :param semester: Semester in dem du dich befindest (1, 2, 3, 4, 5, 6)
        :param veranstaltung: (Optional) Name der Veranstaltung
        :param professor: (Optional) Name des Professors
        - Example: Option("BI", 2, "Programmierung in C", "Böhmer")
        """
        self.studiengang = studiengang
        self.semester = semester
        self.veranstaltung = veranstaltung
        self.professor = professor
    
class OptionList:

    options: Option = []

    def __init__(self, *options: Option) -> None:
        for arg in options:
            self.options.append(arg)
    
    def add_option(self, option: Option) -> None:
        self.options.append(option)

    def get_options(self) -> list[Option]:
        return self.options