import openpyxl

book = openpyxl.open('data.xlsx', read_only=True)
sheet = book.active

print('\nreading cell:')
print(sheet['B2'].value)  # ячейки
print(sheet[1][2].value)  # индексы
print(sheet[1][0].value)  # rows start from 1, columns start from 0

print('\nrow:')
for row in range(1, sheet.max_row + 1):
    author = sheet[row][0].value
    name = sheet[row][1].value
    year = sheet[row][2].value
    rating = sheet[row][3].value
    print(row, author, name, year, rating)

print('\nrange:')
cells = sheet['B1':'D5']
for name, year, rating in cells:  # выдаст кортеж из двух элементов поскольку диапазон от B до D равент 3.
    print(name.value, year.value, rating.value)

print('\niter_rows():')
for row in sheet.iter_rows(min_row=2, max_row=5, min_col=1, max_col=3):  # for row in sheet.iter_rows() --> выводит все
    for cell in row:
        print(cell.value, end=' ')
    print()

print('\nworksheets[]:')
book_sheets = book.worksheets
print(book_sheets)
sheet2 = book.worksheets[1]
print(sheet2['A2'].value)

print('\nclose():')
book.close()
