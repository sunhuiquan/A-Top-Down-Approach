# Task 3 2021/2/23 14:14 SunHuiquan

from socket import *


def main():
    serverName = 'localhost'
    serverPort = 6789
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    rqeuestFile = input('What are you looking for?\n')
    requestHeader = 'Get /' + rqeuestFile + ' HTTP/1.1\r\n'
    clientSocket.send(requestHeader.encode())
    message = clientSocket.recv(1024).decode()
    print(message)
    if int(message.split()[1]) == 200:
        length = int(message.split()[4])
        body = ''
        for i in range(length):
            body += clientSocket.recv(1024).decode()
        print(body)
    else:
        print('Can\'t find the file.')
    clientSocket.close()
    input()


if __name__ == '__main__':
    main()
