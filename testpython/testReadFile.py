import os
from pathlib import Path
os.getcwd()
file=r'/workspace/helloworld/testpython/00473-IM-(IM.OM.IM_RESERVE_BUSI_HIS_EX.REQ_2022_0206060_lwx997552.20220322103836.DDL)-Jiangsu_bes-swx552311.sql'
# userName = ((file.split('\\')[-1]).split('-'))[1]  #从文件里提取用户名
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
#        self.Author_1 = '_'.join((((Alist[5].split(':'))[-1]).split('_'))[:-1])   #需求编号
        self.Author_2 = ((Alist[5].split(':'))[-1])    #需求编号
        self.Name = (Alist[6].split(':'))[-1]    #开发名字
        self.Date = (Alist[8].split(':'))[-1]
        self.Remark = (Alist[10].split(':'))[-1]
        self.DDLContent = '\n'.join(Alist[13:])
        self.DDLAllContent = '\n'.join(Alist[:])
        self.userName = ((str(file).split('/')[-1]).split('-'))[1]   
        self.Alist=Alist
        self.Create = (Alist[13].split(' ')[0].lower()=='create')   #判断文件是否是create
        self.isTable = (Alist[13].split(' ')[1].lower()=='table')
        self.userDict = {'OM':['orders','crmdb1-4'],'IM':['im','resdb'],'PM':['prod','pubdb'],'SUBSCRIPTION':['subs','crmdb1-4'],'BESCHARGE':['bescharge','crmdb1-4'],'BESPRO':['bespro','pubdb'],'BESCUST':['cust','pubdb'],'COMMON':['sysmgr','pubdb'],'SM':['sysmgr','pubdb'],'SHOPCART':['shopcart','crmdb1-4'],'BESPAY':['bespay','crmdb1-4'],'BESPUB':['bespub','pubdb'],'BESINVOICE':['besinvoice','crmdb1-4'],'BESSMS':['bessms','crmdb1-4'],'BESGRPCUST':['besgrpcust','crmdb1-4'],'BESAUDIT':['besaudit','crmdb1-4'],'BESOPM':['besopm','crmdb1-4'],'BESRECEIPT':['besreceipt','crmdb1-4'],'BESREPORT':['besreport','crmdb1-4'],'MEMBER':['member','pubdb']}
        for k,v in self.userDict.items():
            if self.userName==k:
                self.db_username=v[0]       #数据库用户名
                self.db_name=v[1]          #数据库名
        if self.Create and self.isTable:  #如果是新增表，记录新增表名
            self.tablename=Alist[13].split(' ')[2]
