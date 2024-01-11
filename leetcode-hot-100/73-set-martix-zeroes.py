# 238. 除自身以外数组的乘积
# https://leetcode.cn/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        preSum, postSum = 1, 1
        left, right = 0, n - 1
        while left < n:
            ans[left] *= preSum
            ans[right] *= postSum
            preSum *= nums[left]
            postSum *= nums[right]
            left += 1
            right -= 1

        return ans
