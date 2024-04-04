from tkinter import ttk, Button

from config import root
from handlers import btn_path_clicked, btn_path_itog_clicked, sort, delete_person_table, edit_person_table, apply

# Определение контейнера для поиска исполняемого файла

path_frame = ttk.Frame(root, width=400, height=50)
path_frame_label = ttk.Label(path_frame, text='Укажите путь до файла')
path_frame_entry = ttk.Entry(path_frame, width=52)
path_frame_button = Button(path_frame, text='Путь',
                           activebackground='darkgreen', command=btn_path_clicked,
                           bg='green',
                           font=('Arial', 10),
                           fg='white',
                           width=5,
                           )

# Определение контейнера для поиска папки сохранения итогового файла

path_itog_frame = ttk.Frame(root, width=400, height=50)
path_itog_frame_label = ttk.Label(path_itog_frame, text='Укажите папку сохранения')
path_itog_frame_entry = ttk.Entry(path_itog_frame, width=52)
path_itog_frame_button = Button(path_itog_frame, text='Путь', command=btn_path_itog_clicked,
                                activebackground='darkgreen',
                                bg='green',
                                font=('Arial', 10),
                                fg='white',
                                width=5,
                                )

# Определение контейнера с таблицей

employees_table_frame = ttk.Frame(root, padding=5)
employees_table_columns_frame = ("name", "position", "ante", "color")
employees_table = ttk.Treeview(employees_table_frame, columns=employees_table_columns_frame, show='headings')
employees_table.heading('name', text='Имя', anchor='w', command=lambda: sort(0, False))
employees_table.heading('position', text='Должность', anchor='w', command=lambda: sort(1, False))
employees_table.heading('ante', text='Ставка', anchor='w', command=lambda: sort(2, False))
employees_table.heading('color', text='Цвет', anchor='w', command=lambda: sort(3, False))
employees_table.column("#1", stretch=False, width=162, minwidth=142)
employees_table.column("#2", stretch=False, width=95, minwidth=95)
employees_table.column("#3", stretch=False, width=50, minwidth=30)
employees_table.column("#4", stretch=False, width=50, minwidth=30)
scrollbar = ttk.Scrollbar(employees_table_frame, orient='vertical', command=employees_table.yview)
employees_table.configure(yscroll=scrollbar.set)

# Определение контейнера с кнопками удаления и изменения сотрудников

employees_button_frame = ttk.Frame(root, padding=5)
employees_table_button_delete = Button(employees_button_frame, text='Удалить сотрудника', command=delete_person_table,
                                       activebackground='darkgreen',
                                       bg='green',
                                       font=('Arial', 10),
                                       fg='white',
                                       width=20,
                                       )
employees_table_button_edit = Button(employees_button_frame, text='Редактировать сотрудника', command=edit_person_table,
                                     activebackground='darkgreen',
                                     bg='green',
                                     font=('Arial', 10),
                                     fg='white',
                                     width=20,
                                     )
accept_button = Button(employees_button_frame, text='Готово', command=apply,
                       activebackground='darkgreen',
                       bg='green',
                       font=('Arial', 15),
                       fg='white',
                       width=20,
                       )
