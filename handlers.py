from tkinter import filedialog
from tkinter.messagebox import showwarning, askyesno, showinfo

import frames
from DataBase import get_employee, delete_employee, delete_all_employee
from config import root
from window_edit import make_window_edit
from zarplata_script import identify


def apply():
    path = frames.path_frame_entry.get()
    path_success = frames.path_itog_frame_entry.get()
    if path_success:
        file_name = path.split(sep='.xlsx')
        file_name = ''.join(file_name)
        file_name = file_name.split(sep='/')
        file_name = file_name[-1]
        file_name += '(ГОТОВО).xlsx'
        path_success1 = path_success + '/' + file_name
    else:
        path_success1 = path.replace('.xlsx', '(ГОТОВО).xlsx')
        path_success = path.split('/')
        path_success.remove(path_success[-1])
        path_success = '/'.join(path_success)
    if path:
        try:
            identify(path, path_success1)
            showinfo(title='Успех', message='Готовый файл находится в папке:', detail=path_success)
        except:
            showwarning(title='Ошибка', message='Файл не найден или что-то пошло не так.',
                        detail='Попробуй использовать другой файл.')
    else:
        showwarning(title='Ошибка', message='Файл не найден или что-то пошло не так.',
                    detail='Попробуй использовать другой файл.')


def get_path():  # Функция получения пути исполняемого файла
    path = filedialog.askopenfilename(defaultextension='*.xlsx')
    return path


def get_path_itog():  # Функция получения пути папки сохранения итогового файла
    path = filedialog.askdirectory()
    return path


def btn_path_clicked():  # Функция обработки события нажатия кнопки поиска исполняемого файла
    frames.path_frame_entry.delete(0, 'end')  # Очистка поля
    frames.path_frame_entry.insert(0, get_path())  # Запись полученного пути


def btn_path_itog_clicked():  # Функция обработки события нажатия кнопки поиска папки сохранения итогового файла
    frames.path_itog_frame_entry.delete(0, 'end')  # Очистка поля
    frames.path_itog_frame_entry.insert(0, get_path_itog())  # Запись полученного пути


def btn_path_clicked_clear(event):  # Функция обработки события нажатия кнопки
    frames.path_frame_entry.delete(0, 'end')  # Очистка поля


def btn_path_itog_clicked_clear(event):  # Функция обработки события нажатия кнопки поиска исполняемого файла
    frames.path_itog_frame_entry.delete(0, 'end')  # Очистка поля


def sort(col, reverse):  # Сортировка таблицы по нажатию
    l = [(frames.employees_table.set(k, col), k) for k in frames.employees_table.get_children("")]
    l.sort(reverse=reverse)
    for index, (_, k) in enumerate(l):
        frames.employees_table.move(k, "", index)
    frames.employees_table.heading(col, command=lambda: sort(col, not reverse))


def insert_in_table():  # Добавление всех сотрудников в таблицу
    for person in get_employee():
        frames.employees_table.insert("", 'end', values=person)


def insert_in_table_person(name, position, ante, color):  # Добавление одного сотрудника в таблицу
    person = name, position, ante, color
    frames.employees_table.insert("", 'end', values=person)


def edit_person_table():
    try:
        selected_item = frames.employees_table.selection()[0]
        name = frames.employees_table.set(selected_item, '#1')
        position = frames.employees_table.set(selected_item, '#2')
        ante = frames.employees_table.set(selected_item, '#3')
        color = frames.employees_table.set(selected_item, '#4')
        make_window_edit(name, position, ante, color)
    except IndexError:
        showwarning(title='Ошибка', message='Вы не выбрали сотрудника', detail='Нажмите на сотрудника в таблице')


def delete_person_table():
    try:
        selected_item = frames.employees_table.selection()[0]
        name = frames.employees_table.set(selected_item, '#1')
        result = askyesno(title='Удаление', message='Подтвердите удаление', detail=f'Сотрудник: {name}')
        if result:
            showinfo(title='Успех', message=f'Сотрудник {name} удален')
            delete_employee(name)
            frames.employees_table.delete(selected_item)
        else:
            pass
    except IndexError:
        showwarning(title='Ошибка', message='Удаление невозможно', detail='Нажмите на сотрудника в таблице')


def delete_all_table():
    try:
        result = askyesno(title='Удаление', message='Подтвердите удаление всей таблицы')
        if result:
            showinfo(title='Успех', message=f'Все сотрудники удалены')
            for i in frames.employees_table.get_children(''):
                frames.employees_table.delete(i)
            delete_all_employee()
        else:
            pass
    except IndexError:
        showwarning(title='Ошибка', message='Удаление невозможно', detail='В таблице ничего нет')


def disable_event():
    result = askyesno(title='Подтверждение закрытия', message='Вы действительно хотите закрыть окно?')
    if result:
        root.destroy()
    else:
        pass
