# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 09:24:12 2024

@author: Asus
"""

import socket


socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_add = ('Localhost',1127)
socket.connect(server_add)

while True:
    message=input("Enter the message: ")
    if message.lower()=='exit':
        break
    socket.sendto(message.encode(), server_add)
socket.close()
print("Exited")