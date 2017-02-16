import socket

sock=socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'444')

data=conn.recv(2048)
sock.close()

print(data)
