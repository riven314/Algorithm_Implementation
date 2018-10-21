#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:02:49 2018

Haffman Algorithm Implementation (Greedy Algorithm)

@author: Alex Lau
"""
from heapq import heappush, heappop

INPUT_FILE = 'huffman.txt'


########################################
############ HUFFMAN ALGO ##############
########################################
def main():
    h = read_txt(INPUT_FILE)
    alpha_dict = {tup[1]: 0 for tup in h}
    while len(h) != 1:
        a_tup = heappop(h)
        b_tup = heappop(h)
        # Get merge frequency
        a_frq = a_tup[0]
        b_frq = b_tup[0]
        merge_frq = a_frq + b_frq
        # Get merge name
        a_node = a_tup[1]
        b_node = b_tup[1]
        merge_node = merge_alpha(a_node, b_node)
        # Increment length of merging alphabet
        merge_list = merge_node.split(',')
        for node in merge_list:
            alpha_dict[node] += 1
        # Insert the merge node in heap
        merge_tup = (merge_frq, merge_node)
        heappush(h, merge_tup)
    # Retrieve the encoding info (e.g length)
    max_val = dict_max(alpha_dict)
    min_val = dict_min(alpha_dict)
    print('Max encoding = {}\nMin encoding = {}\n'.format(max_val, min_val))
    return alpha_dict

########################################
############ DICT MAX/ MIN #############
########################################
def dict_max(alpha_dict):
    max_tup = max(alpha_dict.items(), key = lambda x: x[1])
    return max_tup[1]

def dict_min(alpha_dict):
    min_tup = min(alpha_dict.items(), key = lambda x: x[1])
    return min_tup[1]

########################################
############ STRING MATCH ##############
########################################
# ERROR: ONE NODE HAS NAME MORE THAN ONE CHARACTER
def encode_len(merge_str):
    alpha_dict = {}
    cnt = 0
    for i in merge_str:
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
        else:
            alpha_dict[i] = cnt
    return alpha_dict

def merge_alpha(a_str, b_str):
    merge_str = a_str + ',' + b_str
    return merge_str

########################################
############ PROCESS DATA ##############
########################################
def read_txt(filename, end_pt = -1):
    file = open(filename,"r")
    h = []
    ind = -1
    for line in file:
        ind += 1
        if ind == 0:
            continue
        elif ind == end_pt:
            break
        else:
           tmp = int(line)
           tmp_tup = (tmp, str(ind))
           heappush(h, tmp_tup)
    file.close()
    return h

# heappop(h),
