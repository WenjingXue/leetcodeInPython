import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        selected = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>selected[-1]: 
                selected.append(nums[i])
            else:
                j = bisect.bisect_left(selected,nums[i])
                selected[j] = nums[i]
        return len(selected)
