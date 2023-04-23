import socket, tqdm, os

# 传输数据分隔符
separator = "<separator>"

# 服务器信息
host = "127.0.0.1"
port = 5002   # 1~1024多数会被系统占用，不建议用

#文件传输的缓冲区（传输不是一个字节一个字节传，而是一整个buffer）
buffer_size = 1024

# 传输文件
filename = r"F:\stable diffusion\novelai-webui-aki-v3\models\Stable-diffusion\yoneyamaMaiStyle_yoneyamaMaiV2Locon.safetensors"
#filename = input('请输入需要上传文件的绝对路径：')
# 文件大小
file_size = os.path.getsize(filename)

# 创建socket连接
s = socket.socket()

# 连接服务器
print(f"服务器连接中{host}:{port}")
s.connect((host, port))
print("与服务器连接成功!")

# 发送文件名字和文件大小，必须进行编码处理encode()
s.send(f"{filename}{separator}{file_size}".encode())

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

# 关闭资源
s.close()
