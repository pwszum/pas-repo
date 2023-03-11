#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(5)

    try:
        client_socket.connect(('127.0.0.1', 2900))
        print('Connected')
    except socket.error as exc:
        print('Wyjatek socket.error : %s' % exc)
        sys.exit()

    while True:
        message = input()

        if not message:
            break

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)

    client_socket.close()
