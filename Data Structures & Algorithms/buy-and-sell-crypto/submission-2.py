class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p,lowest = 0,prices[0]
        for num in prices:
            max_p = max(max_p, num-lowest)
            lowest = min(num,lowest)
        return max_p