import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定自己的ip可以为空字符串
    udp_socket.bind(('', 8889))

    # 本次最大接收1024字节
    # receive_data = udp_socket.recvfrom(1024)

    # 返回一个元组 第一个是1024字节 第二个是元组 元组第一个是发送方ip 第二个是发送方端口
    # print(receive_data)  # (b'hello', ('192.168.1.103', 8099))

    while True:
        # 调用recvform之前 会把接收到的数据暂时存储起来 等到调用的时候在去取
        msg, send_tuple = udp_socket.recvfrom(1024)

        msg = msg.decode('gbk')

        print(msg)

        if msg == 'END':
            break

    udp_socket.close()


if __name__ == '__main__':
    main()
