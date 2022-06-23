import os
import zipfile
import shutil
import time
from pathlib import Path
dict={'interface':'202206232100.0.1','bes':'202206232100.0.1','app':'202206232100.0.1','web':'202206232100.0.1'}

defaultPath=os.getcwd()
def scan_file():   #查询当前目录下所有zip包
    for f in os.listdir():  #由于这里是当前路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
        print(f)
        if f.endswith('.zip'):
            unzip_it(f)
            return f

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
    filename=os.path.join(os.getcwd(),f,f,'env\crm')
    print(filename)
    file=open(filename)
    for lines in file:
        if '/' in lines:
            print(lines,end='')
            line=lines.strip('/')[-1]
            print(line)
            name=line.strip(':')[0]
            value = line.strip(':')[0]
            if name in dict:
                value=value.replace(value,dict[name])
                print(value)

def zip_it(f):   #压缩回文件，先删除原有zip，再重新压缩回去
    f = (f.split('.'))[0]
    shutil.make_archive(f,'zip',f)
    print('a')

scan_file()
