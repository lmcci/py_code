# udp 每个数据包都有地址端口 不安全 数据可能丢失
# tcp 面向链接 先建立链接 安全   发送应答机制 接收方告诉发送方收到的响应

import socket


def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_client.connect(('192.168.1.100', 8888))

    tcp_client.send('hello'.encode('gbk'))

    

    tcp_client.close()


if __name__ == '__main__':
    main()

