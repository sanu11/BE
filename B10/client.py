import socket
s=socket.socket()
port=12346
host=socket.gethostname()
s.connect((host,port))
ip=raw_input("Enter input\n")
s.send(ip)
print "Sending input \n"
print "Result \n"
print s.recv(1024)

s.close
