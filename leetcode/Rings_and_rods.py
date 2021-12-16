class Solution:
    def countPoints(self, rings: str) -> int:
        rec = {}
        cur, res = 0,0
        while cur <len(rings):
            if rings[cur+1] not in rec.keys():
                rec[rings[cur+1]]=set()
            rec[rings[cur+1]].add(rings[cur])
            cur += 2
        for rod in rec.keys():
            if len(rec[rod]) >=3:
                res +=1
        return res
