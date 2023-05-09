import socket, tqdm, os,time
from tkinter import *
from tkinter import filedialog
from threading import Thread

filelist = []

# 传输数据分隔符
separator = "<separator>"
# 文件传输的缓冲区（传输不是一个字节一个字节传，而是一整个buffer）
buffer_size = 1024

def socket_init():
    # 服务器信息
    host = "xxx.xxx.xxx.xxx"
    port = 8080  # 1~1024多数会被系统占用，不建议用

    # 创建socket连接
    s = socket.socket()
    # 连接服务器
    print(f"服务器连接中{host}:{port}\n")
    s.connect((host, port))
    log_text.insert(END, '与服务器连接成功!\n')
    print("与服务器连接成功!\n")
    return s

def run(s,filename,file_size):
    try:
        # 发送文件名字和文件大小，必须进行编码处理encode()
        filename_temp = filename.split('/')[-1]
        s.send(f"{filename_temp}{separator}{file_size}".encode())

        # 文件传输，用tqdm提示发送进度，传输单位Byte（1024表示1Byte=1024bit）
        progress = tqdm.tqdm(range(file_size), f"发送{filename}", unit="B", unit_divisor=1024)

        with open(filename, "rb") as f:
            for _ in progress:
                # 读取文件
                bytes_read = f.read(buffer_size)    # 一次读取buffer_size大小的
                if not bytes_read:      # 读取不到就退出
                    break
                # sendall()可以确保即使网络拥堵，数据仍然可以传输
                s.sendall(bytes_read)
                progress.update(len(bytes_read))    # 按照读的大小 更新进度条
            result_text.insert(1.0, filename + ' 已上传\n')

        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        log_text.insert(END, current_time + ' 文件已上传至10.33.251.116:\\uploadFile\\temp目录下\n')
        print('传输完成！\n')
    except:
        time.sleep(5)
        run(s,filename,file_size)
    # 关闭资源
    s.close()
    time.sleep(5)

def upload():
    filelist = text.get(1.0, END)
    filelist = filelist.split('\n')
    print(filelist)

    for filename in filelist:
        try:
            file_size = os.path.getsize(filename)
            s = socket_init()
            run(s,filename,file_size)
        except:
            pass


    # print('所有文件已上传')

def select_files():
    # 多个文件选择
    selected_files_path = filedialog.askopenfilenames()  # askopenfilenames函数选择多个文件
    info = '\n'.join(selected_files_path)
    text.insert(END,info)  # 多个文件的路径用换行符隔开


root = Tk()
root.title("文件上传工具_v1.0")           #窗口名
root.geometry('1068x500+10+10')
#标签
lb = Label(root, text="待上传文件")
lb.grid(row=0, column=0)
lb2 = Label(root, text="输出结果")
lb2.grid(row=0, column=12)
#信息框
# text = StringVar()
# message = Message(root,text="123")
# message.grid(row=1, column=0, rowspan=10, columnspan=10)
#文本框
text = Text(root, width=67, height=20)  #原始数据录入框
text.grid(row=1, column=0, rowspan=10, columnspan=10)

result_text = Text(root, width=70, height=35)  #处理结果展示
result_text.grid(row=1, column=12, rowspan=15, columnspan=10)
log_text = Text(root, width=66, height=9)  # 日志框
log_text.grid(row=13, column=0, columnspan=10)
#按钮
select_button = Button(root, text="选择文件", bg="lightblue", width=10,command=select_files)  # 调用内部方法  加()为直接调用
select_button.grid(row=1, column=11)
upload_button = Button(root, text="上传", bg="lightblue", width=10,command=upload)  # 调用内部方法  加()为直接调用
upload_button.grid(row=3, column=11)

root.mainloop()
