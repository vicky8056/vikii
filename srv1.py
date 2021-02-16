import socket
name=input("Enter the name:")
s=socket.socket()

s.bind(('127.0.0.1',1234))
s.listen(5)
c,addr=s.accept()
while True:
  c.send(bytes(name,'utf-8'))
  m=c.recv(1024)
  print(m)
s.close()
