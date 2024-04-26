
class Option:

    def __init__(self, studiengang: str, semester: int) -> None:
        r"""Creates a Option object.
        :param studiengang: Studiengang den du besuchst (BCSP, BI, BWI, ZUSATZ(für Zusatzveranstaltungen)
        :param semester: Semester in dem du dich befindest (1, 2, 3, 4, 5, 6)
        - Example: Option("BI", 2)
        """
        self.studiengang = studiengang
        self.semester = semester
    
class OptionList:

    options: Option = []

    def __init__(self, *options: Option) -> None:
        """Creates an OptionList object.
        :param options: The options to add to the list
        - Example: OptionList(Option("BWI", 4), Option("BI", 2))"""
        for arg in options:
            self.options.append(arg)
    
    def add_option(self, option: Option) -> None:
        self.options.append(option)

    def get_options(self) -> list[Option]:
        return self.options
