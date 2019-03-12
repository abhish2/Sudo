import socket
port=33333
ADDRESS= '127.0.0.1'
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#print("123")
	
s.bind((ADDRESS,port))
while True:

	data, addr = s.recvfrom(1024)
	#print("received")
	sata=data.decode('utf-8')
	
	print (sata)

