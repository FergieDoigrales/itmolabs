import re

class Timetable:
    def __init__(self):
        self.lessons = []
        self.day = ""

def parse_file(file):
    schedule = Timetable()
    timetable_start = False
    key_value = re.compile(r"\s*(\w+):\s*(.*)")
    for line in file.readlines():
        line=line[:-1]
        if timetable_start:
            if re.fullmatch(r"(\s)+day:\s*(\w*)",line):
                word = key_value.search(line).group(2)
                schedule.day = word
            elif re.fullmatch(r"\s*lesson\d+:",line):
                schedule.lessons.append({})
            else:
                groups = key_value.search(line)
                schedule.lessons[-1][groups.group(1)] = groups.group(2)
        elif "timetable" in line:
            timetable_start = True
    return schedule

def file_to_xml(file):
    schedule = parse_file(file)
    xml = "<timetable>\n"
    xml+=f"\t<day>{schedule.day}</day>\n"
    for i in range(len(schedule.lessons)):
        lesson = schedule.lessons[i]
        xml += f"\t<lesson{i+1}>\n"
        for p in lesson:
            xml += f"\t\t<{p}>{lesson[p]}</{p}>\n"
        xml += f"\t</lesson{i+1}>\n"
    xml += "</timetable>"
    return xml

def convert_file(input_file_name, output_file_name):
    with open(f"{input_file_name}.yml", "r",  encoding='utf-8') as file:
        xml = file_to_xml(file)
    with open(f"{output_file_name}.xml", "w",  encoding='utf-8') as file:
        file.write(xml)


if __name__ == "__main__":
    import time
    t_start = time.perf_counter()
    convert_file("timetable","timetable")
    print("time: ",time.perf_counter() - t_start)
