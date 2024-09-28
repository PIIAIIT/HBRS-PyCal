import os
from datetime import datetime
import uuid
PATH = os.getenv("PROJECT_DIR")


def createCalendarFile(data: list[dict]) -> None:
    """Writes the ical file
    :param data: The data to write as a list of dictionaries"""
    # all conventions are based on the icalendar standard
    fileName = "stundenplan"
    fileExt = "ical"
    __x = 5
    print(f"(1/{__x}) Writing ical file...")

    # check if the file already exists
    # and create a new one if necessary
    print(f"(2/{__x}) Creating new file...")
    calenderFilePath = f"/output/{fileName}"
    os.makedirs(PATH + "/output", exist_ok=True)
    for i in range(1, 100):
        tempPath = f"/output/{fileName}({i}).{fileExt}" \
            if i else calenderFilePath
        if not os.path.exists(PATH + tempPath):
            calenderFilePath = tempPath
            break
    print(f"(3/{__x}) File created: {calenderFilePath}")

    print(f"(4/{__x}) Writing to: {calenderFilePath}")
    with open(PATH + calenderFilePath, "w", encoding="utf-8") as f:
        # Calender Header
        f.write("BEGIN:VCALENDAR\n")

        f.write("VERSION:2.0\n")
        f.write("PRODID:Patrick Saft @PIIAIIT\n")
        f.write("CALSCALE:GREGORIAN\n")
        f.write("METHOD:PUBLISH\n")
        f.write("X-WR-CALNAME:Stundenplan H-brs\n")
        f.write("X-WR-TIMEZONE:Europe/Berlin\n")
        f.write("X-WR-CALDESC:Stundenplan von der " +
                "www.kalenderapp.aptinstall.de\\nSeite\n")

        # Events
        for __lv in data:
            try:
                startDate = datetime.strptime(
                    __lv["parsedDate"]["start"], "%d.%m.%Y")
                endDate = datetime.strptime(
                    __lv["parsedDate"]["end"], "%d.%m.%Y")
                weeks = endDate - startDate
                eventStartTime = datetime(startDate.year,
                                          startDate.month,
                                          startDate.day,
                                          int(__lv["startTime"].split(":")[0]),
                                          int(__lv["startTime"].split(":")[1]))
                eventEndTime = datetime(startDate.year,
                                        startDate.month,
                                        startDate.day,
                                        int(__lv["endTime"].split(":")[0]),
                                        int(__lv["endTime"].split(":")[1]))
                interval = 1
                __tmp = __lv.get("parsedDate", {"info": "KW ()"})
                if not __tmp.get("info", "").split(" ")[0].startswith("KW"):
                    interval = 2

            except Exception:
                print(f"Error while parsing: {__lv}")
                continue

            f.write("BEGIN:VEVENT\n")
            f.write("DTSTART;TZID=Europe/Berlin:" +
                    eventStartTime.strftime("%Y%m%dT%H%M%S") + "\n")
            f.write("DTEND;TZID=Europe/Berlin:" +
                    eventEndTime.strftime("%Y%m%dT%H%M%S") + "\n")
            f.write(f"RRULE:FREQ=WEEKLY;COUNT={weeks.days//7};" +
                    f"INTERVAL={interval}" + "\n")
            f.write(
                f"DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n")
            f.write("UID:"+str(uuid.uuid4())+"\n")
            f.write("CREATED:"+datetime.now().strftime('%Y%m%dT%H%M%SZ')+"\n")
            f.write("DESCRIPTION:"+__lv.get("title") + " in Raum: " +
                    __lv.get("room") + " bei: " + __lv.get("lecturer") + "\n")
            f.write("LOCATION:"+__lv.get("room")+"\n")
            f.write("SUMMARY:"+__lv.get("title")+"\n")
            f.write("END:VEVENT\n")
        # Events

        # Calender Footer
        f.write("END:VCALENDAR")
    print(f"(5/{__x}) Writing done.")
