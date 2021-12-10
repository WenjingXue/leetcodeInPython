#### Strategy: use heap to grab the largest k elements, the time complexity is O(n*log(k)). In this process, we can also get the maximum odd and maximum even numbers beyond the k elements (max_odd and max_even).
#### Then we go through the k elements in the heap to calculate the sum and find the minimum even and odd numbers (min_even and min_odd). The time complexity is O(k)
#### if the sum is even, then we can return the result. 
#### if the sum is odd, then we choose the bigger result between the following two cases:
#### case 1: max_even and min_odd exist, then result = sum - min_odd + max_even
#### case 2: max_odd and min_even exist, then result = sum - min_even + max_odd
#### if neither of the two cases exists, then return -1. This comparison process costs O(1) time complexity
#### The final time complexity is O(n*log(k)) + O(k) + O(1) = O(n*log(k))

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        import heapq
        
        # generate the heapq structure of the largest k elements
        # extract the maximum odd and even numbers outside of the k elements during the fitering process
        set_k = nums[0:k].copy()
        heapq.heapify(set_k)
        max_odd = -1; max_even = -2
        for i in range(k,len(nums),1):
            if nums[i] > set_k[0]:
                num_new = heapq.heapreplace(set_k,nums[i])
                if num_new%2 == 0: max_even = num_new
                else: max_odd = num_new
            else:
                if nums[i]%2 == 0: max_even = max(max_even,nums[i])
                else: max_odd = max(max_odd,nums[i])
        
        # go through the k elements in the heap structure, get the sum and extract the minimum odd and even number
        res = 0; min_odd = sys.maxsize; min_even = sys.maxsize
        for num in set_k:
            res +=num
            if num%2 == 0: min_even = min(num,min_even)
            else: min_odd = min(num,min_odd)
        
        # if the sum is even, return sum. Or else, switch the min_odd with max_even, and switch min_even with max_odd if possible. use the larger result.
        if res%2==0: return res
        else:
            res_f = -1
            if max_even>=0 and min_odd<sys.maxsize:
                res_f = max(res_f, res-min_odd+max_even)
            if max_odd >=0 and min_even<sys.maxsize:
                res_f = max(res_f, res-min_even+max_odd)
            return res_f
