#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:02:17 2018

Scheduling Algorithm (Greedy Algorithm)

@author: Alex Lau
"""
# Function for reading text file
import pandas as pd


def txt_to_lists(filename):
    file = open(filename,"r")
    weight_list = []
    length_list = []
    i = 0
    for line in file:
        i+=1
        if i == 1:
            pass
        else:
            num_list = line.split()
            num_list = [int(i) for i in num_list]
            weight_list.append(num_list[0])
            length_list.append(num_list[1])
    file.close()
    return weight_list, length_list

# Functions for Sorting
def Sort_By_Difference(w_list, l_list):
    df = pd.DataFrame({'weight': w_list,
                       'length': l_list})
    df['difference'] = df['weight'] - df['length']
    df.sort_values(by = ['difference', 'weight'],
                   ascending = False,
                   inplace = True)
    w_list = df.weight.tolist()
    l_list = df.length.tolist()
    return w_list, l_list

def Sort_By_Ratio(w_list, l_list):
    df = pd.DataFrame({'weight': w_list,
                       'length': l_list})
    df['ratio'] = df['weight'] / df['length']
    df.sort_values(by = ['ratio', 'weight'],
                   ascending = False,
                   inplace = True)
    sorted_w_list = df.weight.tolist()
    sorted_l_list = df.length.tolist()
    return sorted_w_list, sorted_l_list

def Get_Metrics(sorted_w_list, sorted_l_list):
    weighted_complete_time = 0
    complete_time = 0
    for weight, length in zip(sorted_w_list, sorted_l_list):
        complete_time += length
        weighted_complete_time += complete_time * weight
    print('Resultant Weighted Completion Time:\n', weighted_complete_time)
    return weighted_complete_time

if __name__ == '__main__':
    w_list, l_list = txt_to_lists('jobs.txt')
    # Sort By Difference
    sorted_w_list, sorted_l_list = Sort_By_Difference(w_list, l_list)
    ans_diff = Get_Metrics(sorted_w_list, sorted_l_list)
    print('Weighted Completion by Difference:\n', ans_diff)

    # Sort By Ratio
    sorted_w_list, sorted_l_list = Sort_By_Ratio(w_list, l_list)
    ans_ratio = Get_Metrics(sorted_w_list, sorted_l_list)
    print('Weighted Compeltion by Ratio:\n', ans_ratio)
