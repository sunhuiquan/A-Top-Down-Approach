# Task 1 2021/2/23 9:44 SunHuiquan

# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
#Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill here

    try:
        message = serverSocket.recv(1024)  # Fill
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # Fill

        # Send one HTTP header line into socket
        #Fill in start
        header = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(header.encode())
        #Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found)
        header = 'HTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(header.encode())  # Fill

    # Close client socket
    connectionSocket.close()  # Fill
serverSocket.close()
