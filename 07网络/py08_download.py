import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 本地端口8888
    tcp_socket.bind(('', 15963))

    download_file_path = input('请输入要下载的文件名:')

    # 远程ip 192.168.1.103    远程端口8888
    tcp_socket.connect(('192.168.1.100', 15963))

    tcp_socket.send(download_file_path.encode('utf-8'))

    # 下载的长度
    content_length = 0

    while True:
        # 一直获取数据
        recv_data = tcp_socket.recv(1024 * 1024)

        if recv_data:
            with open('download/%s' % get_file_name(download_file_path), 'ba') as f:
                content_length += 1
                print('已经下载了 %d' % (content_length // 8))
                f.write(recv_data)
        else:
            print('链接已关闭')
            break

    tcp_socket.close()


def get_file_name(path):
    rindex = path.rfind('\\')
    # rindex = path.rfind('/')

    if rindex == -1:
        return path
    else:
        return path[rindex + 1:]


if __name__ == '__main__':
    main()













