import sys
import socket
def build_server():
    #创建 socket对象
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取用户名
    hostname = socket.gethostname()
    port = 9999
    #绑定端口号
    serversocket.bind((hostname, port))
    # 设置最大连接数
    serversocket.listen(5)
    while True :
        clientsocket, addr = serversocket.accept()
        print('监听地址为:%s'%str(addr))
        message = '你好客户端，我是服务端\n'
        clientsocket.send(message.encode('utf-8'))
        clientsocket.close()
if __name__ == '__main__':
    build_server()

