import socket

sock=socket.socket()
sock.bind(("", 9090))
sock.listen(1)
conn, addr =sock.accept()

print('connected', addr)
while True:
    print("waiting for connection....")
    data=conn.recv(2048)
   
    if not data:
        break
    conn.send(data)
conn.close()
