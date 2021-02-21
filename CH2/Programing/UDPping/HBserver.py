# Task 2
from socket import *
import time


def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.settimeout(5)
    serverSocket.bind(('', serverPort))
    print('Ready to receive.')
    times = 0
    missCon = 0
    ready = 0
    while True:
        times += 1
        try:
            message, clientAddr = serverSocket.recvfrom(1024)
            missCon = 0
            if ready == 0:
                ready = 1
            message = message.decode().split()[1]
            sentTime = float(message)
            print('Time %d: %.3f.' % (times, float(time.time()) - sentTime))
        except Exception as e:
            # print(e) Use it for contest is very important.
            if ready == 0:
                continue
            else:
                missCon += 1
                print('Time %d: miss.' % (times))
                if(missCon == 3):
                    print('App exit.')
                    break
    serverSocket.close()
    input()


if __name__ == '__main__':
    main()
