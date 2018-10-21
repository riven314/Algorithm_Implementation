#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:57:41 2018

Optimal Binary Search Tree Algorithm (Dynamic Programming)

@author: Alex Lau
"""
import numpy as np
import pandas as pd


frq_list = [0.05, 0.4, 0.08, 0.04, 0.1, 0.1, 0.23]

def init_table(frq_list):
    n = len(frq_list)
    # Remember to use double!!! not integer!!
    opt_table = np.zeros((n,n), dtype = np.double)
    return opt_table


def get_subopt(start, end, opt_table, frq_list):
    if start == end:
        return frq_list[start]
    elif start > end:
        return 0
    else:
        # both end point and start point inclusive
        subopt_const = sum(frq_list[start : end + 1])
        subopt_list = []
        for r in range(start, end + 1):
            subopt_left = get_subopt(start, r - 1, opt_table, frq_list)
            subopt_right = get_subopt(r + 1, end, opt_table, frq_list)
            tmp_subopt = subopt_const + subopt_left + subopt_right
            subopt_list.append(tmp_subopt)
        subopt_val = min(subopt_list)
        opt_table[start, end] = subopt_val
        return subopt_val

def bst_opt_val(frq_list):
    n = len(frq_list)
    opt_table = init_table(frq_list)
    for s in range(n):
        for i in range(n):
            print('s = {}, i = {}'.format(s, i))
            if i + s >= n:
                print('Out of index')
                pass
            else:
                opt_table[i, i +s] = get_subopt(i, i + s, opt_table, frq_list)
    opt_val = opt_table[0, n-1]
    print('Optimal Expected Weight = {}'.format(opt_val))
    return opt_val
