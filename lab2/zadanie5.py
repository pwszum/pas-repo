#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    while True:
        try:
            message = input('> ')
        except KeyboardInterrupt:
            print('\nProgram closed')
            break

        if not message:
            break

        client_socket.sendto(message.encode(), ('212.182.24.27', 2901))
        try:
            data = client_socket.recv(4096).decode()
            print(data)
        except socket.error as e:
            print('socket.error exception: %s' % e)

    client_socket.close()
