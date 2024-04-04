import sqlite3


def get_employee():
    connect = sqlite3.connect('Employees.db')
    cursor = connect.cursor()
    cursor.execute("SELECT name, position, ante, color FROM names_antes")
    return cursor


def save_employee_db(name, position, ante, color):
    connect = sqlite3.connect('Employees.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO names_antes (name, position, ante, color) VALUES (?, ?, ?, ?)", (name, position,
                                                                                                 ante, color))
    connect.commit()
    connect.close()


def delete_employee(name):
    connect = sqlite3.connect('Employees.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM names_antes WHERE name = ?', (name,))
    connect.commit()
    connect.close()


def delete_all_employee():
    connect = sqlite3.connect('Employees.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM names_antes WHERE name = name')
    connect.commit()
    connect.close()


def edit_employee(name, position, ante, color):
    connect = sqlite3.connect('Employees.db')
    cursor = connect.cursor()
    cursor.execute('UPDATE names_antes SET name =?, position =?, ante =?, color =? WHERE name =?',
                   (name, position, ante, color, name))
    connect.commit()
    connect.close()


def get_ante():
    connect = sqlite3.connect('Employees.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    row = cursor.execute('SELECT name, ante FROM names_antes').fetchall()
    row_dict = dict(row)
    return row_dict


def get_color():
    connect = sqlite3.connect('Employees.db')
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    row = cursor.execute('SELECT name, color FROM names_antes').fetchall()
    row_dict = dict(row)
    return row_dict
