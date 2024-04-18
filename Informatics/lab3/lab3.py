import re


def point_1(): 
    print('Задание 1.')
    point1=["Штирлиц гулял вокруг пруда и смотрел на уток: \n«Утки», - подумал Штирлиц. \n«долбо=-P», - подумали гуси.\n",
        "Если вселенная бесконечна действительно, значит есть куча копий нашей планеты =-P. \nГде-то сейчас происходят те же события, копия меня пишет копию песни этой. =-P \n",
        "Полковнику никто не пишет, \nполковника никто не ждёт. \nНа линии огня \nпустые города, \nв которых никогда \nты раньше не бывала =-(\n",
        "Нашла коса на камень= -P, \nидет война на память лет.=-P\n",
        "Я на тебе, как на войне, а на войне как на тебе,\nно я устал, окончен бой, беpу поpтвейн иду домой.\nОкончен бой, зачах огонь и не осталось ничего,\nа мы живём, а нам с тобою повезло назло"]
    pattern = re.compile('=-P')
    for x in point1:
        print(len(pattern.findall(x)),end="\n\n")

def point_2(): 
    print('Задание 2.')
    point2=['Уважаемые студенты! В эту субботу в 1500:00 планируется доп. занятие на 2 часа. То есть в 17:00:01 оно уже точно кончится.',
        'Привет, братва, встречаемся 23 числа в 23:59 на вокзале',
        'أطلب من الجامعة أن تفصلني بمحض إرادتي',
        'Прошу отчислить меня из университета по собственному желанию после 28:00, хочу попить кофе в не_столовой!',
        'Не душите, пожалуйста, время 01:10:10:01, а я пишу эту лабу']
    pattern2 = re.compile('( [01][0-9]|2[0-3])(:([0-5][0-9])){1,2} ')
    for y in point2:
        if pattern2.search(y):
            print(re.sub(pattern2, ' (TBD) ',y),end="\n\n")
        else:
            print(y, '\n')
        

def point_3():
    print('Задание 3.')
    point3=['google@niu@itmo.ru','sob-aka@sobaka.com', 'world.of.warcraft@niuitmo.ru', 'zeliboba_2003.gmail.com', 'zaycev.net@g.mail.ru.', '____@gmail.com']
    point3_1=['students.spam@yandex.ru', 'example@example', 'example@example.com']
    pattern3 = re.compile('([\w .]+)@([a-zA-Z0-9]+\.[a-zA-Z0-9.]+\w)')
    for z in (point3 + point3_1):
        res = pattern3.fullmatch(z)
        if res:
            print(res.group(2))
        else:
            print('Fail!')

def main ():
    point_1()
    point_2()
    point_3()
if __name__ == '__main__':
    main()
#C:\Users\fergee\AppData\Local\Programs\Python\Python310\python.exe
