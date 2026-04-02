class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices) - 1
        dp = [0] * days

        for i in range(days):
            # base cases i == 0
            if i == 0:
                continue
            dp[i] = max(prices[i] - prices[i - 1] + dp[i - 1], dp[i])
        
        return dp[days - 1]