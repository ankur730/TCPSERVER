import socket

host = "94.142.241.111"
port = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((host,port))

msg = "Hello World , this is the message from the client"
s.send(msg.encode('ascii'))

rmsg = s.recv(1024)

print(rmsg.decode('ascii'))
s.close()
