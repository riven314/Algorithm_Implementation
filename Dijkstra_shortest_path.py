"""

Dijkstra Algorithm on Shortest Path

"""

from graph_class_v2 import vertex
from graph_class_v2 import graph

def Dijkstra_Algo(graph_class,start_vertex):
    X = [start_vertex]
    A = {}
    A[start_vertex] = 0
    while len(X) < len(graph_class.nodeList):
        counter = True
        min_len = 0
        for n in X:
            node = graph_class.getvertex(n)
            for key in node:
                if not (key in X):
                    if counter or A[n]+node.connect[key] < min_len:
                        min_len = A[n] + node.connect[key]
                        min_key = key
                        counter = False
        X.append(min_key)
        A[min_key] = min_len
        min_len = 0
        min_key = 0
    return X, A

#Case 1
ver1 = vertex(1)
ver1.connect = {2:1,8:2}
ver2 = vertex(2)
ver2.connect = {1:1,3:1}
ver3 = vertex(3)
ver3.connect = {2:1,4:1}
ver4 = vertex(4)
ver4.connect = {3:1,5:1}
ver5 = vertex(5)
ver5.connect = {4:1,6:1}
ver6 = vertex(6)
ver6.connect = {5:1,7:1}
ver7 = vertex(7)
ver7.connect = {6:1,8:1}
ver8 = vertex(8)
ver8.connect = {7:1,1:2}
g1 = graph()
for i in [ver1,ver2,ver3,ver4,ver5,ver6,ver7,ver8]:
    g1.addvertex(i)

# real casesreal_graph = graph()
file = open("Dijkstra_Text.txt","r")
real_graph = graph()
for line in file:
        num_list = line.split("\t")
        num_list.remove('\n')
        temp_vertex = vertex(int(num_list[0]))
        if len(num_list)>1:
            temp_dict ={}
            for x in num_list[1:]:
                temp = x.split(",")
                temp_dict[int(temp[0])] = int(temp[1])
            temp_vertex.connect = temp_dict
            del temp_dict
        real_graph.addvertex(temp_vertex)
        del temp_vertex

file.close()

x, y = Dijkstra_Algo(real_graph,1)
ind_list = [7,37,59,82,99,115,133,165,188,197]

ans_list = []
for i in ind_list:
    ans_list.append(y[i])
