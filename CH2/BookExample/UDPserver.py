from socket import *


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print('Ready to receive.')
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)


if __name__ == '__main__':
    main()
