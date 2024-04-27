# 135. 分发糖果
# https://leetcode.cn/problems/candy
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ret = 1
        inc, dec, pre = 1, 0, 1

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                dec = 0
                pre = 1 if ratings[i] == ratings[i - 1] else pre + 1
                ret += pre
                inc = pre
            else:
                dec += 1
                if dec == inc:
                    dec += 1
                ret += dec
                pre = 1

        return ret
