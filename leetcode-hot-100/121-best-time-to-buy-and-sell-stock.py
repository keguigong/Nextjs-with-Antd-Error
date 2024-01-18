# 121. 买卖股票的最佳时机
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            min_price = min(min_price, prices[i - 1])
            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
