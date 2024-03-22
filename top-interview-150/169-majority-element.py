# 169. 多数元素
# https://leetcode.cn/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = dict()
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1

        maxCount = 0
        elem = 0
        for key, value in lookup.items():
            if value >= maxCount:
                maxCount = value
                elem = key

        return elem
