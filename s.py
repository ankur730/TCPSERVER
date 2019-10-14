import socket

host = "94.142.241.111"
port = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind((host,port))

s.listen(5)

while(True):
	c,addr=s.accept()
	rmsg=c.recv(1024)
	print(rmsg.decode("ascii"))

	msg="Hello World. This is server"
	c.send(msg.encode("ascii"))


s.close()
