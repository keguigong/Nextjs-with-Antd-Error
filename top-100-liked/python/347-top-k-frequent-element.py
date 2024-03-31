# 347. 前 K 个高频元素
# https://leetcode.cn/problems/top-k-frequent-elements

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = dict[int, int]()
        for num in nums:
            if num in lookup:
                lookup[num] += 1
            else:
                lookup[num] = 1
        items = list(lookup.items())
        items.sort(key=lambda x: x[1], reverse=True)
        n = len(lookup)
        ans: List[int] = []
        for i in range(n):
            if i < k:
                ans.append(items[i][0])
            else:
                break
        return ans
