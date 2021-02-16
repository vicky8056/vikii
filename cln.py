import socket
s=socket.socket()
s.connect(('127.0.0.1',2850))
m=s.recv(1024)
print(m)
s.close()
