import os
import datetime as dt
import uuid


def writeToFile(path:str, data:str) -> None:
    print(f"(4/{max}) Writing to: {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)
    print(f"(5/{max}) Writing done.")

def icalFormat(data: list[dict]) -> str:
    s = ""
    # Calender Header
    s+="BEGIN:VCALENDAR\n"
    s+="VERSION:2.0\n"
    s+="PRODID:Patrick Saft @PIIAIIT\n"
    s+="CALSCALE:GREGORIAN\n"
    s+="METHOD:PUBLISH\n"
    s+="X-WR-CALNAME:Stundenplan H-brs\n"
    s+="X-WR-TIMEZONE:Europe/Berlin\n"
    s+="X-WR-CALDESC:Diese App referenziert den iCalGenerator von @Hochgesand\n"

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

        s+="BEGIN:VEVENT\n"
        s+="DTSTART;TZID=Europe/Berlin:" + eventStartTime.strftime("%Y%m%dT%H%M%S") + "\n"
        s+="DTEND;TZID=Europe/Berlin:" + eventEndTime.strftime("%Y%m%dT%H%M%S") + "\n"
        s+=f"RRULE:FREQ=WEEKLY;COUNT={int((weeks.days//7) / interval)};" + f"INTERVAL={interval}" + "\n"
        s+=f"DTSTAMP:{dt.datetime.now().strftime('%Y%m%dT%H%M%SZ')}\n"
        s+="UID:"+str(uuid.uuid4())+"\n"
        s+="CREATED:"+dt.datetime.now().strftime('%Y%m%dT%H%M%SZ')+"\n"
        s+="DESCRIPTION:" +lv.get("title", "") + " in Raum: " + lv.get("room") + " bei: " + lv.get("lecturer") + "\n"
        s+="LOCATION:"+lv.get("room", "")+"\n"
        s+="SUMMARY:"+lv.get("title", "")+"\n"
        s+="END:VEVENT\n"
    # Events

    # Calender Footer
    s+="END:VCALENDAR"
    return s

def createiCalFile(data: list[dict], abfrage=True) -> None:
    """Writes the ical file
    :param data: The data to write as a list of dictionaries"""
    # all conventions are based on the icalendar standard
    PROJECT_DIR = os.getenv("PROJECT_DIR") if os.getenv("PROJECT_DIR") is not None else os.getcwd()
    assert PROJECT_DIR is not None, "PROJECT_DIR is not set" 

    ext = {1: "ics", 2: "ical", 3: "ifb", 4:"icalendar"}
    if abfrage:
        fileName = input("Enter the filename: (Standard: Stundenplan)") or "Stundenplan"
        inp = input("Enter the file extension 1: ics, 2: ical, 3: ifb, 4: icalendar (Voreinstellung: 1):")
    else:
        fileName = "Stundenplan"
        inp = 1 # "ics"
    fileExt = ext.get(int(inp) if inp in ext.keys() else 1)
    print("(1/5) Writing ical file...")

    # check if the file already exists
    # and create a new one if necessary
    print("(2/5) Checking if Path exists...")
    calenderFilePath = f"/output/{fileName}"
    os.makedirs(PROJECT_DIR + "/output", exist_ok=True)
    for i in range(0, 100):
        tempPath = f"/output/{fileName}({i}).{fileExt}" \
            if i else calenderFilePath + f".{fileExt}"
        if not os.path.exists(PROJECT_DIR + tempPath):
            calenderFilePath = tempPath
            break
    print(f"(3/5) Saving File to: {calenderFilePath}")

    writeToFile(PROJECT_DIR + calenderFilePath, icalFormat(data))
