# 974. 和可被 K 整除的子数组
# https://leetcode.cn/problems/subarray-sums-divisible-by-k


from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict = {}
        dict[0] = 1

        preSum = 0
        count = 0
        for num in nums:
            preSum += num
            mod = preSum % k
            if mod < 0:
                mod += k
            count += dict.get(mod, 0)
            dict[mod] = dict.get(mod, 0) + 1

        return count
