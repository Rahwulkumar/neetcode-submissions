class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_len = 0

        while right < len(prices):
            if prices[right] >= prices[left]:
                total_profit = prices[right] - prices[left]
                max_len = max(max_len, total_profit)
            else:
                left = right
            right += 1
        return max_len
            

            