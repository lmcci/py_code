import socket

def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_client.connect((input('服务器地址：'), int(input('服务器端口：'))))

    download_file_name = input('下载的文件名：')

    tcp_client.send(download_file_name.encode('gbk'))

    download_file = tcp_client.recv(1024*1024)

    with open('res/下载_%s' % download_file_name, 'wb') as f:
        f.write(download_file)

    tcp_client.close()


if __name__ == '__main__':
    main()

