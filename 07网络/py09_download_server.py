import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 提供服务的端口是8888
    tcp_socket.bind(('', 8888))

    # 监听链接
    tcp_socket.listen(128)

    while True:
        # 有客户端链接上来
        tcp_client_socket, tcp_client_info = tcp_socket.accept()

        print('有客户端链接上来 ip:%s 端口%d' % tcp_client_info)

        download_file_name = tcp_client_socket.recv(1024).decode('utf-8')

        print('%s 要下载 %s' % (tcp_client_info[0], download_file_name))

        try:
            f = open(download_file_name, 'rb')
            while True:
                file_data = f.read(1024 * 1024)
                if file_data:
                    tcp_client_socket.send(file_data)
                else:
                    break
            f.close()
        except Exception as e:
            print(e)
            print('文件异常')
            tcp_client_socket.send('None'.encode('utf-8'))

        tcp_client_socket.close()


if __name__ == '__main__':
    main()

