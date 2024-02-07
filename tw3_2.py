# Client (client.py)

import socket

def start_udp_client():
	# Create a UDP socket
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# Server address and port
	server_address = ('localhost', 12345)

	while True:
		# Get user input for the message
		message = input("Enter message to send (or 'exit' to quit): ")

		if message.lower() == 'exit':
			break

		# Send the message to the server
		client_socket.sendto(message.encode(), server_address)

	# Close the socket when done
	client_socket.close()

if __name__ == "__main__":
	start_udp_client()


					