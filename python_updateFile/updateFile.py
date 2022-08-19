import os
import zipfile
import shutil
import time
from pathlib import Path

file = open('a.txt')
dict={}
errer={}
for lines in file:
#    print(lines,end='')
    line=(lines.split(' '))#切割空格
    name1=line[0].strip() #切割\n
    name=line[0].split('\t') #切割\t
    dictname=name[0]
    dictvalue=name[1].strip('\n')
    dict.setdefault(dictname,dictvalue)


defaultPath=os.getcwd()
def scan_file():   #查询当前目录下所有zip包
    for f in os.listdir():  #由于这里是当前路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
        print(f)
        if f.endswith('.zip'):
            unzip_it(f)
#            return f

def unzip_it(f):   #解压zip包
    newZip=zipfile.ZipFile(f)
    f=(f.split('.'))[0]
    if not os.path.exists(f):
        os.makedirs(f)
    newZip.extractall(f)  #解压到当前目录
    newZip.close()
    delete(f+'.zip')   #删除压缩包
    deal_it(f,dict)    #处理文件
    zip_it(f)   #压缩原包

def delete(f):
    os.unlink(f)  # 删除压缩包

def deal_it(f,dict):   #处理文件,根据传过来的路径名，拼接文件路径
    filename=os.path.join(os.getcwd(),f,'env\crm.env')
    print(filename)
    file=open(filename)
    fileW = open(filename+'_temp','a')
    for lines in file:
        if '/' not in lines:
            fileW.writelines(lines)
        if '/' in lines:
            tempvalube =lines
            tempvalube_pre=tempvalube.rsplit(':',1)  #切割原始行一直到‘:’
            line=(lines.strip()).split('/')[-1]
            print(line,end='')
            name=line.split(':')[0]    #镜像名
            value = line.split(':')[1]  #镜像号
            if name in dict:
                value=value.replace(value,dict[name])
                tempvalube_pre=str(tempvalube_pre[0])+':'+dict[name] #拼接整行
                print('\t'+value)
            else:
                print('\n请检查镜像名'+name+'在a.txt中是否存在!')
                errer.setdefault(f,name)  #报错的文件和镜像名
                break
            fileW.writelines(tempvalube_pre+'\n')
#            fileW.writelines('\n')
    file.close()
    fileW.close()
    delete(filename)  #删除原始文件
    rename(filename)  # 将temp文件重命名为原文件名

def rename(f):
    try:
        os.rename(f+'_temp',f)
        print("重命名完毕")
    except(FileNotFoundError):
        print("temp文件不存在")

def zip_it(f):   #压缩回文件，先删除原有zip，再重新压缩回去
    f = (f.split('.'))[0]
    shutil.make_archive(f,'zip',f)


scan_file()
print('\n进程结束！')
print('报错文件:',end='')
print(errer.items())
time.sleep(30)
