import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter.messagebox import askyesno, showinfo

import frames
from DataBase import edit_employee


def make_window_edit(name, position, ante, color):
    win_edit = tk.Tk()
    win_edit.title('Редактирование сотрудника')

    win_edit.geometry('300x300')
    x = (win_edit.winfo_screenwidth() - win_edit.winfo_reqwidth()) / 6
    y = (win_edit.winfo_screenheight() - win_edit.winfo_reqheight()) / 3
    win_edit.wm_geometry("+%d+%d" % (x, y))

    win_edit.resizable(False, False)

    def disable_event():
        result = askyesno(title='Подтверждение закрытия', message='Вы действительно хотите закрыть окно?')
        if result:
            win_edit.destroy()
        else:
            pass

    def get_color():
        if new_color_employee_entry.get():
            init_color = '#' + new_color_employee_entry.get()
        else:
            init_color = 'white'
        color1 = colorchooser.askcolor(initialcolor=init_color)
        try:
            button_new_color['bg'] = color1[1]
            sep = '' + str(color1[1])
            result = sep.split(sep='#')[1]
            new_color_employee_entry.delete(0, 'end')
            new_color_employee_entry.insert(0, result)
        except:
            pass

    def update_in_table_person(name, position, ante, color):
        selected_item = frames.employees_table.selection()[0]
        frames.employees_table.set(selected_item, 0, name)
        frames.employees_table.set(selected_item, 1, position)
        frames.employees_table.set(selected_item, 2, ante)
        frames.employees_table.set(selected_item, 3, color)

    def save_edition():
        name = new_name_employee_entry.get()
        position = new_position_employee_entry.get()
        ante = new_ante_employee_entry.get()
        color = new_color_employee_entry.get()
        if not name:
            name = old_name_employee_entry.get()
        if not position:
            position = old_position_employee_entry.get()
        if not ante:
            ante = old_ante_employee_entry.get()
        if not color:
            color = old_color_employee_entry.get()
        result = askyesno(title='Сохранить?', message='Сохранить сотрудника:',
                          detail=f'{name} {position} {ante} {color}')
        if result:
            edit_employee(name, position, ante, color)
            update_in_table_person(name, position, ante, color)
            showinfo(title='Успех', message='Сотрудник сохранен')
            win_edit.destroy()
        else:
            pass

    win_edit.protocol('WM_DELETE_WINDOW', disable_event)

    # Определение контейнера с редактированием сотрудника

    edit_employee_frame = ttk.Frame(win_edit, padding=5)
    # ---------------------- Имя ----------------------------------
    old_name_employee_label = ttk.Label(edit_employee_frame, text='Прежнее имя')
    old_name_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    new_name_employee_label = ttk.Label(edit_employee_frame, text='Новое имя')
    new_name_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    # ---------------------- Должность ----------------------------
    old_position_employee_label = ttk.Label(edit_employee_frame, text='Прежняя должность')
    old_position_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    new_position_employee_label = ttk.Label(edit_employee_frame, text='Новая должность')
    new_position_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    # ---------------------- Ставка -------------------------------
    old_ante_employee_label = ttk.Label(edit_employee_frame, text='Прежняя ставка')
    old_ante_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    new_ante_employee_label = ttk.Label(edit_employee_frame, text='Новая ставка')
    new_ante_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    # ---------------------- Цвет ---------------------------------
    old_color_employee_label = ttk.Label(edit_employee_frame, text='Прежний цвет')
    old_color_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    new_color_employee_label = ttk.Label(edit_employee_frame, text='Новый цвет')
    new_color_employee_entry = ttk.Entry(edit_employee_frame, width=20)
    # ---------------------- Кнопки -------------------------------
    button_new_color = tk.Button(edit_employee_frame, text='Выбрать', command=get_color,
                                 bg='#' + color,
                                 font=('Arial', 10),
                                 fg='black',
                                 width=34)

    buttons_frame = ttk.Frame(win_edit, padding=5)

    button_save = tk.Button(buttons_frame, text='Сохранить', command=save_edition,
                            activebackground='darkgreen',
                            bg='green',
                            font=('Arial', 10),
                            fg='white',
                            width=16)
    button_cancel = tk.Button(buttons_frame, text='Отменить', command=disable_event,
                              activebackground='darkgreen',
                              bg='green',
                              font=('Arial', 10),
                              fg='white',
                              width=15)

    # Распаковка контейнера с редактированием сотрудника

    edit_employee_frame.pack(expand=True, fill='both', padx=2, pady=2)
    # ---------------------- Имя ----------------------------------
    old_name_employee_label.grid(row=0, column=0, sticky='w')
    old_name_employee_entry.grid(row=0, column=1, columnspan=2, pady=2, sticky='we')
    new_name_employee_label.grid(row=1, column=0, sticky='w')
    new_name_employee_entry.grid(row=1, column=1, pady=2, sticky='we')
    # ---------------------- Должность ----------------------------
    old_position_employee_label.grid(row=2, column=0, sticky='w')
    old_position_employee_entry.grid(row=2, column=1, pady=2, sticky='we')
    new_position_employee_label.grid(row=3, column=0, sticky='w')
    new_position_employee_entry.grid(row=3, column=1, pady=2, sticky='we')
    # ---------------------- Ставка -------------------------------
    old_ante_employee_label.grid(row=4, column=0, sticky='w')
    old_ante_employee_entry.grid(row=4, column=1, pady=2, sticky='we')
    new_ante_employee_label.grid(row=5, column=0, sticky='w')
    new_ante_employee_entry.grid(row=5, column=1, pady=2, sticky='we')
    # ---------------------- Цвет ---------------------------------
    old_color_employee_label.grid(row=6, column=0, sticky='w')
    old_color_employee_entry.grid(row=6, column=1, pady=2, sticky='we')
    new_color_employee_label.grid(row=7, column=0, sticky='w')
    new_color_employee_entry.grid(row=7, column=1, pady=2, sticky='we')
    # ---------------------- Кнопки -------------------------------
    button_new_color.grid(row=8, columnspan=2, pady=5)

    buttons_frame.pack(expand=True, fill='x', padx=2, pady=2)
    button_save.grid(row=9, column=0, padx=5, sticky='we')
    button_cancel.grid(row=9, column=1, sticky='we')

    old_name_employee_entry.insert(0, name)
    old_position_employee_entry.insert(0, position)
    old_ante_employee_entry.insert(0, ante)
    old_color_employee_entry.insert(0, color)

    old_name_employee_entry.configure(state='disable')
    old_position_employee_entry.configure(state='disable')
    old_ante_employee_entry.configure(state='disable')
    old_color_employee_entry.configure(state='disable')
