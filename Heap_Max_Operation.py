# Create a heap tree with maximum as root
class Heap_Max:
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
        if self.heaptree[child]>self.heaptree[parent]:
            self.heaptree[child],self.heaptree[parent]=self.heaptree[parent],self.heaptree[child]
    def Del_Max(self):
        k = self.heaptree[0]
        last = self.heaptree.pop()
        self.size = len(self.heaptree)
        if not self.size == 0:
            index = 0
            # Error1: List out of range when list size = 1
            self.heaptree[index] = last
            while 2*index+1 <= self.size-1:
                max_index = self.Max_Index(index)
                # Error2: List out of range becoz line 26 size not -1v
                if self.heaptree[max_index]>self.heaptree[index]:
                    self.heaptree[max_index],self.heaptree[index]=self.heaptree[index],self.heaptree[max_index]
                index = max_index
        return k
    def Max_Index(self,i):
        if self.size<=2*i+2:
            return 2*i+1
        elif self.heaptree[2*i+1]>=self.heaptree[2*i+2]:
            return 2*i+1
        else:
            return 2*i+2
    def Print_Max(self):
        return self.heaptree[0]
