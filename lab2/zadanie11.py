#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)

    try:
        client_socket.connect(('212.182.24.27', 2908))
        print('Connected')
    except socket.error as e:
        print('socket.error exception: %s' % e)
        sys.exit()

    message = input('> ')
    while len(message) < 20:
        message += ' '
    if len(message) > 20:
        message = message[:20]

    client_socket.send(message.encode())

    data = client_socket.recv(20).decode()
    print(data)

    client_socket.close()
