import socket
import threading
import queue

IP = '127.0.0.1'
PORT = 11111
BUFLEN = 512

serviceSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serviceSocket.bind((IP,PORT))
serviceSocket.listen(5)

clientlist = []  #存放socket实例
public_message = {}   #存放公共信息
def init():
    while True:
        try:
            client,addr = serviceSocket.accept()
            if client in clientlist:
                print('您是老用户！')
            else:
                clientlist.append(client)
                r = threading.Thread(target=recv_info,args=(client,))
                r.start()
        except Exception as e:
            print(f'{addr}中断了连接',e)

def recv_info(client):
    while True:
        try:
            if client in clientlist:
                data = client.recv(BUFLEN).decode()
                if data !='':
                    print(data)
                    public_message[client] = queue.Queue()
                    public_message[client].put(data)
                    # boardcast(client)
                else:
                    print('有用户退出')
                    clientlist.remove(client)
        except Exception as e:
            print('有用户中断了连接', e)
            clientlist.remove(client)

def boardcast():
    while True:
        if len(clientlist) > 1:
            public_message_clone = [i for i in public_message]
            for client in clientlist:
                for i in public_message:
                    if i!=client and public_message[i].empty() ==False:
                        data = public_message[i].get_nowait()
                        if data !='':
                            client.send(data.encode())
                            print('服务器转发了信息')

t1 = threading.Thread(target=init)
t2 = threading.Thread(target=boardcast)

t1.start()
t2.start()





