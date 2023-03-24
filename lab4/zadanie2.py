#!/bin/env python3
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 6001)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    try:
        connection, client_address = sock.accept()
    except KeyboardInterrupt:
        print('\nProgram closed')
        sys.exit()
    except:
        print('Error')
    try:
        print('connection from %s' % client_address[0])

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096)
            print('received "%s"' % data.decode())
            if data:
                print('sending back "%s" to client' % data.decode())
                connection.sendall(data)
            else:
                print('no more data from %s' % client_address[0])
                break
    finally:
        # Clean up the connection
        connection.close()
