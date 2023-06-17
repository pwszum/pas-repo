#!/usr/bin/env python3
import socket
import sys

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(30)

    try:
        client_socket.connect(('httpbin.org', 80))
        print('Connected')
    except socket.error as e:
        print('socket.error exception: %s' % e)
        sys.exit()

    message = "GET /image/png HTTP/1.1\r\nHOST: httpbin.org\r\n\r\n"

    client_socket.send(message.encode())

    data = client_socket.recv(16384)

    fd = open("image.png", "wb")
    fd.write(data.split(b'\r\n\r\n')[1])

    fd.close()
    client_socket.close()
