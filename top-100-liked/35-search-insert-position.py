# 35. 搜索插入位置
# https://leetcode.cn/problems/search-insert-position

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        def searchHalf(start: int, end: int) -> int:
            n = end - start + 1
            if n > 1:
                half = start + n // 2
                print("start = {}, end = {}, half = {}".format(start, end, half))
                if nums[half] > target:
                    return searchHalf(start, max(half - 1, start))
                elif nums[half] < target:
                    return searchHalf(min(half + 1, end), end)
                else:
                    # print('half = {}'.format(half))
                    return half
            else:
                # print('start = {}, end = {}'.format(start, end))
                if nums[start] > target:
                    return start
                elif nums[start] < target:
                    return end + 1
                else:
                    return start

        return searchHalf(0, length - 1)
