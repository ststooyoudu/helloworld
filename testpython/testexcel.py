import openpyxl
from testReadFile import DDL
wb = openpyxl.load_workbook('a.xlsx')
#sheet = wb.sheetnames[0]
sheet = wb.active
print(sheet)
#sheet1 = wb.create_sheet('myNewSheet')
DDL1=DDL(r'/workspace/helloworld/00473-IM-(IM.OM.IM_RESERVE_BUSI_HIS_EX.REQ_2022_0206060_lwx997552.20220322103836.DDL)-Jiangsu_bes-swx552311.sql'
)
for column in range(sheet.max_column+1):
    if column == 1:
        sheet.cell(row=sheet.max_row+1,column=column).value=DDL1.Author_1
    if column == 2:
        sheet.cell(row=sheet.max_row,column=column).value= DDL1.Author_1
    if column == 3:
        sheet.cell(row=sheet.max_row,column=column).value= DDL1.Remark
    if column == 5:
        sheet.cell(row=sheet.max_row,column=column).value= 'ddl'
    if column == 7:
        sheet.cell(row=sheet.max_row,column=column).value= DDL1.DDLAllContent
    if column == 8:
        sheet.cell(row=sheet.max_row,column=column).value= DDL1.Author_2
    if column == 11:
        sheet.cell(row=sheet.max_row,column=column).value= '江苏bes'
    if column == 14:
        sheet.cell(row=sheet.max_row,column=column).value= '执行一次'    
    if column == 15:
        sheet.cell(row=sheet.max_row,column=column).value= '一般'  
wb.save('a.xlsx')
