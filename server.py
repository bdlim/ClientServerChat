import socket
import sys

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024
print >> sys.stderr, 'starting up on %s port %s' % (TCP_IP, TCP_PORT)
s.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
s.listen(5)

SERVER_MESSAGE = 'Hello. I am the server.'

while True:
    # Wait for incoming connections
    print >> sys.stderr, 'waiting for connection'
    connection, client_address = s.accept()

    try:
        print >> sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(BUFFER_SIZE)
            print >> sys.stderr, 'received "%s"' % data
            if data:
                print >> sys.stderr, 'sending response to the client'
                connection.sendall(SERVER_MESSAGE)
            else:
                print >> sys.stderr, 'no more data from', client_address
                break
    finally:
        # Clean up the connection
        connection.close()
