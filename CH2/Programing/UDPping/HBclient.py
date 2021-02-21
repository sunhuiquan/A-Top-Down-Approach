# Task 2
from socket import *
import time


def main():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    times = 0
    while True:
        times += 1
        message = 'HeartBeat ' + str(time.time())
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        print('Have sent to server %d times.' % (times))
        time.sleep(4.9)  # Other code will costs time too.
    clientSocket.close()

if __name__ == '__main__':
    main()
