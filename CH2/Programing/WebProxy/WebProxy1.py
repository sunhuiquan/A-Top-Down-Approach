# Task 1 2021/2/26 9:20 SunHuiquan

# coding:utf-8
from socket import *
import sys

if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n\
    [server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
serverPort = int(sys.argv[1])
tcpSerSock.bind(('', serverPort))
tcpSerSock.listen(10)
# Fill in end.

while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(4096).decode()  # Fill
    print(message)

    # Extract the filename from the given message
    filename = message.split()[1].partition("//")[2]
    # print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    # print(filetouse)

    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:].replace('/', '_'), "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        if(outputdata[0].split()[1] != '304'):
            tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
            tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        print(outputdata)
        for s in outputdata:
            tcpCliSock.send(s.encode())
        # Fill in end.
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)  # Fill
            resourceServerName = filename.partition("/")[0]
            print(resourceServerName)

            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((resourceServerName, 80))
                c.sendall(message.encode())
                buff = c.recv(4096)
                print(buff)
                tcpCliSock.sendall(buff)
                # Fill in end.

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                fn = filename.replace('/', '_')
                # print(fn)
                # 文件名不能有/所以要换成别的字符比如_，记得查找的创建文件的时候调整一下文件名字符串
                tmpFile = open("./" + fn, "w")
                # Fill in start.
                print('------------'+str(len(buff)))
                tmpFile.writelines(buff.decode().replace('\r\n', '\n'))
                tmpFile.close()
                # Fill in end.
            except Exception as e:
                print(e)
                print("Illegal request")
        else:
            # HTTP response message for file not found
            # Fill in start.
            # 这里是指在资源服务器上找不到，不是代理服务器找不到
            print('404 File Not Found.')
            # Fill in end.
            # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
# Fill in end.
