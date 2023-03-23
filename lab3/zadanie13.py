#!/bin/env python3
import socket
import struct

if __name__ == '__main__':
    datagram = struct.pack("!36B",
        0xed, 0x74, 0x0b, 0x55, 0x00, 0x24, 0xef, 0xfd, 0x70, 0x72, 0x6f, 0x67, 0x72, 0x61,
        0x6d, 0x6d, 0x69, 0x6e, 0x67, 0x20, 0x69, 0x6e, 0x20, 0x70, 0x79, 0x74, 0x68, 0x6f,
        0x6e, 0x20, 0x69, 0x73, 0x20, 0x66, 0x75, 0x6e)

    source, destination, length, checksum = struct.unpack("!18H", datagram)[0:4]
    data = struct.unpack("!36B", datagram)[8:]

    message = "zad14odp;src;"
    message += str(source)
    message += ";dst;"
    message += str(destination)
    message += ";data;"
    for c in data:
        message += chr(c)


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    client_socket.sendto(message.encode(), ("212.182.24.27", 2910))
    try:
        result = client_socket.recv(4096).decode()
        print(result)
    except socket.error as e:
        print('socket.error exception: %s' % e)

    client_socket.close()
