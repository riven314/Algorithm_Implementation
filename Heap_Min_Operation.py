# Create a heap tree with minimum as root
class Heap_Min:
    def __init__(self):
        self.heaptree = []
        self.size = 0
    def Insert(self,n):
        self.heaptree.append(n)
        self.size = len(self.heaptree)
        n_index = self.size - 1
        while n_index>0:
            if n_index%2 == 0:
                parent_index = n_index//2 - 1
            else:
                parent_index = n_index//2
            self.BubbleUp(n_index,parent_index)
            n_index = parent_index
    def BubbleUp(self,child,parent):
        if self.heaptree[child]<self.heaptree[parent]:
            self.heaptree[child],self.heaptree[parent]=self.heaptree[parent],self.heaptree[child]
    def Del_Min(self):
        k = self.heaptree[0]
        last = self.heaptree.pop()
        self.size = len(self.heaptree)
        if not self.size == 0:
            index = 0
            self.heaptree[index] = last
            while 2*index+1 <= self.size-1:
                min_index = self.Min_Index(index)
                if self.heaptree[min_index]<self.heaptree[index]:
                    self.heaptree[min_index],self.heaptree[index]=self.heaptree[index],self.heaptree[min_index]
                index = min_index
        return k
    def Min_Index(self,i):
        if self.size<=2*i+2:
            return 2*i+1
        elif self.heaptree[2*i+1]<=self.heaptree[2*i+2]:
            return 2*i+1
        else:
            return 2*i+2
    def Print_Min(self):
        return self.heaptree[0]
