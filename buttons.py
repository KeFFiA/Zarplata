from config import root
from tkinter import Button, ttk
from handlers import apply_get

# apply = Button(root, text='apply', command=apply_get, activebackground='gray')

browse = Button(root, text='Путь', command=apply_get,
                activebackground='darkgreen',
                bg='green',
                # padx=80,
                # pady=25,
                font=('Arial', 20),
                fg='white',
                width=16,
                )
