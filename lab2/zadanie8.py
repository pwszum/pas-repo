#!/usr/bin/env python3
import socket
import sys

n = len(sys.argv)

if n != 2:
    print('Invalid number of arguments')
    sys.exit()

HOST = sys.argv[1]

try:
    print('Type port to start from: ', end='')
    first = int(input())
    print('Type port to end on: ', end='')
    last = int(input())
    print('Set timeout to (in seconds): ', end='')
    tm = float(input())
    if first > last or first < 0 or last < 0 or first > 65353 or last > 65353:
        print('Invalid port range')
        sys.exit()
except:
    print('Invalid value')
    sys.exit()

print('Scanning ports from ' + str(first) + ' to ' + str(last) + ' for ' + HOST + '...')

for port in range(first, last+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(tm)
    try:
        sock.connect((HOST, port))
        print('Port ' + str(port) + ' is open')
        try:
            serviceName = socket.getservbyport(port, 'tcp')
            print('Name of the service: ' + serviceName)
        except socket.error as e:
            print('Name of the service cannot be retrieved for port ' + str(port))
    except KeyboardInterrupt:
        print("\nProgram closed")
        sock.close()
        sys.exit()
    except:
        pass

    sock.close()

print('Scanning complete')
