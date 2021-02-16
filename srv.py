import socket
s=socket.socket()
s.bind(('127.0.0.1',2850))
s.listen(5)
c,addr=s.accept()
c.send(b'hello')
s.close()
