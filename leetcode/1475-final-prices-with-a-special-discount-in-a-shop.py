# 1475. 商品折扣后的最终价格
# https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        stack = [0]
        for i in range(n - 1, -1, -1):
            price = prices[i]
            while len(stack) > 1 and stack[-1] > price:
                stack.pop()
            ans[i] = price - stack[-1]
            stack.append(price)
        return ans
