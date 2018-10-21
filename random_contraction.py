from graph_class_v2 import vertex
from graph_class_v2 import graph

def merge_edge(a,b):
    new_vertex = vertex((a.id,b.id))
    gp_list = {}
    for i in a.connect:
        if i in b.connect:
            gp_list[i] = a.connect[i]+b.connect[i]
        else:
            gp_list[i] = a.connect[i]
    for j in b.connect:
        if j not in a.connect:
            gp_list[j] = b.connect[j]
    gp_list.pop(a.id,None)
    gp_list.pop(b.id,None)
    new_vertex.connect = gp_list
    return new_vertex

def contraction(old_graph,first,second):
    new_graph = graph()
    ver1 = old_graph.getvertex(first)
    ver2 = old_graph.getvertex(second)
    merge_ver = merge_edge(ver1,ver2)
    for dummy in old_graph:
        ver = old_graph.getvertex(dummy)
        if ver.id != ver1.id and ver.id != ver2.id:
            temp_ver = vertex(ver.id)
            for x in ver:
                if x in merge_ver.id:
                    temp_ver.connect[merge_ver.id] = merge_ver.connect[ver.id]
                else:
                    temp_ver.connect[x] = ver.connect[x]
            new_graph.addvertex(temp_ver)
            del temp_ver
        del ver
    new_graph.addvertex(merge_ver)
    return new_graph

import random
def random_contraction(orig_graph):
    if len(orig_graph.nodeList)<=2:
        return orig_graph
    rand1 = random.choice(list(orig_graph.nodeList))
    rand2 = random.choice(list(orig_graph.nodeList[rand1]))
    con_graph = contraction(orig_graph,rand1,rand2)
    return random_contraction(con_graph)

def opt_rand(orig_graph):
    n = len(orig_graph.nodeList)
    min_cut_list = []
    for k in range(1,n**2):
        temp_graph = random_contraction(orig_graph)
        sub_dict = list(temp_graph.nodeList.values())[0]
        min_cut = list(sub_dict.values())[0]
        min_cut_list.append(min_cut)
        del temp_graph
        del min_cut
    return min_cut_list

# Testing with different cases
'a = {"a":3,"b":4,"c":5}
'b = {"b":10,"c":7,"d":99}

#Case 1, Ans=2
ver1 = vertex(1)
ver1.connect = {2:1,3:1,4:1}
ver2 = vertex(2)
ver2.connect = {1:1,3:1}
ver3 = vertex(3)
ver3.connect = {1:1,2:1,4:1}
ver4 = vertex(4)
ver4.connect = {1:1,3:1}
g1 = graph()
for i in [ver1,ver2,ver3,ver4]:
    g1.addvertex(i)

#Case 2, Ans= 2
g2 = graph()
ver1 = vertex(1)
ver1.connect = {4:1,2:1,7:1,3:1}
ver2 = vertex(2)
ver2.connect = {4:1,1:1,3:1}
ver3 = vertex(3)
ver3.connect = {1:1,2:1,4:1}
ver4 = vertex(4)
ver4.connect = {5:1,1:1,2:1,3:1}
ver5 = vertex(5)
ver5.connect = {8:1,7:1,6:1,4:1}
ver6 = vertex(6)
ver6.connect = {8:1,5:1,7:1}
ver7 = vertex(7)
ver7.connect = {6:1,8:1,5:1,1:1}
ver8 = vertex(8)
ver8.connect = {7:1,6:1,5:1}
for i in [ver1,ver2,ver3,ver4,ver5,ver6,ver7,ver8]:
    g2.addvertex(i)

#Real Case
real_graph = graph()
file = open("graph_test_case.txt","r")
for line in file:
        num_list = line.split("\t")
        num_list.remove('\n')
        temp_vertex = vertex(num_list[0])
        if len(num_list)>1:
            temp_dict ={}
            for x in num_list[1:]:
                temp_dict[x] = 1
            temp_vertex.connect = temp_dict
            del temp_dict
        real_graph.addvertex(temp_vertex)
        del temp_vertex

file.close()
# ans = 17
