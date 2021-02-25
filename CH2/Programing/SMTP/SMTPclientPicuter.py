# Task 3 2021/2/25 2:49 SunHuiquan

from socket import *
import base64

emailFrom = '1503028072@qq.com'
emailTo = 'sunhuiquan@yeah.net'
emailBase64 = 'MTUwMzAyODA3MkBxcS5jb20='
passwordBase64 = 'd21sbWtyd3N3ZGNkZ2FjaQ=='

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.qq.com'  # Fill 1

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill 2
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Auth login
authMsg = 'auth login\r\n'
clientSocket.send(authMsg.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '334':
    print('334 reply not received from server.')

clientSocket.send(str(emailBase64 + '\r\n').encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[3] != '334':
    print('334 reply not received from server.')

clientSocket.send(str(passwordBase64 + '\r\n').encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill 3
clientSocket.send(str('MAIL FROM:<' + emailFrom + '>\r\n').encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
# Fill 4
clientSocket.send(str('RCPT TO:<' + emailTo + '>\r\n').encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
# Fill 5
clientSocket.send('Data\r\n'.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '354':
    print('354 reply not received from server.')

# Send message data.
# Fill 6
send_text = 'from:%s\r\nto:%s\nsubject:hello,you!\
\r\nContent-Type:text/plain\r\n' % (emailFrom, emailTo)+'\r\n'+'hello'+'\r\n'
print(send_text)
send_text = send_text.encode()

send_html = 'from:%s\nto:%s\nsubject:hello,you!\
\r\nContent-Type:text/html\r\n' % (emailFrom, emailTo)+'\r\n'+'<h1>hello</h1><img src="https://github.com/sunhuiquan/mit_6.S081_lab/blob/util/IMG/lab1.png">'+'\r\n'
print(send_html)
send_html = send_html.encode()

with open("02.jpg", "rb") as f:
    f = base64.b64encode(f.read())
send_image = ('from:%s\nto:%s\nsubject:hello,you!\
\r\nContent-Type:image/JPEG\r\nContent-transfer-encoding:base64\r\n' % (emailFrom, emailTo)+'\r\n').encode()+f+'\r\n'.encode()

send_text_with_image = 'from:%s\nto:%s\nsubject:hello,you!\
\r\nContent-Type:multipart/mixed;boundary="simple"\r\n\r\n--simple\r\n' % (emailFrom, emailTo)+'Content-Type:text/html\r\n\r\n<h1>hello</h1><img src="https://github.com/sunhuiquan/mit_6.S081_lab/blob/util/IMG/lab1.png">\r\n\r\n'
send_text_with_image = send_text_with_image.encode()+'--simple\r\n'.encode() + \
    'Content-Type:image/JPEG\r\nContent-transfer-encoding:base64\r\n\r\n'.encode()
with open("02.jpg", "rb") as f:
    f = base64.b64encode(f.read())
send_text_with_image += f
send_text_with_image += '\r\n--simple\r\n'.encode()

temp = send_text_with_image
print(temp)
clientSocket.send(temp)


temp = '\r\n.\r\n'
print(temp)
clientSocket.send(temp.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

# Send QUIT command and get server response.
# Fill 8
clientSocket.send('QUIT\r\n'.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '221':
    print('221 reply not received from server.')

# Close the client socket.
clientSocket.close()
