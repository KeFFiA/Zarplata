import tkinter as tk
from tkinter import WORD


def make_window_info():
    text = ("""Данная программа предназначена для быстрого просчета заработанной платы сотрудников предприятия
    
Чтобы правильно пользоваться программой, необходимо:

1. Подготовить таблицу в MSExel:
    1.1. В первой строке таблицы могут находиться названия столбцов
    1.2. В первом столбце должны находится имена сотрудников
    1.3. Во втором столбце должны находится название предприятий(-я)
    1.4. В третьем столбце должны находиться должности сотрудников
    1.5. В последующих столбцах должны находиться явки сотрудников в отработанных часах:минутах
    
2. Подготовить список сотрудников:
    2.1. В верхней части окна нажать "Таблица"
    2.2. Нажать "Добавить сотрудника"
    2.3. В новом окне внести данные сотрудника: Имя, Должность, Ставка, Цвет(указывается для удобного оформления таблицы)
    2.4. Сохранить 

3. Указать путь к файлу MSExel

4. Указать папку для сохранения файла(если не указать, тогда файл сохранится в папку с исходным файлом)

После всех манипуляций файл будет сохранен в указанной папке с подписью 'ГОТОВО'
------------------------------------------------------
Если необходимо отредактировать сотрудника:
    1. Выбрать сотрудника в таблице программы
    2. Нажать "Редактировать сотрудника"
    3. Внести исправления
    4. Сохранить
    
По вопросам обращаться на почту: ogienko.12003@gmail.com""")

    win_info = tk.Tk()
    win_info.title('Информация')

    win_info.geometry('550x731')
    win_info.maxsize(550, 731)
    x = (win_info.winfo_screenwidth() - win_info.winfo_reqwidth()) / 3
    y = (win_info.winfo_screenheight() - win_info.winfo_reqheight()) / 8
    win_info.wm_geometry("+%d+%d" % (x, y))

    def disable_event():
        win_info.destroy()

    win_info.protocol('WM_DELETE_WINDOW', disable_event)

    info = tk.Text(win_info, font=('courier new', 12), wrap=WORD, bg='lightgrey')
    info.pack(fill='both', expand=True)

    info.insert(1.0, text)

    info.tag_add('title', 1.0, '1.end')
    info.tag_add('contacts', 30.0, '30.end')

    info.tag_config('title', justify='center', font=('bold', 15), foreground='red', underline=True)
    info.tag_config('contacts', justify='right', font=('bold', 8), foreground='darkgreen')

    info.config(state='disabled')

    win_info.update()
