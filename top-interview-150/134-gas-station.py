# 134. 加油站
# https://leetcode.cn/problems/gas-station
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0
        while start < n:
            avail_gas = 0
            for i in range(n):
                j = start + i if start + i < n else start + i - n
                avail_gas += gas[j] - cost[j]
                if avail_gas < 0:
                    start += i + 1
                    break
            else:
                return start
        return -1
