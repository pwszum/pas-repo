#!/usr/bin/env python3
import ipaddress

print('IP Address: ', end='')
ip = input()

try:
    ipaddress.ip_address(ip)
    print('Valid IP address')
except:
    print('Invalid IP address')
