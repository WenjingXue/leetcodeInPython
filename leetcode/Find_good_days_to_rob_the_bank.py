## draw a graph of the number of securities. the good days will be in a basin with two sides both more than t(time) days.
## So I set two parameters: non_increasing and non_decreasing. So I updated these two parameters while iterating the list
## for security[i], if non_increasing < t:  records[i]= False. if non_decreasing < t: records[i-2] = False.
## In this way, we keep updating the qualification of each day in the list records.
## In the end, we can just attach each element in the list records to the result.
## Since we go through the security list linearly, the time complexity is O(n). The space complexity is O(n) too because we store a list of length n.

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        records = [True] * len(security)
        non_increasing = 0; non_decreasing = 0
        for i in range(1,len(security)):
            diff = security[i] - security[i-1]
            if diff > 0:
                non_increasing =0
                non_decreasing +=1
            elif diff< 0:
                non_increasing +=1
                non_decreasing = 0
            else:
                non_increasing +=1
                non_decreasing +=1
            if non_increasing < time: records[i] = False
            if non_decreasing < time and i>=time: records[i-time] = False
        res = []
        for i in range(time,len(security)-time):
            if records[i]:res.append(i)
        return res
