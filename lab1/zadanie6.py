#!/usr/bin/env python3
import socket
import sys

n = len(sys.argv)

if n < 3:
    print('Not enough arguments')
    sys.exit()

HOST = sys.argv[1]
try:
    PORT = int(sys.argv[2])
except:
    print('Invalid port')
    sys.exit()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect((HOST, PORT))
    print('Connected successfully')
except socket.error as e:
    print('socket.error exception: %s' % e)

sock.close()
