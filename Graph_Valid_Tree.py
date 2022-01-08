class UnionFind:
    def __init__(self, size:int):
        self.root = [i for i in range(size)]
        self.rank = [1]*size
        self.count = size
    def find(self, i:int) -> int:
        if i == self.root[i]: return i
        self.root[i] = self.find(self.root[i])
        return self.root[i]
    def union(self, i:int, j:int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j: return False
        self.count -= 1
        if self.rank[root_i] > self.rank[root_j]:
            self.root[root_j] = root_i
        elif self.rank[root_j] > self.rank[root_i]:
            self.root[root_i] = root_j
        else:
            self.root[root_j] = root_i
            self.rank[root_i] += 1
        return True

            
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            if not uf.union(edge[0],edge[1]): return False
        return uf.count ==1
        
