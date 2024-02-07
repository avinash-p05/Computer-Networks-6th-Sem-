# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:02:06 2024

@author: Asus
"""

import socket

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_add = ('Localhost',1127)

socket.bind(server_add)

socket.listen(5)

print("TCP server is waiting for Connection.....")
print(f'Server listening on {server_add}')
while True:
    
    
    client_socket,client_address = socket.accept()
    print(f'Recieved message from {client_address}')
    
    try:
        data= client_socket.recv(1024)
        if data:
            print(f'data is {data.decode()}')
        else:
            break
    finally:
        client_socket.close()
        
        