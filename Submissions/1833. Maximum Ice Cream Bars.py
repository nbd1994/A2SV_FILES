class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cnt = 0
        tot = 0
        for cost in costs:
            tot+=cost
            if tot <= coins:
                cnt+=1
        return cnt