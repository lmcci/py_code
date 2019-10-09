import socket


def main():

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.bind(('', 8889))

    # 同一时刻可有128个链接同时建立
    tcp_server.listen(128)

    # 阻塞等待客户端链接
    client_socket, client_info = tcp_server.accept()

    print(client_info)

    # 阻塞等待客户端发送消息       recv只有发送的消息  udp的recvfrom既有发送的消息也有发送方的ip 端口
    # 如果recv返回结果为空 证明客户端已经断开链接
    print(client_socket.recv(1024).decode('gbk'))

    client_socket.close()
    tcp_server.close()


if __name__ == '__main__':
    main()


