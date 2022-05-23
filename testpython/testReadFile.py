import os
from pathlib import Path
os.getcwd()
file=r'/workspace/helloworld/00473-IM-(IM.OM.IM_RESERVE_BUSI_HIS_EX.REQ_2022_0206060_lwx997552.20220322103836.DDL)-Jiangsu_bes-swx552311.sql'
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
        self.Author_1 = '_'.join(((Alist[5].split(':'))[-1]).split('_'))[:-1]   #需求编号
        self.Author_2 = ((Alist[5].split(':'))[-1]).split('_')[-1]     #开发名字
        self.Name = (Alist[6].split(':'))[-1]
        self.Date = (Alist[7].split(':'))[-1]
        self.Remark = (Alist[8].split(':'))[-1]
        self.DDLContent = '\n'.join(Alist[11:])
        self.DDLAllContent = '\n'.join(Alist[:])
        self.userName = ((file.split('\\')[-1]).split('-'))[1]     #数据库名
        self.Alist=Alist
        self.Create = (Alist[11].split(' ')[0].lower()=='create')   #判断文件是否是create
userDict={'OM':'orders','IM':'im','PM':'bespub','SUBSCRIPTION':'subs','BESCHARGE':'bescharge'}
ddl1=DDL(file)
#print(ddl1.DDLContent)
# print(ddl1.Author_1)
# print(ddl1.Author_2)
# print(ddl1.Create)
#print(ddl1.DDLAllContent)
