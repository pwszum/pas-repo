#!/usr/bin/env python3
import socket
import sys
import time

if __name__ == '__main__':
    start = time.perf_counter()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    message = 'Hello world! Hello world! Hello world! Hello world! Hello world!'

    client_socket.sendto(message.encode(), ('127.0.0.1', 6013))

    try:
        data = client_socket.recv(4096).decode()
        print(data)
    except socket.error as e:
        print('socket.error exception: %s' % e)

    client_socket.close()

    end = time.perf_counter()
    print(f'{end - start:0.4f} seconds')
