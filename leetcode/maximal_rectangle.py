class Solution:
    # Treat each row as a histogram and use help function to find the maximum.
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        res = 0
        m = len(matrix[0])
        accu = [0] * m
        for row in matrix:
            for column in range(m):
                if row[column] == "1":
                    accu[column] += 1
                else:
                    accu[column] = 0
            res = max(res, self.maximalRectangle_1D(accu))
        return res
        
    # Help function to calculate maximal rectangle on a histogram (1D Array).
    # Find the rectangle on each index and then compare them to find the maximum.
    # Use stack so we only need to visit once on each point, O(N).
    def maximalRectangle_1D(self, arr:List[str])->int:
        res = 0
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                pos_peak = stack.pop()
                if stack:
                    res = max(res,arr[pos_peak]*(i-stack[-1]-1))
                else:
                    res = max(res,arr[pos_peak]*i)
            stack.append(i)
        stack = [-1] + stack
        for i in range(1,len(stack)):
            res = max(res,arr[stack[i]]*(stack[-1] - stack[i-1]))
        return res
