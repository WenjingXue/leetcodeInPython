## We can sort the list and store in another temp list. 
## We use dictionary to store the counts and later use it to create result. 
## Time: O(n log n) bcoz of sort. Space: O(n) bcoz of dictionary.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = sorted(nums.copy())
        dic = {}
        for i,num in enumerate(nums1):
            if num not in dic:
                dic[num] = i
        return [dic[num] for num in nums]
