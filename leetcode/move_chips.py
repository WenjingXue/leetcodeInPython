# 1217. Minimum Cost to Move Chips to The Same Position
# Either move odd to even, or move even to odd. Choose the less cost one.
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for p in position:
            if p%2:
                odd = odd + 1
            else:
                even = even + 1
        return min(odd, even)
