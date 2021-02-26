# Task 2 2021/2/25 2:42 SunHuiquan

from socket import *
import ssl
# emailFrom = 'qq number@qq.com'
# emailTo = 'email to@yeah.net'
# emailBase64 = 'email from base64'
# passwordBase64 = 'password base64'

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.qq.com'  # Fill 1
context = ssl.create_default_context()
# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill 2
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 465))
clientSocketSSL = context.wrap_socket(clientSocket,server_hostname=mailserver)

recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocketSSL.send(heloCommand.encode())
recv1 = clientSocketSSL.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Auth login
authMsg = 'auth login\r\n'
clientSocketSSL.send(authMsg.encode())
recv2 = clientSocketSSL.recv(1024).decode()
print(recv2)
if recv2[:3] != '334':
    print('334 reply not received from server.')

clientSocketSSL.send(str(emailBase64 + '\r\n').encode())
recv3 = clientSocketSSL.recv(1024).decode()
print(recv3)
if recv3[3] != '334':
    print('334 reply not received from server.')

clientSocketSSL.send(str(passwordBase64 + '\r\n').encode())
recv4 = clientSocketSSL.recv(1024).decode()
print(recv4)
if recv4[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill 3
clientSocketSSL.send(str('MAIL FROM:<' + emailFrom + '>\r\n').encode())
recv5 = clientSocketSSL.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
# Fill 4
clientSocketSSL.send(str('RCPT TO:<' + emailTo + '>\r\n').encode())
recv6 = clientSocketSSL.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
# Fill 5
clientSocketSSL.send('Data\r\n'.encode())
recv7 = clientSocketSSL.recv(1024).decode()
print(recv7)
if recv7[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
# Fill 6
msgFormat = 'From:<' + emailFrom + '>\r\n'
msgFormat += 'To:<' + emailTo + '>\r\n'
msgFormat += 'Subject:send from python\r\n'
sendMsg = msgFormat + msg + endmsg
clientSocketSSL.send(sendMsg.encode())
recv8 = clientSocketSSL.recv(1024).decode()
print(recv8)
if recv8[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
# Fill 8
clientSocketSSL.send('QUIT\r\n'.encode())
recv9 = clientSocketSSL.recv(1024).decode()
print(recv9)
if recv9[:3] != '221':
    print('221 reply not received from server.')

# Close the client socket.
clientSocketSSL.close()
