from zarplata_script import identify
from tkinter import filedialog
import tkinter
from config import root


def apply_get():
    global error, success
    path = filedialog.askopenfilename(title='Поиск таблицы')
    file_name1 = path.split(sep='.xlsx')
    file_name1[-1] = '(ГОТОВО)'
    file_name1.append('.xlsx')
    file_name1 = ''.join(file_name1)
    print(file_name1)
    print(path)
    try:
        success.destroy()
        error.destroy()
    except:
        pass
    if path:
        try:
            error.destroy()
            success.destroy()
        except:
            pass
        finally:
            identify(path, file_name1)
            success = tkinter.Label(root, text='Успех!')
            success.pack()
    else:
        try:
            error = tkinter.Label(root, text='Файл не найден')
            error.pack()
            success.destroy()
        except:
            pass
