import socket
# 字符串 转 字节  ''.encode('utf-8')      b''


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送数据 可以不绑定本地端口 使用随机端口
    udp_socket.bind(('', 8889))

    while True:
        input_str = input('要发送的数据')

        if input_str == 'END':
            break

        # 不能直接发送字符串     TypeError: a bytes-like object is required, not 'str'
        # ip是str 端口是int
        udp_socket.sendto(input_str.encode('utf-8'), ('192.168.1.103', 8888))

    udp_socket.close()


if __name__ == '__main__':
    main()
