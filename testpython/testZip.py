import os
import shutil
import time
import zipfile

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

print(scan_file())

while True:
    if scan_file():
        print('解压正常')
    else:
        print('解压完成！')
        break
