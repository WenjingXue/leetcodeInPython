class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        from collections import deque
        direct = {}
        for i in range(len(bombs)):
            direct[i] = []
            for j in range(len(bombs)):
                if j!=i and (bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2 <= bombs[i][2]**2:
                    direct[i].append(j)
        res = 0
        total = {}
        for i in range(len(bombs)):
            total[i]= set()
            queue_i = deque()
            total[i].add(i)
            queue_i.append(i)
            while queue_i:
                cur = queue_i.pop()
                for ele in direct[cur]:
                    if ele in total[i]: continue
                    total[i].add(ele)
                    if ele in total.keys(): total[i].update(total[ele])
                    else: queue_i.append(ele)
            res = max(res,len(total[i]))
        return res
