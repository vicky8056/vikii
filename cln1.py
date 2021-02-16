wqimport socket
name1=input("Enter the name:")
s=socket.socket()
s.connect(('127.0.0.1',1234))
while True: 
  s.send(bytes(name1,'utf-8')) 
  m=s.recv(1024)
  print(m)
s.close()

