import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter.messagebox import askyesno, showinfo, showerror

from DataBase import save_employee_db
from handlers import insert_in_table_person


def make_window_add():
    win_add = tk.Tk()
    win_add.title('Добавить сотрудника')

    win_add.geometry('300x300')
    x = (win_add.winfo_screenwidth() - win_add.winfo_reqwidth()) / 6
    y = (win_add.winfo_screenheight() - win_add.winfo_reqheight()) / 3
    win_add.wm_geometry("+%d+%d" % (x, y))

    win_add.resizable(False, False)

    def disable_event():
        result = askyesno(title='Подтверждение закрытия', message='Вы действительно хотите закрыть окно?')
        if result:
            win_add.destroy()
        else:
            pass

    def save_employee():
        name = add_employee_entry_name.get()
        position = add_employee_entry_position.get()
        ante = add_employee_entry_ante.get()
        color = add_employee_entry_color.get()
        if name and position and ante and color:
            result = askyesno(title='Добавление', message=f'Вы действительно хотите добавить сотрудника:',
                              detail=f'{name} {position} {ante} {color}')
            if result:
                save_employee_db(name, position, ante, color)
                insert_in_table_person(name, position, ante, color)
                showinfo(title='Успех!', message='Сотрудник успешно добавлен!',
                         detail=f'{name} {position} {ante} {color}')
                win_add.destroy()
            else:
                pass
        else:
            showerror(title='Ошибка!', message='Сохранение невозможно', detail='Заполнены не все поля')

    def get_color():
        if add_employee_entry_color.get():
            init_color = '#' + add_employee_entry_color.get()
        else:
            init_color = 'white'
        color = colorchooser.askcolor(initialcolor=init_color)
        try:
            add_employee_button_color['bg'] = color[1]
            sep = '' + str(color[1])
            result = sep.split(sep='#')[1]
            add_employee_entry_color.delete(0, 'end')
            add_employee_entry_color.insert(0, result)
        except:
            pass

    win_add.protocol('WM_DELETE_WINDOW', disable_event)

    # Определение контейнера с добавлением сотрудника

    add_employee_frame = ttk.Frame(win_add, padding=5)
    add_employee_lable_name = ttk.Label(add_employee_frame, text='Имя сотрудника', justify='center')
    add_employee_entry_name = ttk.Entry(add_employee_frame)
    # -----------------------------Поле Имя----------------------------------
    add_employee_lable_position = ttk.Label(add_employee_frame, text='Должность сотрудника', justify='center')
    add_employee_entry_position = ttk.Entry(add_employee_frame)
    # -----------------------------Поле Должность----------------------------
    add_employee_lable_ante = ttk.Label(add_employee_frame, text='Ставка сотрудника в час', justify='center')
    add_employee_entry_ante = ttk.Entry(add_employee_frame)
    # -----------------------------Поле Ставка-------------------------------
    add_employee_lable_color = ttk.Label(add_employee_frame, text='Цвет', justify='center')
    add_employee_entry_color = ttk.Entry(add_employee_frame)
    add_employee_button_color = tk.Button(add_employee_frame, text='Выбрать', command=get_color,
                                          bg='green',
                                          font=('Arial', 10),
                                          fg='white',
                                          width=10)
    # -----------------------------Поле Цвет---------------------------------
    add_employee_buttons = ttk.Frame(win_add, width=400, height=50)
    add_employee_button_accept = tk.Button(add_employee_buttons, text='Сохранить',
                                           command=save_employee,
                                           activebackground='darkgreen',
                                           bg='green',
                                           font=('Arial', 10),
                                           fg='white',
                                           width=17)
    add_employee_button_cancel = tk.Button(add_employee_buttons, text='Отменить', command=disable_event,
                                           activebackground='darkgreen',
                                           bg='green',
                                           font=('Arial', 10),
                                           fg='white',
                                           width=17)
    # -----------------------------Кнопки-------------------------------------

    # Распаковка контейнера с добавлением сотрудника

    add_employee_frame.pack(expand=True, fill='x', padx=2, pady=2)
    add_employee_lable_name.pack(expand=True, pady=2, padx=2, anchor='center')
    add_employee_entry_name.pack(pady=2, padx=2, expand=True, fill='x')
    # -----------------------------Поле Имя----------------------------------
    add_employee_lable_position.pack(expand=True, anchor='center', pady=2, padx=2)
    add_employee_entry_position.pack(pady=2, padx=2, expand=True, fill='x')
    # -----------------------------Поле Должность----------------------------
    add_employee_lable_ante.pack(expand=True, anchor='center', pady=2, padx=2)
    add_employee_entry_ante.pack(pady=2, padx=2, expand=True, fill='x')
    # -----------------------------Поле Ставка-------------------------------
    add_employee_lable_color.pack(expand=True, anchor='center', pady=2, padx=2)
    add_employee_entry_color.pack(pady=2, padx=2, expand=True, fill='x')
    add_employee_button_color.pack(pady=2, padx=2, expand=True, fill='x')
    # -----------------------------Поле Цвет---------------------------------
    add_employee_buttons.pack(expand=True, fill='x', padx=2, pady=2)
    add_employee_button_accept.grid(pady=2, padx=(0, 2), row=0, column=0, sticky='ew')
    add_employee_button_cancel.grid(pady=2, padx=(2, 0), row=0, column=1, sticky='ew')

    # -----------------------------Кнопки------------------------------------
