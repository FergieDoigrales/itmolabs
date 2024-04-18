NUMBER_CHARS = [str(i) for i in range(0,10)]
WORDS = 'day time room subject lesson teacher location parity format weeks'.split(' ')
COMMA = ','
import time

def match_lesson(s):
    word = ''
    for j in range(len(s)):
            word = word + s[j]
            if word == 'lesson' and s[j+1] in NUMBER_CHARS:
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
    for line in lines:
        if timetable_start:
            if line.count("  ", 0, 2) ==0: #проверяем не закончилась ли таблица
                break
            else:
                line = line.replace("\n", "").replace("  ", "").replace(": ", ":")
                if "day" in line:
                    key, word = parse_line(line)
                    schedule.day = word
                elif match_lesson(line) and len(lesson)!=0:
                    schedule.lessons.append(lesson)
                    lesson = dict()
                else:
                    key, word = parse_line(line)
                    if key in WORDS:
                        lesson[key] = word
        if "timetable" in line:
            timetable_start = True

    schedule.lessons.append(lesson)
    return schedule

def file_to_csv(file):
    schedule = parse_file(file)
    csv = ""
    csv += "timetable.day"+COMMA
    for i in range(len(schedule.lessons)):
        lesson = schedule.lessons[i]
        for key in lesson:
            csv += f"timetable.lesson{i+1}.{key}"
            #проверка на последний элемент, чтобы не было запятой в конце
            if i == len(schedule.lessons)-1 and list(lesson.keys())[-1] == key:
                pass
            else:
                csv += COMMA
    csv += "\n"
    csv += schedule.day + COMMA
    for i in range(len(schedule.lessons)):
        lesson = schedule.lessons[i]
        for key in lesson:
            #если в строке есть запятая то надо заключить в кавычки
            if COMMA in lesson[key]:
                csv += f'"{lesson[key]}"'
            else:
                csv += f"{lesson[key]}"
            if i == len(schedule.lessons)-1 and list(lesson.keys())[-1] == key:
                pass
            else:
                csv += COMMA
    return csv

def convert_file(input_file_name, output_file_name, show = False):
    input_file = open(input_file_name + ".yml", 'r', encoding='utf-8') 
    output_file = open(output_file_name + ".csv",'w', encoding = "utf-8")
    csv = file_to_csv(input_file)
    output_file.write(csv)
    input_file.close()
    output_file.close()
    if show:
        print(csv)

convert_file("timetable","timetable",True)
