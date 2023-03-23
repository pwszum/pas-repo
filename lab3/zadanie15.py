#!/bin/env python3
import sys
import socket
import struct

if __name__ == '__main__':
    datagram = struct.pack("!78B",
        0x45, 0x00, 0x00, 0x4e, 0xf7, 0xfa, 0x40, 0x00, 0x38, 0x06, 0x9d, 0x33, 0xd4, 0xb6, 0x18, 0x1b,
        0xc0, 0xa8, 0x00, 0x02, 0x0b, 0x54, 0xb9, 0xa6, 0xfb, 0xf9, 0x3c, 0x57, 0xc1, 0x0a, 0x06, 0xc1,
        0x80, 0x18, 0x00, 0xe3, 0xce, 0x9c, 0x00, 0x00, 0x01, 0x01, 0x08, 0x0a, 0x03, 0xa6, 0xeb, 0x01,
        0x00, 0x0b, 0xf8, 0xe5, 0x6e, 0x65, 0x74, 0x77, 0x6f, 0x72, 0x6b, 0x20, 0x70, 0x72, 0x6f, 0x67,
        0x72, 0x61, 0x6d, 0x6d, 0x69, 0x6e, 0x67, 0x20, 0x69, 0x73, 0x20, 0x66, 0x75, 0x6e)

    version = struct.unpack("!78B", datagram)[0] // 16
    sourceIP = struct.unpack("!78B", datagram)[12:16]
    destinationIP = struct.unpack("!78B", datagram)[16:20]
    protocol = struct.unpack("!78B", datagram)[9]

    sourcePort, destinationPort = struct.unpack("!39H", datagram)[10:12]
    data = struct.unpack("!78B", datagram)[52:]

    message1 = "zad15odpA;ver;"
    message1 += str(version)
    message1 += ";srcip;"
    message1 += str(sourceIP[0]) + '.' + str(sourceIP[1]) + '.' + str(sourceIP[2]) + '.' + str(sourceIP[3])
    message1 += ";dstip;"
    message1 += str(destinationIP[0]) + '.' + str(destinationIP[1]) + '.' + str(destinationIP[2]) + '.' + str(destinationIP[3])
    message1 += ";type;"
    message1 += str(protocol)

    message2 = "zad15odpB;srcport;"
    message2 += str(sourcePort)
    message2 += ";dstport;"
    message2 += str(destinationPort)
    message2 += ";data;"
    for c in data:
        message2 += chr(c)


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)

    client_socket.sendto(message1.encode(), ("212.182.24.27", 2911))
    try:
        result = client_socket.recv(4096).decode()
        print(result)
    except socket.error as e:
        print('socket.error exception: %s' % e)
        client_socket.close()
        sys.exit()

    if result == "TAK":
        client_socket.sendto(message2.encode(), ("212.182.24.27", 2911))
        try:
            result = client_socket.recv(4096).decode()
            print(result)
        except socket.error as e:
            print('socket.error exception: %s' % e)

    client_socket.close()
