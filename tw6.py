# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:05:53 2024

@author: Asus
"""

count = 1000
packets = [200, 500, 600, 700, 450, 400, 200]

length = len(packets)
index = length - 1
while index >= 0:
    while index >= 0 and count > packets[index]:
        print("Packet moved out of queue is", packets[index])
        count = count - packets[index]
        index = index - 1
    if index >= 0:
        print("Count is less than packet value:")
        count = 1000
print("All packets are moved out of the queue successfully")