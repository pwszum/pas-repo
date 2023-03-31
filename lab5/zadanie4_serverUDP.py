#!/bin/env python3
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 6013)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

try:
    while True:
        # Wait for a connection
        print('waiting for a connection')

        # Receive the data in small chunks and retransmit it
        data, address = sock.recvfrom(4096)
        print('received "%s" from client ' % data.decode(), end='')
        print(address)
        if data:
            print('sending back "%s" to client ' % data.decode(), end='')
            print(address)
            print()
            sock.sendto(data, address)
except KeyboardInterrupt:
    print('\nProgram closed')
    sys.exit()
except:
    print('Error')
finally:
    sock.close()
