# 763. 划分字母区间
# https://leetcode.cn/problems/partition-labels

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lookup = dict()
        for i in range(n):
            if s[i] not in lookup:
                lookup[s[i]] = [i, i]
            else:
                lookup[s[i]][1] = i

        intervals = list(lookup.values())
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return [(lambda x: x[1] - x[0] + 1)(x) for x in merged]


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
