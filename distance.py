# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:38:25 2024

@author: Asus
"""
import sys
class Network:
    def __init__(self,nodes):
        self.nodes = nodes
        self.distance_vector={}
        self.graph = {}
    
    def add_link(self,node1,node2,cost):
        if node1 not in self.graph:
            self.graph[node1]={}
        self.graph[node1][node2]=cost
        if node2 not in self.graph:
            self.graph[node2]={}
        self.graph[node2][node1]=cost
        
        
    def initialise_distance_vector(self,node):
        self.distance_vector[node]={node:0}
        for n in self.nodes:
            if  n!=node:
                self.distance_vector[node][n]=sys.maxsize
    
    
    def update_distance_vector(self,node):
        for dest in self.nodes:
            if dest!=node:
                min_cost = sys.maxsize
                for neighbour in self.graph[node]:
                    if dest in self.distance_vector[neighbour]:
                        cost = self.distance_vector[neighbour][dest]+self.graph[node][neighbour]
                        if cost<min_cost:
                            min_cost = cost
                self.distance_vector[node][dest]=min_cost
            
            
    def print_routing_table(self,node):
        print(f'Routing table for Node {node}')
        print("Destination  Cost")
        for dest,cost in self.distance_vector[node].items():
            if dest!=node:
                print(f'{dest}       {cost}')
        print()
        
        
        
if __name__=="__main__":
    nodes = [1, 2, 3, 4, 5]
    network = Network(nodes)

    # Add links between nodes with specified costs
    network.add_link(1, 2, 2)
    network.add_link(1, 3, 2)
    network.add_link(1, 4, 1)
    network.add_link(2, 3, 1)
    network.add_link(2, 5, 1)
    network.add_link(3, 4, 1)
    network.add_link(3, 5, 1)
    
    
    for node in nodes:
        network.initialise_distance_vector(node)
        
    num = 6
    
    for i in range(num):
        for node in nodes:
            network.update_distance_vector(node)
            
    for node in nodes:
        network.print_routing_table(node)
        
        
        
            
            
            
            
            
            
                        
                        
                        
                        