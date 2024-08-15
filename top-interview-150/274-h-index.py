# 274. H 指数
# https://leetcode.cn/problems/h-index

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        hIndex = 1
        for index, cite in enumerate(citations):
            if cite >= hIndex and index + 1 >= hIndex:
                hIndex += 1
            else:
                return hIndex - 1
        return hIndex - 1