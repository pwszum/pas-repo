#!/bin/env python3
import socket
import struct

if __name__ == '__main__':
    datagram = struct.pack("!40B",
        0x0b, 0x54, 0x89, 0x8b, 0x1f, 0x9a, 0x18, 0xec, 0xbb, 0xb1, 0x64, 0xf2, 0x80, 0x18,
        0x00, 0xe3, 0x67, 0x71, 0x00, 0x00, 0x01, 0x01, 0x08, 0x0a, 0x02, 0xc1, 0xa4, 0xee,
        0x00, 0x1a, 0x4c, 0xee, 0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x3a, 0x29)

    source, destination = struct.unpack("!20H", datagram)[0:2]
    data = struct.unpack("!40B", datagram)[32:]

    message = "zad13odp;src;"
    message += str(source)
    message += ";dst;"
    message += str(destination)
    message += ";data;"
    for c in data:
        message += chr(c)


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    client_socket.sendto(message.encode(), ("212.182.24.27", 2909))
    try:
        result = client_socket.recv(4096).decode()
        print(result)
    except socket.error as e:
        print('socket.error exception: %s' % e)

    client_socket.close()
