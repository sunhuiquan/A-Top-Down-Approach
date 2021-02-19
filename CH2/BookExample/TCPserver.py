from socket import *


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    print('Ready to receive!')
    while True:
        connectSocket, addr = serverSocket.accept()
        sentence = connectSocket.recv(1024).decode()
        capitailizedSentence = sentence.upper()
        connectSocket.send(capitailizedSentence.encode())
        connectSocket.close()


if __name__ == '__main__':
    main()
