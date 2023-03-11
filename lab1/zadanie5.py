#!/usr/bin/env python3
import ipaddress
import socket
import sys

n = len(sys.argv)

for i in range(1, n):
    try:
        ip = socket.gethostbyname(sys.argv[i])
        print('IP address for hostname ' + sys.argv[i] + ': ' + ip)
    except:
        print('Couldn\'t get IP address')
