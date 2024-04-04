from tkinter import Menu

from frames import *
from handlers import insert_in_table, btn_path_clicked, btn_path_itog_clicked, delete_all_table, disable_event
from window_add import make_window_add
from window_info import make_window_info

# Распаковка контейнера с функцией поиска исполняемого файла

path_frame.pack(anchor='nw', padx=5, pady=5)
path_frame_label.grid(padx=5, row=0, columnspan=1)
path_frame_entry.grid(row=1, column=0, padx=5, pady=5)
path_frame_button.grid(row=1, column=1, padx=5, pady=5)

# Распаковка контейнера с функцией указывания папки итогового файла

path_itog_frame.pack(anchor='nw', padx=5, pady=5)
path_itog_frame_label.grid(padx=5, row=0, columnspan=1)
path_itog_frame_entry.grid(row=1, column=0, padx=5, pady=5)
path_itog_frame_button.grid(row=1, column=1, padx=5, pady=5)

# Распаковка контейнера с таблицей

employees_table_frame.pack(anchor='nw', padx=5)
employees_table.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

# Распаковка контейнера с кнопками

employees_button_frame.pack(padx=5)
employees_table_button_delete.grid(row=0, column=0, sticky='ew', padx=5)
employees_table_button_edit.grid(row=0, column=1, sticky='ew', padx=5)
accept_button.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=10)
#
# # Бинд кнопок
#
# path_frame_button.bind("<Control-Button-1>", btn_path_clicked_clear)
# path_frame_button.bind("<Control-Button-1>", btn_path_itog_clicked_clear)

# Распаковка меню

root.option_add("*tearOff", False)

main_menu = Menu()
file_menu = Menu()
table_menu = Menu()

main_menu.add_cascade(label="Файл", menu=file_menu)
main_menu.add_cascade(label="Таблица", menu=table_menu)

file_menu.add_command(label="Открыть", command=btn_path_clicked)
file_menu.add_command(label="Сохранить", command=btn_path_itog_clicked)
file_menu.add_separator()
file_menu.add_command(label="Выйти", command=disable_event)

table_menu.add_command(label="Добавить сотрудника", command=make_window_add)
table_menu.add_command(label="Удалить всех сотрудников", command=delete_all_table)

main_menu.add_command(label='Инфо', command=make_window_info)

root.config(menu=main_menu)

root.protocol('WM_DELETE_WINDOW', disable_event)

# Инициализация приложения

if __name__ == '__main__':
    insert_in_table()
    root.mainloop()
