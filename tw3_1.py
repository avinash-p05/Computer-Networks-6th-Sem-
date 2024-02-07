# Server (server.py)

import socket

def start_udp_server():
	# Create a UDP socket
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Bind the socket to a specific address and port
	server_address = ('localhost', 12345)
	server_socket.bind(server_address)

	print("UDP server waiting for response")
	print(f"Server listening on {server_address}")

	while True:
		# Wait for a message from the client
		data, client_address = server_socket.recvfrom(1024)
		print(f"Received message from {client_address}: {data.decode()}")

		# Send the same message back to the client
		# server_socket.sendto(data, client_address)
  
	#close the connection when done
	# server_socket.close()

if __name__ == "__main__":
	start_udp_server()
