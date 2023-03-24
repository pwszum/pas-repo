#!/bin/env python3
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('127.0.0.1', 6003)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

try:
    while True:
        # Wait for a connection
        print('waiting for a connection')

        # Receive the data in small chunks and retransmit it
        num1 = sock.recvfrom(4096)[0].decode()
        op, address = sock.recvfrom(4096)
        op = op.decode()
        num2 = sock.recvfrom(4096)[0].decode()
        print('received "%s %s %s" from client ' % (num1, op, num2), end='')
        print(address)

        data = ''

        try:
            x,y = (float(num1), float(num2))
        except:
            data = 'Error: at least one argument is not a number'

        if not data and num1 and op and num2:
            if op == '+':
                data = float(num1) + float(num2)
            elif op == '-':
                data = float(num1) - float(num2)
            elif op == '*':
                data = float(num1) * float(num2)
            elif op == '/':
                if float(num2) == 0.0:
                    data = 'Cannot divide by zero'
                else:
                    data = float(num1) / float(num2)
            else:
                data = 'Unsupported operator (use only +,-,*,/)'
        if data:
            print('sending back "%s" to client ' % str(data), end='')
            print(address)
            print()
            sock.sendto(str(data).encode(), address)
except KeyboardInterrupt:
    print('\nProgram closed')
    sys.exit()
except:
    print('Error')
finally:
    sock.close()
