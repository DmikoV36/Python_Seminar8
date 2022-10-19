#функционал:
    # доб учениками
    # удалить учениками
    # выборка
        # все ученики класса
        # все отличники(хорошисты, троечники)
        # именинники месяца
        # по фио номер тел
        # вся информациипо фио
        # по фио класс руковод???

from easygui import *

msg = "Выберите дальнейшее действие: "
title = "Информация об учениках школы № ?"
choices = ['Добавить информацию об ученике', 'Удалить информацию об ученике', 'Редактировать информацию об ученике', 'Поиск информации']
choice = choicebox(msg, title, choices)

if choice == choices[0]:
    msg = "Введите информацию об ученике: "
    title = "Ввод информации об ученике"
    fieldNames  =  ["ФИО","Дата рождения","Класс","Классный руководитель","Адрес","Телефон родителя","Средняя успеваемость"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)
    while True:
        if fieldValues == None: break
        errmsg = ""
        for i in range (len(fieldNames)-1):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" это обязательные поля.\n\n' % fieldNames[i])
        if errmsg == "":
            break # no problems found
        fieldValues = multenterbox(errmsg, title,  fieldNames, fieldValues)
    print ("Введена инфомация:", fieldValues)

if choice == choices[1]:
    msg = "Введите ФИО ученика: "
    title = "Удаление информации об ученике"
    fieldNames  =  ["ФИО"]
    fieldValues = []
    fieldValues = multenterbox(msg, title, fieldNames)

if choice == choices[2]:
    msg = "Выберите данные для редактирования: "
    title = "Редактирование данных об ученике"
    choices = ["ФИО","Дата рождения","Класс","Классный руководитель","Адрес","Телефон родителя","Средняя успеваемость"]
    overwriting = multchoicebox(msg, title, choices)
    if choices[3]:
        msg = "Введите информацию об ученике: "
        title = "Ввод информации об ученике"
        fieldNames  =  overwriting
        fieldValues = []
        fieldValues = multenterbox(msg, title, fieldNames)

if choice == choices[3]:
    msg = "Выберите шаблон поиска: "
    title = "Поиск информации"
    choices = ['Информация об ученике', 'Классный руководитель ученика', 'Телефон родителя', 'Ученики класса', 'Именинники месяца', 'Выборка по успеваемости']
    choice = choicebox(msg, title, choices)
    if choice == choices[5]:
        msg = "Выберите шаблон поиска: "
        title = "Успеваемость"
        choices = ['Отличники', 'Хорошисты', 'Троечники']
        choice = choicebox(msg, title, choices)