from socket import *
import threading

'''
1、实例化一个socket,带入http和tcp协议
2、连接ip和port
3、发送信息
'''

IP = '127.0.0.1'
PORT = 11111
BUFLEN = 512

#AF_INET ipv4协议，SOCK_STREAM tcp协议
#实例化一个socket

def recv_info():
    while True:
        data = s.recv(BUFLEN)
        if not data: break
        print(f'received:{data.decode()}')
        # conn.send('服务器收到信息'.encode())

def send_info():
    while True:
        data = input('>>>')
        if not data:
            pass
        else:
            s.send(data.encode())
            rely = s.recv(BUFLEN)
            if not rely:break
            print(f'Receied:{rely.decode()}')

if __name__ == '__main__':
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((IP, PORT))
    print('已成功连接主机！开始通信...')
    print(type(s))

    s_recv = threading.Thread(target=recv_info,daemon=True)
    # s_send = threading.Thread(target=recv_info,daemon=True)
    s_recv.start()
    # s_send.start()

    send_info()





