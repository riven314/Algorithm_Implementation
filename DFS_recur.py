"""

Depth First Search - Recursive Approach

"""

from collections import defaultdict

#Below DFS algorithm assumes that all the nodes from a given graph are reachable
#For sinking node, a self cycle needs to be constructed
#to avoid list index out of range
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS_helper(self,s,visited):
        if visited[s]==False:
            visited[s]=True
            print(s)
        for i in self.graph[s]:
            if visited[i]==False:
                self.DFS_helper(i,visited)
    def DFS(self):
        visited = [False]*len(self.graph)
        for i in range(len(self.graph)):
            self.DFS_helper(i,visited)

g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.addEdge(4,6)
g.addEdge(6,5)
g.addEdge(6,7)
g.addEdge(6,8)
g.addEdge(5,8)
g.addEdge(7,8)
g.addEdge(8,8)
g.DFS()
