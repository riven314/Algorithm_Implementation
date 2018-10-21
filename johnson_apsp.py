#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:50:06 2018


@author: Alex Lau
"""
# graph.nodeList: dict
import numpy as np
from operator import itemgetter
from collections import defaultdict
import time
from heapdict import heapdict

###########################################
########### BELLMEN FORD ALGO #############
###########################################
filename_1 = 'g3.txt'


def Johnson_Algo(graph_dict):
    # Make node with no outflow edge visible
    #graph_dict = restruct_graph(graph_dict)

    # Run Bellman-ford to get reweight factor
    # Check for negative cycle
    start = time.time()
    arti_graph_dict = add_arti_node(graph_dict)
    reweight_dict = get_reweight_dict(arti_graph_dict)
    end = time.time()
    print('Bellman-ford completed, time elapsed: {}'.format(end - start))

    if reweight_dict == None:
        print('The graph has negative cycle so Algo is terminated!')
        return None
    # Reweigh the graph
    graph_dict = reweigh_graph(graph_dict, reweight_dict)
    #graph_dict.pop(0)

    # Iterate by Dijkstra
    start = time.time()
#    counter = 0
    min_path_list = []
    for vertex in graph_dict.keys():
#        if counter == limit:
#            break
#        counter +=1

        # Check if the node has outflow edges
        if len(graph_dict[vertex].keys()) != 0:
            # Get shortest path for each node
            shortest_path_dict = Dijkstra_Algo(graph_dict, vertex)
            # Recover its weight
            recover_min_path_dict = recover_weight(vertex,
                                                   shortest_path_dict,
                                                   reweight_dict)
            # Get min. shortest path with its node
            recover_min_path = get_min_path(recover_min_path_dict)
            min_path_list.append(recover_min_path)
    end = time.time()
    print('Dijkstra completed, time elapsed: {}'.format(end - start))
    # Extract the min path
    global_min_path = min(min_path_list)
    print('The shortest path = {}'.format(global_min_path))
    return global_min_path


# Output a new instance of graph dict with artificial node
def add_arti_node(graph_dict):
    arti_graph_dict = graph_dict.copy()
    all_nodes_list = list(arti_graph_dict.keys())
    init_edge = {node: 0 for node in all_nodes_list}
    # Artificial node 0
    arti_graph_dict[0] = init_edge
    return arti_graph_dict

# Output a dict with reweight factor for each node
def get_reweight_dict(graph_dict):
    reweight_dict = Bellman_Ford(graph_dict, 0)
    return reweight_dict

# Overwrite the input graph with edge weight updated
def reweigh_graph(graph_dict, reweight_dict):
    for start_vertex in graph_dict.keys():
        for end_vertex in graph_dict[start_vertex].keys():
            # Avoid node with no outflow edge
            if len(graph_dict[start_vertex].keys()) != 0:
                start_vertex_weight = reweight_dict[start_vertex]
                end_vertex_weight = reweight_dict[end_vertex]
                edge_weight = graph_dict[start_vertex][end_vertex]
                graph_dict[start_vertex][end_vertex] = edge_weight + start_vertex_weight - end_vertex_weight
    return graph_dict

# Overwrite the input graph so that its edge weight is recoverd
def recover_weight(source_vertex, shortest_path_dict, reweight_dict):
    recover_min_path_dict = {}
    source_v_weight = reweight_dict[source_vertex]
    for tail_v, min_path in shortest_path_dict.items():
        tail_v_weight = reweight_dict[tail_v]
        recover_min_path = min_path - source_v_weight + tail_v_weight
        recover_min_path_dict[tail_v] = recover_min_path
    return recover_min_path_dict

# Return the shortest path and its node
def get_min_path(shortest_path_dict):
    shortest_path = min(shortest_path_dict.values())
    return shortest_path

###########################################
########### BELLMEN FORD ALGO #############
###########################################
def Bellman_Ford(graph_dict, source_vertex):
    num = len(graph_dict)
    shortest_path_dict = init_inf_graph(graph_dict)
    shortest_path_dict[source_vertex] = 0
    # Compute shortest path for each target node
    for i in range(num - 1):
        for vertex in graph_dict.keys():
            ancestor = shortest_path_dict[vertex]
            parent_nodes = get_parent_nodes(graph_dict, vertex)
            if len(parent_nodes) != 0:
                local_shortest_path = get_local_shortest_path(graph_dict,
                                                              shortest_path_dict,
                                                              vertex,
                                                              parent_nodes)
                shortest_path = min(local_shortest_path, ancestor)
                shortest_path_dict[vertex] = shortest_path
    # Check if there are any negative cycle
    for vertex in graph_dict.keys():
        ancestor = shortest_path_dict[vertex]
        parent_nodes = get_parent_nodes(graph_dict, vertex)
        if len(parent_nodes) != 0:
            local_shortest_path = get_local_shortest_path(graph_dict,
                                                          shortest_path_dict,
                                                          vertex,
                                                          parent_nodes)
            shortest_path = min(local_shortest_path, ancestor)
            if ancestor != shortest_path:
                print('There exist negative cycle!!')
                return None
    return shortest_path_dict


###########################################
############# DIJKSTRA ALGO ###############
###########################################
def Dijkstra_Algo(graph_dict, source_v):
    # Init vertex sets and edge heap
    v_sets = {source_v}
    node_heap = init_node_heap(graph_dict, source_v)
    # Init shortest path doc
    shortest_path_dict = {}
    shortest_path_dict[source_v] = 0
    # Iterate until there no
    while node_heap and is_continue(node_heap):
        min_node, min_path = node_heap.popitem()
        shortest_path_dict[min_node] = min_path
        v_sets.add(min_node)
        node_heap = update_node_heap(graph_dict, node_heap, min_node, min_path)
    # Remove source node
    shortest_path_dict.pop(source_v)
    return shortest_path_dict

def is_continue(node_heap):
    key, val = node_heap.peekitem()
    if val == np.inf:
        return False
    else:
        return True

def init_node_heap(graph_dict, source_v):
    node_heap = heapdict()
    for node in graph_dict.keys():
        node_heap[node] = np.inf
    # Remove source vertex
    node_heap[source_v] = 0
    node_heap.popitem()
    # Update value for adacency node
    if len(graph_dict[source_v].keys()) == 0:
        return node_heap
    for target_v in graph_dict[source_v].keys():
        node_heap[target_v] = graph_dict[source_v][target_v]
    return node_heap

def update_node_heap(graph_dict, node_heap, min_v, min_path):
    if len(graph_dict[min_v].keys()) == 0:
        return node_heap
    for target_v in graph_dict[min_v].keys():
        if target_v in node_heap:
            update_weight = min_path + graph_dict[min_v][target_v]
            if update_weight < node_heap[target_v]:
                node_heap[target_v] = update_weight
    return node_heap

###########################################
############### READ FILES ################
###########################################
def read_graph(filename):
    file = open(filename,"r")
    graph_dict = defaultdict(dict)
    i = 0
    for line in file:
        i += 1
        if i != 1:
            num_list = line.split()
            num_list = [int(i) for i in num_list]
            start_node = num_list[0]
            end_node = num_list[1]
            weight = num_list[2]
            graph_dict[start_node][end_node] = weight
    file.close()
    return graph_dict

###########################################
################# GRAPH ###################
###########################################
def init_inf_graph(graph_dict):
    shortest_path_graph = {}
    for vertex in graph_dict:
        shortest_path_graph[vertex] = np.inf
    return shortest_path_graph

def addedge(graph_dict, source_node, target_node, weight):
    graph_dict[source_node][target_node] = weight
    return graph_dict

def get_parent_nodes(graph_dict, target_node):
    parent_node_list = []
    for key_node in graph_dict.keys():
        if target_node in graph_dict[key_node]:
            parent_node_list.append(key_node)
    return parent_node_list

def get_local_shortest_path(graph_dict, shortest_path_list,
                            target_vertex, parent_node_list):
    path_list = []
    for parent_node in parent_node_list:
        source_to_tmp = shortest_path_list[parent_node]
        if source_to_tmp != np.inf:
            tmp_to_target = graph_dict[parent_node][target_vertex]
            tmp_path = source_to_tmp + tmp_to_target
            path_list.append(tmp_path)
        else:
            path_list.append(np.inf)
    return min(path_list)

###########################################
############### TEST CASES ################
###########################################
# Equivalent
g2 = {1: {2:1,8:2},
      2: {1:1,3:1},
      3: {2:1,4:1},
      4: {3:1,5:1},
      5: {4:1,6:1},
      6: {5:1,7:1},
      7: {6:1,8:1},
      8: {7:1,1:2}}

g_test = {1: {2:4, 3:2},
          2: {3:3, 4:2, 5:3},
          3: {2:1, 4:4, 5:5},
          4: {},
          5: {4: -5}}

g_neg_cycle = {1: {2: -6},
               2: {3: 3},
               3: {1: 2}}

g_class = {1: {2: -2},
           2: {3: -1},
           3: {1: 4, 4: 2, 5: -3},
           4: {},
           5: {},
           6: {4: 1, 5: -4}}

g_class2 = {1: {2: 0},
            2: {3: 0},
            3: {1: 1, 4: 0, 5: 0},
            4: {},
            5: {},
            6: {4: 2, 5: 2}}
