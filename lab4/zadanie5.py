#!/bin/env python3
import ipaddress
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 6004)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

try:
    while True:
        # Wait for a connection
        print('waiting for a connection')

        # Receive the data in small chunks and retransmit it
        data, address = sock.recvfrom(4096)
        data = data.decode()
        print('received "%s" from client ' % data, end='')
        print(address)

        try:
            ipaddress.ip_address(data)
            try:
                hostname = socket.gethostbyaddr(data)
                message = 'Hostname for IP address ' + data + ': ' + hostname[0]
            except:
                message = 'Couldn\'t get hostname for ' + data
        except:
            message = 'Invalid IP address: ' + data

        if data and message:
            print('sending "%s" to client ' % message, end='')
            print(address)
            print()
            sock.sendto(message.encode(), address)
except KeyboardInterrupt:
    print('\nProgram closed')
    sys.exit()
except:
    print('Error')
finally:
    sock.close()
