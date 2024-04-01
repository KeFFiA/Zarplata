import openpyxl as ox
import re
from openpyxl.styles import Font, Border, Side, NamedStyle, PatternFill


def identify(path, file_name1):
    book = ox.load_workbook(f"{path}")
    sheet = book.active
    file_name = file_name1
    znach(sheet, book, file_name)


def znach(sheet, book, file_name):
    stavka = {
        'Огиенко Александр': 200,
        'Тишков Артем': 250,
        'Бехруз Рахматуллаев': 250,
        'Рахматуллаев Бехруз': 80,
        'Андреев Николай': 250,
        'Филинева Анастасия': 170,
        'Земскова Татьяна': 130,
        'Ивантеева Ангелина': 170,
        'Мамадиева Ангелина': 250,
        'Фомин Никита': 250,
        'Щерчкова Дарья': 170,
        'Ефремова Татьяна': 250,
        'Еремин Дмитрий': 250,
        'Ликучев Данила': 250,
        'Скворцов Данила': 250,
        'Данилов Андрей': 250
    }

    col = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    time = []
    time11 = []
    e = ''
    r = ''

    for row in range(2, sheet.max_row + 1):
        name = sheet[row][0].value
        # company = sheet[row][1].value
        # title = sheet[row][2].value
        if name in stavka:
            sheet[f"W{row}"] = stavka[name]
        for column in col:
            q = sheet[f"{column}{row}"].value
            time.append(q)
        for i in time:
            try:
                e += i
                for i1 in e:
                    if i1 == ':':
                        i1 = '+'
                        r += i1
                    else:
                        r += i1
                r = re.sub(pattern=r'[+][0]', repl=r"+0o", string=r)
                r = re.sub(pattern=r'[+](0o9)|[+](0o8)', repl=r"+0o7", string=str(r))
                time11.append(r)
                r = ''
                e = ''
            except:
                pass
        t = list(map(lambda x: x + '/60', time11))
        time.clear()
        time11.clear()
        time_itog = []
        j = 0.0
        for i in range(len(t)):
            time_itog.append(round(eval(t[i]), 2))
            j += round(eval(t[i]), 2)
        sheet[f"U{row}"] = j
        # print(name, company, time_itog, j)
    cells_names(sheet, book, file_name)


def cells_names(sheet, book, file_name):
    name_4_cells = {
        "U": "Часы",
        "V": "Общие часы",
        "W": "Ставка",
        "X": "Итого наличка",
        "Y": "На карту",
        "Z": "Остаток",
        "AA": "Оплачено"
    }
    for column in name_4_cells:
        sheet[f"{column}{1}"] = name_4_cells[column]
    formulas(sheet, book, file_name)


def formulas(sheet, book, file_name):
    for row in range(2, sheet.max_row + 1):
        try:
            sheet[f"V{row}"] = f"=U{row}"
            sheet[f"X{row}"] = f"=V{row}*W{row}"
            sheet[f"Z{row}"] = f"=X{row}-Y{row}"
        except AttributeError:
            pass
    styles(sheet, book, file_name)


def styles(sheet, book, file_name):
    colors = {
        'Огиенко Александр': 'de9495',
        'Тишков Артем': '7f7ac0',
        'Бехруз Рахматуллаев': 'bc5e34',
        'Рахматуллаев Бехруз': 'bc5e34',
        'Андреев Николай': 'e45f5d',
        'Филинева Анастасия': '65f0ff',
        'Земскова Татьяна': 'b3a94e',
        'Ивантеева Ангелина': '49d58a',
        'Мамадиева Ангелина': '979797',
        'Фомин Никита': 'ffffff',
        'Щерчкова Дарья': 'aeff7c',
        'Ефремова Татьяна': 'a898cf',
        'Еремин Дмитрий': 'a3ff8b',
        'Ликучев Данила': '9eb53c',
        'Скворцов Данила': 'fff26a',
        'Данилов Андрей': 'ff8eb0',
        'Богатов Артем': '00ff8d'
    }

    colums = ['V', 'W', 'X', 'Y', 'Z', 'AA']
    borders_sheet = NamedStyle(name='border')
    borders_sheet.border = Border(left=Side(border_style='thin'),
                                  top=Side(border_style='thin'),
                                  bottom=Side(border_style='thin'),
                                  right=Side(border_style='thin'))

    for column in range(20, 26):
        sheet[1][column].font = Font(bold=True)

    for row in range(1, sheet.max_row + 1):
        name = sheet[row][0].value
        stroka = name
        # print(stroka)
        for column in range(20, 27):
            sheet[row][column].style = borders_sheet

    a = 0
    b = 0
    for row in range(1, sheet.max_row + 1):
        name = sheet[row + a][0].value
        stroka1 = sheet[row + 1 + a][0].value
        stroka2 = sheet[row + 2 + a][0].value
        if stroka1 == name and stroka2 == name:
            a += 1
            if name is not None:
                for i in colums:
                    sheet.merge_cells(f'{i}{row + a - 1}:{i}{row + 2 + a - 1}')
                    sheet[f"V{row + a - 1}"] = f"=U{row + b}+U{row + a}+U{row + 2 + a - 1}"
                b += 1
        elif stroka1 == name or stroka2 == name:
            a += 1
            if name is not None:
                for i in colums:
                    sheet.merge_cells(f'{i}{row + a - 1}:{i}{row + 1 + a - 1}')
                    sheet[f"V{row + a - 1}"] = f"=U{row + b}+U{row + 1 + a - 1}"
                b += 1

    for row in range(2, sheet.max_row + 1):
        name = sheet[row][0].value
        for column in range(0, 27):
            if name in colors:
                sheet[row][column].fill = PatternFill(patternType='solid', start_color=f'{colors[name]}')

    sheet.freeze_panes = "B2"

    book.save(filename=file_name)
