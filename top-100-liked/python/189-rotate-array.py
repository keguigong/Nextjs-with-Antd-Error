# 189.旋转数组
# https://leetcode.cn/problems/rotate-array/
from typing import List


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

        # Complexity: O(n)
        # if not nums:
        #     return
        # k %= len(nums)
        # for i in range(k):
        #     temp = nums.pop()
        #     nums.insert(0, temp)


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
solution.rotate(nums, k)
print(nums)
