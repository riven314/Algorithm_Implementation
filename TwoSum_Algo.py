#TO BE FIXED:
#1. Do it in from scratch: sort algorithm, binary search & search the nearest
#2. Debug for locating the range of y (Staring from line 23)
#3. Doing it by Hash Table
import numpy as np

#READ INPUT AND CONVERT TO ARRAY
file = open("input.txt","r")
input_list = []
i = 0
for line in file:
#if i <= 1000:
    num = int(line)
    input_list.append(num)
    #i+=1

file.close()
input_array = np.array(input_list)

#SORTING THE ARRAY
input_array.sort(kind='quicksort')


1,2,3,4,5,6,7
#LOCATING THE RANGE OF Y
#-10000-x <y < 10000-x
sum_array = np.array([])
for i in input_array:
    lower_y = -10000 - i
    higher_y = 10000 - i
    lower_index = input_array.searchsorted(lower_y, side = "left")
    higher_index = input_array.searchsorted(higher_y, side = "right")
    if lower_index!=higher_index:
        y_rng_array = input_array[lower_index:higher_index+1]
        sum_array = np.append(sum_array,y_rng_array + i)

#FILTER OUT UNDESIRED ELEMENT FROM sum_array
target_array = np.array([])
for i in sum_array:
    if i>=-10000 and i<=10000:
        target_array = np.append(target_array,i)

ans = len(np.unique(target_array))
#ANS = 427 (Dinstinct value of t in [-10000,10000])
