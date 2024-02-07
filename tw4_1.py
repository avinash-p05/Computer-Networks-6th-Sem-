import socket
#server
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('localhost',12345)
server_socket.bind(server_address)

server_socket.listen(5)

print("TCP server is waiting for connections....")

while True:
	client_socket,client_address=server_socket.accept()
	print(f'connected to{client_address}')

	try:
		data=client_socket.recv(1024)
		if data:
			print(f'Recieved data:{data.decode()}')
		else:
			break
	finally:
		client_socket.close()
