class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[i] <= prices[j]:
                    profit = prices[j] - prices[i]
                    res = max(profit,res)

        return res