import socket
s=socket.socket()
host=socket.gethostname()
port=1256
s.connect((host,port))
print s.recv(1024)
