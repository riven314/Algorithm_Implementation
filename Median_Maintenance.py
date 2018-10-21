from Heap_Max_Operation import Heap_Max
from Heap_Min_Operation import Heap_Min

def Median_Main(heap_max,heap_min,i,num_list):
    # Insertion
    if i <= heap_max.Print_Max():
        heap_max.Insert(i)
    elif i >= heap_min.Print_Min():
        heap_min.Insert(i)
    else:
        heap_max.Insert(i)
    #Balancing
    heaps_len = len(heap_max.heaptree) + len(heap_min.heaptree)
    if heaps_len%2 == 0:
        while len(heap_max.heaptree)!=len(heap_min.heaptree):
            if len(heap_max.heaptree)>len(heap_min.heaptree):
                trans = heap_max.Del_Max()
                heap_min.Insert(trans)
            else:
                trans = heap_min.Del_Min()
                heap_max.Insert(trans)
    #Extraction
    if heaps_len%2 == 0:
        num_list.append(heap_max.Print_Max())
    else:
        if len(heap_max.heaptree)>len(heap_min.heaptree):
            num_list.append(heap_max.Print_Max())
        else:
            num_list.append(heap_min.Print_Min())
    #return the list
    return num_list




heap_min = Heap_Min()
heap_max = Heap_Max()
median_list = []
temp_list = []
counter = 0

file = open("text.txt","r")
for line in file:
    num = int(line)
    if counter==0:
        temp_list.append(num)
        median_list.append(num)
        counter+=1
    elif counter==1:
        temp_list.append(num)
        if temp_list[0]>=temp_list[1]:
            heap_max.Insert(temp_list[1])
            heap_min.Insert(temp_list[0])
            median_list.append(temp_list[1])
        else:
            heap_max.Insert(temp_list[0])
            heap_min.Insert(temp_list[1])
            median_list.append(temp_list[0])
        counter+=1
    else:
        median_list = Median_Main(heap_max,heap_min,num,median_list)

file.close()

# Ans = 1213
# To be improved:
# 1. Function to be more generic i.e consider the case when either heap doesn't have any element
