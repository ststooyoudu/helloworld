import openpyxl
wb = openpyxl.load_workbook('a.xlsx')
#sheet = wb.sheetnames[0]
sheet = wb.active
print(sheet)
sheet1 = wb.create_sheet('myNewSheet')

for row in range(2,sheet.max_row+1):
    for column in range(2,sheet.max_column):
        print((sheet.cell(row=row,column=column)).value)
        (sheet1.cell(row=row,column=column)).value=(sheet.cell(row=row,column=column)).value


wb.save('a.xlsx')
print(sheet1.columns)
