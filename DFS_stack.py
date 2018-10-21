"""

Depth First Search - Stack approach

"""


from Graph_class_v3 import Graph
#756156
# Read in data & create a reverse graph
file = open("directed_graph.txt","r")
real_graph = Graph()
for line in file:
    string_list = line.split()
    int_list = list(map(int,string_list))
    real_graph.addEdge(int_list[1],int_list[0])

file.close()

#Find the max among the keys and values
max_len = max(real_graph.graph.keys())
for i in real_graph.graph:
    int_list = real_graph.graph[i]
    if not real_graph.graph[i]==[]:
        temp_max = max(int_list)
        if temp_max > max_len:
            max_len = temp_max

#Make the graph complete, add sink node
for i in range(max_len+1):
    if i not in real_graph.graph or real_graph.graph[i]==[]:
        real_graph.graph[i]=[i]

# Run DFS
real_graph.DFS()
nodes_order = real_graph.order_list


# Create a graph in correct order
file = open("directed_graph.txt","r")
final_graph = Graph()
for line in file:
    string_list = line.split()
    int_list = list(map(int,string_list))
    final_graph.addEdge(int_list[0],int_list[1])

file.close()

#Find the max among the keys and values
max_len = max(final_graph.graph.keys())
for i in final_graph.graph:
    int_list = final_graph.graph[i]
    if not final_graph.graph[i]==[]:
        temp_max = max(int_list)
        if temp_max > max_len:
            max_len = temp_max

#Make the graph complete, add sink node
for i in range(max_len+1):
    if i not in final_graph.graph or final_graph.graph[i]==[]:
        final_graph.graph[i]=[i]

final_graph.order =  nodes_order
final_graph.Dijk_Algo()
