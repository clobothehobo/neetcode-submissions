class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        p = 0
        while p<len(prices)-1:
            i = p+1
            while i<len(prices):
                if prices[i]-prices[p]>profit:
                    profit = prices[i]-prices[p]
                i+=1
            p+=1
        return profit
            