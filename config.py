import tkinter as tk

root = tk.Tk()

root.title('ЗП конвертер')

root.iconbitmap(default='Resources/exel-icon.ico')

root.geometry('400x460')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2.5
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 3
root.wm_geometry("+%d+%d" % (x, y))

root.resizable(False, False)
