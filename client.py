import socket
import sys

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
print >> sys.stderr, 'connecting to %s port %s' % (TCP_IP, TCP_PORT)
s.connect((TCP_IP, TCP_PORT))

try:

    # Send data
    CLIENT_MESSAGE = 'Hello. I am the client.'
    print >> sys.stderr, 'sending "%s"' % CLIENT_MESSAGE
    s.sendall(CLIENT_MESSAGE)

    # Look for the response
    amount_received = 0
    amount_expected = len(CLIENT_MESSAGE)

    while amount_received < amount_expected:
        data = s.recv(BUFFER_SIZE)
        amount_received += len(data)
        print >> sys.stderr, 'received "%s"' % data

finally:
    print >> sys.stderr, 'closing socket'
    s.close()
