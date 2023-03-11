#!/usr/bin/env python3
import ipaddress
import socket
import sys

n = len(sys.argv)

for i in range(1, n):
    try:
        ipaddress.ip_address(sys.argv[i])
        try:
            hostname = socket.gethostbyaddr(sys.argv[i])
            print('Hostname for IP address ' + sys.argv[i] + ': ' + hostname[0])
        except:
            print('Couldn\'t get hostname for ' + sys.argv[i])
    except:
        print('Invalid IP address: ' + sys.argv[i])
