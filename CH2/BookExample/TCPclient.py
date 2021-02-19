from socket import *


def main():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024).decode()
    print(modifiedSentence)
    clientSocket.close()
    input()


if __name__ == '__main__':
    main()
