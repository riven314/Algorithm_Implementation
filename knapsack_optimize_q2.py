#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:11:56 2018

Dynamic programming on Knapsack problem with space optimisation

@author: Alex Lau
"""
import pandas as pd
import numpy as np
from collections import defaultdict
import sys

# [value_n], [weight_n]
INPUT_FILE = 'knapsack_big.txt'

sys.setrecursionlimit(4000)
info_dict, tuple_list = read_txt(INPUT_FILE)
# Outer = item, Inner = weight
memo_dict = defaultdict(dict)
opt_sol = helper_recurse(2000, 2000000, memo_dict, tuple_list)

########################################
######## HELPER FOR KNAPSACK ###########
########################################
def helper_recurse(item, weight, memo_dict, tuple_list):
    # if value exist in hash table, lookup it
    if in_memo_dict(item, weight, memo_dict):
        return memo_dict[item][weight]
    # if item <= 0, return 0
    if item < 1:
        return 0

    # Fill in hash table
    add_weight = tuple_list[item - 1][1]
    add_value = tuple_list[item - 1][0]
    # If item to be added has weight exceeding capacity, inherenet the previous solution
    if weight < add_weight:
        memo_dict[item][weight] = helper_recurse(item - 1, weight, memo_dict, tuple_list)
        return memo_dict[item][weight]
    # Else, compare the two solution
    else:
        memo_dict[item][weight] = max(helper_recurse(item - 1, weight, memo_dict, tuple_list),\
                                      helper_recurse(item - 1, weight - add_weight, memo_dict, tuple_list) + add_value)
        return memo_dict[item][weight]


def in_memo_dict(item, weight, memo_dict):
    if item in memo_dict:
        if weight in memo_dict[item]:
            return True
        else:
            return False
    else:
        return False

########################################
############ PROCESS DATA ##############
########################################
def read_txt(filename, end_pt = -1):
    file = open(filename,"r")
    info_dict = {}
    output_list = []
    i = 0
    for line in file:
        i+=1
        if i == 1:
            tuple_info = line.split()
            tuple_info = [int(i) for i in tuple_info]
            info_dict['weight'] = tuple_info[0]
            info_dict['items'] = tuple_info[1]
            continue
        if i == end_pt:
            break
        else:
            tuple_info = line.split()
            tuple_info = [int(i) for i in tuple_info]
            tuple_info = tuple(tuple_info)
            #clean_line = line
            output_list.append(tuple_info)
    file.close()
    return info_dict, output_list
