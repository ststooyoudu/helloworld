import openpyxl
from testReadFile import DDL

class TestExcel:
    def __init__(self,xls_name,ddl_name):
        self.wb = openpyxl.load_workbook(xls_name)
        #sheet = wb.sheetnames[0]
        self.sheet = self.wb.active
        self.DDL1=DDL(ddl_name)
        for column in range(self.sheet.max_column+1):
            if column == 1:
                self.sheet.cell(row=self.sheet.max_row+1,column=column).value=self.DDL1.Author_1
            if column == 2:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= self.DDL1.Author_1
            if column == 3:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= self.DDL1.Remark
            if column == 5:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= 'ddl'
            if column == 7:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= self.DDL1.DDLAllContent
            if column == 8:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= self.DDL1.Author_2
            if column == 11:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= '江苏bes'
            if column == 13:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= self.DDL1.userName
            if column == 14:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= '执行一次' 
            if column == 15:
                self.sheet.cell(row=self.sheet.max_row,column=column).value= '一般'  
        self.wb.save('a.xlsx')

# print(DDL1.DDLContent)
#print(DDL1.Author_1)
# print(DDL1.Author_2)
# print(DDL1.Create)
# print(DDL1.DDLAllContent)
# print(DDL1.userName)

#wb.save('a.xlsx')

#test1=TestExcel('a.xlsx','/workspace/helloworld/testpython/00475-PM-(PM.PM.PM_TERMINAL_PRICE_EX.REQ_2022_0304100_y30020255.20220330164306.DDL)-Jiangsu_bes-zwx555221.sql')
