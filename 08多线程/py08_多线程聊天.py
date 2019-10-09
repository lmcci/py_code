import threading
import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('', 8888))

    threading.Thread(target=send, args=(udp_socket, )).start()
    threading.Thread(target=recv, args=(udp_socket, )).start()


def send(udp_socket):
    while True:
        udp_socket.sendto(input('').encode('gbk'), ('192.168.1.103', 8888))


def recv(udp_socket):
    while True:
        recv_data, (recv_ip, recv_port) = udp_socket.recvfrom(1024)

        print('%s:%d说：%s' % (recv_ip, recv_port, recv_data.decode('gbk')))


if __name__ == '__main__':
    main()

