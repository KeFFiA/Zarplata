from tkinter.messagebox import showinfo, showerror

from zarplata_script import identify
from tkinter import filedialog


def apply_get():
    path = filedialog.askopenfilename()
    file_name1 = path.split(sep='.xlsx')
    file_name1[-1] = '(ГОТОВО)'
    file_name1.append('.xlsx')
    file_name1 = ''.join(file_name1)
    file_name_success = path.split(sep='/')
    file_name_success[-1] = ''
    file_name_success = '/'.join(file_name_success)
    if path:
        try:
            identify(path, file_name1)
            message = f"Готовый файл находится в папке:\n{file_name_success}"
            showinfo(title='Успех', message=message)
        except:
            message = f"Файл не найден или что-то пошло не так.\nПопробуй использовать другой файл."
            showerror(title='Ошибка', message=message)
    else:
        message = f"Файл не найден или что-то пошло не так.\nПопробуй использовать другой файл."
        showerror(title='Ошибка', message=message)
