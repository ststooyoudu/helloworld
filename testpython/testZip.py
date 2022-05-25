import os
import shutil
import time
import zipfile
from pathlib import Path
import openpyxl
from testexcel import TestExcel
from testexcel_newddl import TestExcel_NewDDL
FileList=[]
os.chdir(r'/workspace/helloworld/testpython')
def scan_file():
    for f in os.listdir():  #由于这里是当前路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
        print(f)
        if f.endswith('.zip'):
            unzip_it(f)
            delete(f)
            return f            
def unzip_it(f):
    newZip=zipfile.ZipFile(f)
    newZip.extractall('.')  #解压到当前目录
    newZip.close()
def delete(f):
    os.unlink(f)   #删除压缩包
def zip_filename():
    for f in os.listdir():
        if f.endswith('.sql'):
            FileList.append(Path.cwd()/f)

while True:
    if scan_file():
        print('解压正常')
    else:
        print('解压完成！')
        break
zip_filename()
print(FileList)
for ddl_name in FileList:
    deal_excel=TestExcel('a.xlsx',ddl_name)    #处理所有DDL
    try:
        deal_excel=TestExcel_NewDDL('b.xlsx',ddl_name)    #处理新建表DDL
    except:
        print("这个不是新增表，已忽略！")


