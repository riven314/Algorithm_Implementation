#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 00:05:41 2018

Weighted Independent Set (Dynamic Programming)

@author: Alex Lau
"""
INPUT_FILE = 'mwis.txt'


# ANS: 01100110

def main():
    weight_list = read_txt(INPUT_FILE)
    #weight_list = [2, 9, 2, 9, 2, 9, 2, 9, 2, 9]
    #weight_list = [9, 2, 9, 2, 9, 2, 9, 2, 9, 2]
    #weight_list = [460, 250, 730, 63, 379, 638, 122, 435, 705, 84]
    optimal_list = get_memorize(weight_list)
    wis_set = get_wis_set(optimal_list, weight_list)

    test_set = [1, 2, 3, 4, 17, 117, 517, 997]
    test_set = set([i-1 for i in test_set])
    ans_dict = {}
    for test_node in test_set:
        if test_node in wis_set:
            ans_dict[test_node] = 1
        else:
            ans_dict[test_node] = 0
    return ans_dict

########################################
############  DYNAMIC PRG ##############
########################################
def get_memorize(weight_list):
    optimal_list = [0] * len(weight_list)
    for i in range(len(weight_list)):
        if i == 0:
            optimal_list[i] = weight_list[0]
        elif i == 1:
            optimal_list[i] = max(weight_list[0], weight_list[1])
        else:
            option_1 = optimal_list[i-1]
            option_2 = weight_list[i] + optimal_list[i-2]
            optimal_list[i] = max(option_1, option_2)
    return optimal_list

def get_wis_set(optimal_list, weight_list):
    wis_set = set()
    i = len(optimal_list) - 1
    while i > 1:
        option_1 = optimal_list[i-1]
        option_2 = optimal_list[i-2] + weight_list[i]
        if option_1 > option_2:
            i -= 1
        elif option_2 > option_1:
            wis_set.add(i)
            i -= 2
        elif option_1 == option_2:
            print('Equality Exist!!')
            i -= 1
    if i == 1:
        if weight_list[0] > weight_list[1]:
            wis_set.add(0)
        else:
            wis_set.add(1)
    elif i == 0:
        wis_set.add(0)
    return wis_set

########################################
############ PROCESS DATA ##############
########################################
def read_txt(filename, end_pt = -1):
    file = open(filename,"r")
    weight_list = []
    ind = -1
    for line in file:
        ind += 1
        if ind == 0:
            continue
        elif ind == end_pt:
            break
        else:
           tmp = int(line)
           weight_list.append(tmp)
    file.close()
    return weight_list
