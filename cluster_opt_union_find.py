#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:38:13 2018

Clustering Algorithm with Union Find implementation

@author: Alex Lau
"""
import pandas as pd
import numpy as np
import itertools

CLUSTER_K = 4
NODE_NUM = 500
INPUT_FILE = 'cluster.txt'

########################################
############## MAIN RUN#################
########################################
def main():
    raw_list = read_txt(INPUT_FILE)
    sorted_list = sort_tuple_list(raw_list)

    root_list, rank_list = union_init(NODE_NUM)

    cluster_cnt = count_cluster(root_list)
    while cluster_cnt != CLUSTER_K:
        min_tuple = sorted_list.pop()
        min_u = min_tuple[0]
        min_v = min_tuple[1]
        union_merge(min_u, min_v, root_list, rank_list)
        cluster_cnt = count_cluster(root_list)

    tmp_tuple = sorted_list.pop()
    u = tmp_tuple[0]
    v = tmp_tuple[1]
    root_u = union_find(u, root_list, rank_list)
    root_v = union_find(v, root_list, rank_list)
    while root_u == root_v:
        tmp_tuple = sorted_list.pop()
        u = tmp_tuple[0]
        v = tmp_tuple[1]
        root_u = union_find(u, root_list, rank_list)
        root_v = union_find(v, root_list, rank_list)

    max_distance = tmp_tuple[2]
    print('Max. distance is {}'.format(max_distance))
    pass

########################################
############# UNION FIND ###############
########################################
# n is the size of list
def union_init(n):
    root_list = []
    for i in range(n):
        root_list.append(i)
    rank_list = [0] * n
    return root_list, rank_list

def union_find(ind, root_list, rank_list):
    if ind != root_list[ind]:
        root_list[ind] = union_find(root_list[ind], root_list, rank_list)
    return root_list[ind]

def union_merge(ind1, ind2, root_list, rank_list):
    u = union_find(ind1, root_list, rank_list)
    v = union_find(ind2, root_list, rank_list)
    if u == v:
        return False
    elif rank_list[u] == rank_list[v]:
        rank_list[v] += 1
        root_list[u] = v
    elif rank_list[u] < rank_list[v]:
        root_list[u] = v
    else:
        root_list[v] = u
    return True

########################################
############# CLUSTERING ###############
########################################
# Count the number of cluster
def count_cluster(root_list):
    cluster_root_set = set()
    for sub_root in root_list:
        while sub_root != root_list[sub_root]:
            sub_root = root_list[sub_root]
        ult_root = sub_root
        cluster_root_set.add(ult_root)
    cluster_cnt = len(cluster_root_set)
    return cluster_cnt

########################################
############ PROCESS DATA ##############
########################################
def read_txt(filename, end_pt = -1):
    file = open(filename,"r")
    output_list = []
    i = 0
    for line in file:
        i+=1
        if i == 1:
            continue
        if i == end_pt:
            break
        else:
            tuple_info = line.split()
            tuple_info = [int(i) for i in tuple_info]
            # Decrease node key by 1
            tuple_info[0] -= 1
            tuple_info[1] -= 1
            tuple_info = tuple(tuple_info)
            #clean_line = line
            output_list.append(tuple_info)
    file.close()
    return output_list

def sort_tuple_list(tuple_list):
    # Sort from max to min
    sorted_list = sorted(tuple_list,
                         key=lambda tup: tup[2],
                         reverse = True)
    return sorted_list
