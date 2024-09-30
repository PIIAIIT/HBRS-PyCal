import os
import datetime as dt
import uuid

def createiCalFile(data: list[dict]) -> None:
    """Writes the ical file
    :param data: The data to write as a list of dictionaries"""
    PROJECT_DIR = os.getenv("PROJECT_DIR") if os.getenv("PROJECT_DIR") is not None else os.getcwd()
    # all conventions are based on the icalendar standard
    assert PROJECT_DIR is not None, "PROJECT_DIR is not set" 
    fileName = input("Enter the filename: (Standard: Stundenplan)") or "Stundenplan"
    fileExt = input("Enter the file extension 1: ical, 2: ics (Voreinstellung: 1):") or "ical"
    max = 5
    print(f"(1/{max}) Writing ical file...")

    # check if the file already exists
    # and create a new one if necessary
    print(f"(2/{max}) Creating new file...")
    calenderFilePath = f"/output/{fileName}"
    os.makedirs(PROJECT_DIR + "/output", exist_ok=True)
    for i in range(0, 100):
        tempPath = f"/output/{fileName}({i}).{fileExt}" \
            if i else calenderFilePath + f".{fileExt}"
        if not os.path.exists(PROJECT_DIR + tempPath):
            calenderFilePath = tempPath
            break
    print(f"(3/{max}) File created: {calenderFilePath}")

    print(f"(4/{max}) Writing to: {calenderFilePath}")
    with open(PROJECT_DIR + calenderFilePath, "w", encoding="utf-8") as f:
        # Calender Header
        f.write("BEGIN:VCALENDAR\n")

        f.write("VERSION:2.0\n")
        f.write("PRODID:Patrick Saft @PIIAIIT\n")
        f.write("CALSCALE:GREGORIAN\n")
        f.write("METHOD:PUBLISH\n")
        f.write("X-WR-CALNAME:Stundenplan H-brs\n")
        f.write("X-WR-TIMEZONE:Europe/Berlin\n")
        f.write("X-WR-CALDESC:" +
                "Diese App referenziert den iCalGenerator von @Hochgesand\n")

        # Events
        for lv in data:
            try:
                startDate = dt.datetime.strptime(
                    lv["parsedDate"]["start"], "%d.%m.%Y")
                endDate = dt.datetime.strptime(
                    lv["parsedDate"]["end"], "%d.%m.%Y")
                weeks = endDate - startDate
                eventStartTime = dt.datetime(startDate.year, startDate.month, startDate.day,
                                             int(lv["startTime"].split(":")[0]),
                                             int(lv["startTime"].split(":")[1]))
                eventEndTime = dt.datetime(startDate.year, startDate.month, startDate.day,
                                           int(lv["endTime"].split(":")[0]),
                                           int(lv["endTime"].split(":")[1]))
                interval = 1
                tmp = lv.get("parsedDate", {"info": "KW ()"})
                info = tmp.get("info", "")
                if not info.startswith("KW"):
                    interval = 2

            except Exception as e:
                print(e)
                print(f"Error while parsing: {lv}")
                continue

            f.write("BEGIN:VEVENT\n")
            f.write("DTSTART;TZID=Europe/Berlin:" +
                    eventStartTime.strftime("%Y%m%dT%H%M%S") + "\n")
            f.write("DTEND;TZID=Europe/Berlin:" +
                    eventEndTime.strftime("%Y%m%dT%H%M%S") + "\n")
            f.write(f"RRULE:FREQ=WEEKLY;COUNT={int((weeks.days//7) / interval)};" +
                    f"INTERVAL={interval}" + "\n")
            f.write(
                f"DTSTAMP:{dt.datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n")
            f.write("UID:"+str(uuid.uuid4())+"\n")
            f.write("CREATED:"+dt.datetime.now().strftime('%Y%m%dT%H%M%SZ')+"\n")
            f.write("DESCRIPTION:" +lv.get("title", "") + " in Raum: " +
                    lv.get("room") + " bei: " + lv.get("lecturer") + "\n")
            f.write("LOCATION:"+lv.get("room", "")+"\n")
            f.write("SUMMARY:"+lv.get("title", "")+"\n")
            f.write("END:VEVENT\n")
        # Events

        # Calender Footer
        f.write("END:VCALENDAR")
    print(f"(5/{max}) Writing done.")
