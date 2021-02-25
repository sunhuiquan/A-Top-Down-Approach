#coding:utf-8
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
    print(message.split()[1])
    filename = message.split()[1].partition("//")[2]
    # print(filename)
    fileExist = "false"
    filetouse = "/" + filename
    # print(filetouse)

    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        tcpCliSock.sendall(outputdata)
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
                tcpCliSock.sendall(buff)
                # Fill in end.  
                           
                # # Create a temporary file on this socket and ask port 80
                # fileobj = c.makefile('r', 0)
                # fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")
                # # Read the response into buffer
                # # Fill in start.
                # # Fill in end.

                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                fn = "./" + filename
                # 文件名不能有/所以要换成别的字符比如_，记得查找的创建文件的时候调整一下文件名字符串
                tmpFile = open(fn, "w")
                # Fill in start.
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
