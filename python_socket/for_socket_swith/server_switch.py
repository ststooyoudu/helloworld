import socket, os,tqdm
from threading import Thread

# 传输数据分隔符
separator = "<separator>"

# 服务器信息
server_host = "127.0.0.1"
server_port = 5002   # 1~1024多数会被系统占用，不建议用

# 文件传输的缓冲区（传输不是一个字节一个字节传，而是一整个buffer）
buffer_size = 4096

# 创建的Server和client
s = socket.socket()
s.bind((server_host, server_port))  # 服务器绑定端口

# 设置连接监听数
s.listen(5)
print(f"服务器端监听{server_host}:{server_port}")

def run(s):
    # 接受客户端连接
    while True:
        client_socket, address = s.accept()     # 哪一个客户的socket, ip地址
        print(f"客户端{address}连接。")# 打印客户端ip

        #连接服务器
        s_client = socket.socket()
        s_client.connect(('127.0.0.1',9999))
        print(f"服务器{server_host}连接成功。")# 打印服务器ip

        # 接收客户端信息
        received = client_socket.recv(buffer_size).decode()     # 解码
        s_client.sendall(received.encode())

        filename, file_size = received.split(separator)         # 客户端用separator分割的
        filename = os.path.basename(filename)                   # 获取文件的名字，去除路径
        file_size = int(file_size)      # 传输过来的是字符串类型
        th = Thread(target=recv_date,args=(filename,file_size,client_socket,s_client))
        th.start()
        th.join()



def recv_date(filename,file_size,client_socket,s_client):
    # 文件接收处理
#    progress = tqdm.tqdm(range(file_size), f"接收{filename}", unit="B", unit_divisor=1024, unit_scale=True)


#    for _ in progress:
        # 从客户端读取数据
    while True:
        bytes_read = client_socket.recv(buffer_size)
        if not bytes_read:      # 读取结束
            break

        s_client.sendall(bytes_read)
#        progress.update(len(bytes_read))

    # 关闭资源，先关闭客户端，再关闭服务器
    client_socket.close()
#s.close()

run(s)







