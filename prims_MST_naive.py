#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 17:04:56 2018

Prim's Algorithm for Minimum Spanning Tree

@author: Alex Lau
"""
# Function for reading text file and build Graph
def txt_to_graph(filename,node_num):
    file = open(filename,"r")
    node_list = [i+1 for i in range(node_num)]
    graph = build_graph(node_list)
    i = 0
    for line in file:
        i+=1
        if i == 1:
            pass
        else:
            num_list = line.split()
            num_list = [int(i) for i in num_list]
            node1 = num_list[0]
            node2 = num_list[1]
            cost = num_list[2]
            add_edge(graph,node1,node2,cost)
    file.close()
    return graph


# Functions related to Graph
def build_graph(vertex_list):
    graph = {}
    for vertex in vertex_list:
        graph[vertex] = {}
    return graph

def add_edge(graph,u,v,cost):
    graph[u][v] = cost
    graph[v][u] = cost


# Functions for Prim MST
def Prim_MST(graph):
    V = set(graph.keys())
    S = {1}
    T = []
    vertex_check = {vertex: False for vertex in V}
    vertex_check[1] = True
    global_cost = 0
    while S != V:
        local_cost = 10000
        local_vertex = 0
        for vertex_include in S:
            for adj_vertex, cost in graph[vertex_include].items():
                if vertex_check[adj_vertex] == False:
                    if cost < local_cost:
                        local_cost = cost
                        local_edge = [vertex_include, adj_vertex]
                        local_vertex = adj_vertex
        S.add(local_vertex)
        T.append(local_edge)
        global_cost += local_cost
        vertex_check[local_vertex] = True
    print('The minimum cost = ', global_cost)
    return S, T, global_cost

# Test Case
test1 = build_graph([1,2,3,4,5,6])
add_edge(test1,1,2,6)
add_edge(test1,1,4,5)
add_edge(test1,1,5,4)
add_edge(test1,2,4,1)
add_edge(test1,2,5,2)
add_edge(test1,2,3,5)
add_edge(test1,2,6,3)
add_edge(test1,3,6,4)
add_edge(test1,4,5,2)
add_edge(test1,5,6,4)

Prim_MST(test1)

# Real Problem
g = txt_to_graph('edges.txt', 500)
s, t, global_cost = Prim_MST(g)
print(global_cost)
