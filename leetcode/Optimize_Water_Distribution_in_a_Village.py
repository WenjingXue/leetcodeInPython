class UnionFind:
    def __init__(self, size:int):
        self.root = [i for i in range(size)]
        self.rank = [1] *size
    def find(self, i:int) -> int:
        if self.root[i] != i:
            self.root[i] = self.find(self.root[i])
        return self.root[i]
    def union(self, i:int, j:int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j: return False
        if self.rank[root_i]>self.rank[root_j]:
            self.root[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.root[root_i] = root_j
        else:
            self.root[root_j] = root_i
            self.rank[root_i] += 1
        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        ordered_edges = []
        for index, cost in enumerate(wells,1):
            ordered_edges.append([cost, 0, index])
        for house1, house2, cost in pipes:
            ordered_edges.append([cost,house1,house2])
        ordered_edges.sort()
        
        uf = UnionFind(n+1)
        total_cost = 0
        
        for cost, house1, house2 in ordered_edges:
            if uf.union(house1, house2):
                total_cost += cost
        return total_cost
