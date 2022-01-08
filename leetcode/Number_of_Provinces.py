class UnionFind:
    def __init__(self, size:int):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.n_province = size
        
    def find(self, i:int) -> int:
        if self.root[i] == i: return i
        self.root[i] = self.find(self.root[i])
        return self.root[i]
    
    def union(self, i:int, j:int):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j: return
        self.n_province -=1
        if self.rank[root_i] > self.rank[root_j]:
            self.root[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.root[root_i] = root_j
        else:
            self.root[root_j] = root_i
            self.rank[root_i] +=1
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    uf.union(i,j)
        return uf.n_province
                
