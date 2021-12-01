# rob[i] = max of (nums[i] + rob[i-2]) and (rob[i-1]).
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0,0]
        for i in nums:
            cur = max(res[-1], i + res[-2])
            res.append(cur)
        return res[-1]
