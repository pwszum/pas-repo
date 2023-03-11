#!/usr/bin/env python3
import socket
import struct
import time

if __name__ == '__main__':

    sockIPv4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockIPv4.settimeout(5)

    data = '\x1b' + 47 * '\0'
    REF_TIME_1970 = 2208988800

    sockIPv4.sendto(data.encode('utf-8'), ('ntp.task.gda.pl', 123))

    data, address = sockIPv4.recvfrom(1024)
    if data:
        t = struct.unpack('!12I', data)[10]
        t -= REF_TIME_1970

    print(time.ctime(t))

    sockIPv4.close()
