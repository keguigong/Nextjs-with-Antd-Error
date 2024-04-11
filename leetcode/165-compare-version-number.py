# 65. 比较版本号
# https://leetcode.cn/problems/compare-version-numbers


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            num1, num2 = 0, 0
            while p1 < m and version1[p1] != ".":
                num1 = num1 * 10 + ord(version1[p1]) - ord("0")
                p1 += 1

            while p2 < n and version2[p2] != ".":
                num2 = num2 * 10 + ord(version2[p2]) - ord("0")
                p2 += 1

            if p1 < m and version1[p1] == ".":
                p1 += 1
            if p2 < n and version2[p2] == ".":
                p2 += 1

            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

        return 0
