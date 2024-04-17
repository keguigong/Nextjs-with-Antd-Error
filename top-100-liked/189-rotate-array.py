# 189.旋转数组
# https://leetcode.cn/problems/rotate-array/
from typing import List

def swap(nums: List[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # complexity: O(1)
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)


    def rotate1(self, nums: List[int], k: int):
        n = len(nums)
        if n < 2:
            return
        for i in range(k):
            last = nums[-1]
            for j in range(n - 1, 0, -1):
                swap(nums, j, j - 1)
            nums[0] = last


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
solution.rotate(nums, k)
print(nums)
