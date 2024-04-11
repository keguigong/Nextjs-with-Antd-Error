# 在排序数组中查找元素的第一个和最后一个位置
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


def searchLeft(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def searchRight(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] > target:
                return mid
            else:
                left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = searchLeft(nums, target), searchRight(nums, target)
        return [left, right]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution().searchRange(nums, target))
