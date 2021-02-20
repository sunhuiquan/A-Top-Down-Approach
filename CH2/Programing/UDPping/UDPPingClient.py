# Ping sequence_number time
from socket import *
import time


def main():
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)
    serverName = 'localhost'
    serverPort = 12000
    miss = 0
    shortest = 100
    longest = 0
    sumRtt = 0
    for i in range(10):  # from 0, 1, 2, ..., 8, 9
        start = time.time()
        message = ('Ping %d %f' % (i + 1, start))
        try:
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            receiveMessage, serverAddr = clientSocket.recvfrom(1024)
            end = time.time()
            rtt = end - start
            print('RTT is %d %.3fs' % (i + 1, rtt))
            if rtt > longest:
                longest = rtt
            if rtt < shortest:
                shortest = rtt
                sumRtt += rtt
        except Exception as e:
            miss += 1
            print('Request %d timed out' % (i + 1))
    print('\nshortest: %.3fs, longest: %.3fs, average: %.3fs' %
          (shortest, longest, sumRtt / 10))
    print('send: %d, receive: %d, miss: %d, missing rate: %d%%' %
          (10, 10 - miss, miss, miss * 10))
    clientSocket.close()
    input()


if __name__ == '__main__':
    main()
