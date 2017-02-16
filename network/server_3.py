#! usr/bin/python3
from time import ctime
import socket

HOST=''
PORT=21567
BUFSIZ = 1024
ADDR=(HOST, PORT)
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print ("waiting for connection....")
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        #tcpCliSock.send(bytes('You sent me "{}"'.format(data.decode('utf8')), 'utf8'))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data)))
    tcpCliSock.close()
tcpSerSock.close()
