# 131. 分割回文串
# https://leetcode.cn/problems/palindrome-partitioning

from typing import List


class Solution:
    def __init__(self):
        self.ans: List[List[str]] = []

    def partition(self, s: str) -> List[List[str]]:
        def helper(begin: int, substr: List[str]):
            n = len(s)
            # print("begin = {}, substr = {}".format(begin, substr))

            if not begin < n:
                self.ans.append(substr)
            else:
                for i in range(begin, n):
                    if i == begin:
                        right = i
                        while right < n and s[right] == s[begin]:
                            temp = substr[:]
                            temp.append(
                                s[begin : right + 1] if right + 1 < n else s[begin:]
                            )
                            helper(right + 1, temp)
                            right += 1
                    else:
                        left, right = i, i

                        while right + 1 < n and s[right + 1] == s[right]:
                            right += 1

                        while (
                            left - 1 >= begin
                            and right + 1 < n
                            and s[right + 1] == s[left - 1]
                        ):
                            right += 1
                            left -= 1

                        if left == begin:
                            temp = substr[:]
                            temp.append(
                                s[begin : right + 1] if right + 1 < n else s[begin:]
                            )
                            helper(right + 1, temp)

        helper(0, [])
        return self.ans
