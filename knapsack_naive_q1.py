#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:11:37 2018

Dynamic programming on Knapsack problem with naive approach

@author: Alex Lau
"""
import pandas as pd
import numpy as np

INPUT_FILE = 'knapsack1.txt'

# [value_n], [weight_n]
info_dict, tuple_list = read_txt(INPUT_FILE)
opt_table = init_table(info_dict)
opt_table = fill_table(opt_table, tuple_list)

########################################
######## HELPER FOR KNAPSACK ###########
########################################
def init_table(info_dict):
    # nrow = weight increment
    nrow = info_dict['weight']
    # ncol = no. of items
    ncol = info_dict['items']
    # create narray
    opt_table = np.zeros((nrow, ncol), dtype = np.int32)
    return opt_table

def fill_table(opt_table, tuple_list):
    nrow, ncol = opt_table.shape
    for  item in range(ncol):
        for weight in range(nrow):
            add_value = tuple_list[item][0]
            add_weight = tuple_list[item][1]
            # Comparing two option: add item i or not
            inherent_sol = get_info(item - 1, weight, opt_table)
            if weight - add_weight < 0:
                # If item i has weight exceeding existing capacity, discard it
                opt_sol = inherent_sol
            else:
                add_sol =  get_info(item - 1, weight - add_weight, opt_table) + add_value
                opt_sol = max(inherent_sol, add_sol)
            # Fill in the table
            opt_table[weight][item] = opt_sol
    return opt_table

def get_info(i, w, table):
    if i < 0:
        return 0
    else:
        return table[w][i]

def get_opt_sol(opt_table):
    pass

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
