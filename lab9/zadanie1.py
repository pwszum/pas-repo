#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)

    try:
        client_socket.connect(('info.cern.ch', 80))
        print('Connected')
    except socket.error as e:
        print('socket.error exception: %s' % e)
        sys.exit()

    message = "GET / HTTP/1.1\r\nHOST: info.cern.ch\r\nUSER-AGENT: Safari/7.0.3\r\n\r\n"

    client_socket.send(message.encode())

    data = client_socket.recv(4096).decode()
    print(data)

    client_socket.close()
