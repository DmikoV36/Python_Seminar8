# import easygui as g
# import sys

# while 1:
#     g.msgbox('Привет, добро пожаловать в интерфейс заказа')

#     msg = "Какой кофе вы хотите выпить?"
#     title = "заказ"
#     choices = ['Карамель макиато', 'Ваниль Фуруи Уайт', "Ручной удар", "Капучино"]

#     choice = g.choicebox(msg, title, choices)

#     # Обратите внимание, что параметр msgbox - это строка
#     # Если пользователь выбирает Отмена, функция возвращает None
#     g.msgbox('Ваш выбор:' + str(choice), "результат")

#     msg = "Вы хотите снова начать выбирать?"
#     title = "пожалуйста, выбери"

#     # Вызвать диалог продолжения / отмены
#     if g.ccbox(msg, title):
#         pass  # Если пользователь выбирает Продолжить
#     else:
#         sys.exit(0)  # Если пользователь выбирает Отмена

from easygui import  *
egdemo()