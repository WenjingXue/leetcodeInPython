class Solution:
    def maxPower(self, s: str) -> int:
        res = 1; cur = 'Z'; count = 0
        for ele in s:
            if ele==cur:
                count +=1
            else:
                res = max(res,count)
                cur = ele
                count = 1
        return max(res,count)
      
