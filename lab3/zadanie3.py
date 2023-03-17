#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)

    try:
        client_socket.connect(('212.182.24.27', 2900))
        print('Connected')
    except socket.error as exc:
        print('socket.error exception: %s' % exc)
        sys.exit()

    while True:
        try:
            message = input('> ')
        except KeyboardInterrupt:
            print('\nProgram closed')
            break

        if not message:
            break

        client_socket.send(message.encode())
        data = client_socket.recv(4096).decode()
        print(data)

    client_socket.close()
