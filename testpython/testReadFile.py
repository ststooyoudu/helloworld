import os
from pathlib import Path
os.getcwd()
file=r'D:\下载\CUST\00422-OM-(OM.OM.OM_GRP_IMS_NUM_PICK_HIS_EX.REQ_2022_03144517_mwx584905.20220421201145.DDL)-Jiangsu_bes-l00293600.sql'
userName = ((file.split('\\')[-1]).split('-'))[1]  #从文件里提取用户名
class DDL:
    def __init__(self,file):
        Alist = []
        with open(file, encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                lineTemp = line.strip('\n')
                Alist.append(lineTemp)
        self.Story = (Alist[3].split(':'))[-1]
        self.DTS = (Alist[4].split(':'))[-1]
        self.Author_1 = '_'.join(((Alist[5].split(':'))[-1]).splist('_'))[:-1]   #需求编号
        self.Author_2 = ((Alist[5].split(':'))[-1]).splist('_')[-1]     #开发名字
        self.Name = (Alist[6].split(':'))[-1]
        self.Date = (Alist[7].split(':'))[-1]
        self.Remark = (Alist[8].split(':'))[-1]
        self.DDLContent = '\n'.join(Alist[11:])
        self.userName = ((file.split('\\')[-1]).split('-'))[1]
        self.Create = (Alist.split(' ')[0].lower()=='create')   #判断文件是否是create
userDict={'OM':'orders','IM':'im','PM':'bespub','SUBSCRIPTION':'subs','BESCHARGE':'bescharge'}
ddl1=DDL(file)
print(ddl1.DDLContent)
