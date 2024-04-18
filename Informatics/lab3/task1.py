import time

obj = [str(i) for i in range(0,10)]
t_start = time.perf_counter()
yml_obj = 'day time place subject lesson teacher location format weeks'.split(' ')

def match_lesson(s):
    word = ''
    for j in range(len(s)):
        word = word + s[j]
        if word == 'lesson' and s[j+1] in obj:
            return True
    return False

class Timetable:
    def __init__(self):
        self.lessons = []
        self.day = ""

def parse_line(line):
    line = line.replace("  ", "").replace('\n','')
    key, word = line.split(":", 1)
    return key, word

def parse_file(file):
    lines = file.readlines()
    schedule = Timetable()
    lesson = dict()
    timetable_start = False
    last_key = ""
    for line in lines:
        if timetable_start:
            if line.count("  ", 0, 2) ==0: 
                break
            else:
                line = line.replace("\n", "").replace("  ", "").replace(": ", ":")
                if line.replace(' ','').startswith('-'):
                    lesson[last_key].append(line.replace(' ','').replace('-',''))
                elif "day" in line:
                    key, word = parse_line(line)
                    schedule.day = word
                elif match_lesson(line) and len(lesson)!=0:
                    schedule.lessons.append(lesson)
                    lesson = dict()
                else:
                    key, word = parse_line(line)
                    if word == '':
                        word = []
                        last_key = key
                    if key in yml_obj:
                        lesson[key] = word
        if "timetable" in line:
            timetable_start = True

    schedule.lessons.append(lesson)
    return schedule

def file_to_xml(file):
    schedule = parse_file(file)
    xml = "<timetable>\n"
    xml+=f"\t<day>{schedule.day}</day>\n"
    for i in range(len(schedule.lessons)):
        lesson = schedule.lessons[i]
        xml += f"\t<lesson{i+1}>\n"
        for p in lesson:
            if isinstance(lesson[p],list):
                for x in lesson[p]:
                     xml += f"\t\t<{p}>{x}</{p}>\n"
                continue
            xml += f"\t\t<{p}>{lesson[p]}</{p}>\n"
        
        xml += f"\t</lesson{i+1}>\n"
    xml += "</timetable>"
    return xml

def convert_file(input_file_name, output_file_name, show = False):
    input_file = open(input_file_name + ".yml", 'r', encoding='utf-8') 
    output_file = open(output_file_name + ".xml",'w', encoding = "utf-8")
    xml = file_to_xml(input_file)
    output_file.write(xml)
    input_file.close()
    output_file.close()
    if show:
        print(xml)

convert_file("timetable","timetable",True)

start_time = 0
for n in range(10):
    t_start = time.perf_counter()
    convert_file("timetable","timetable")
print("time: ",time.perf_counter() - t_start)
