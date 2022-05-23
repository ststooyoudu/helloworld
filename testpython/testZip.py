import os
import shutil
import time
import zipfile
from pathlib import Path
FileList=[]
def scan_file():
    for f in os.listdir():  #由于这里是当前路径，所以需要把这个代码文件和你要处理的文件放到同一个文件夹里
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
#print(scan_file())
print(Path.home())
print(os.path)
print(Path.cwd())
while True:
    if scan_file():
        print('解压正常')
    else:
        print('解压完成！')
        break
zip_filename()
print(FileList)
