"""
42. 接雨水
https://leetcode.cn/problems/trapping-rain-water/description/
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        area, left_max, right_max = 0, 0, 0

        for p_index, p_height in enumerate(height):
            # print("#{}, height = {}".format(p_index, p_height))

            if p_height > left_max:
                left_max = p_height
                # print("left_max = {}".format(left_max))
                continue

            right_index = length - 1
            if p_index == right_index:
                break

            lower_height = 0
            right_max = 0
            while right_index > p_index:
                # print("right_index = {}".format(right_index))
                if height[right_index] >= left_max:
                    lower_height = left_max
                    # print("lower_height = left_max = {}".format(lower_height))
                    break
                elif height[right_index] > right_max:
                    right_max = height[right_index]
                right_index -= 1
            else:
                lower_height = right_max
                # print("lower_height = right_max = {}".format(lower_height))

            if lower_height > p_height:
                area += lower_height - p_height
            # print("area = {}".format(area))

            # if p_index > 0 and p_index < length - 1:
            #     # print(h_index, h)
            #     left_max, right_max = (
            #         max(height[:p_index]),
            #         max(height[p_index + 1 : length]),
            #     )
            #     min_height = min(left_max, right_max)
            #     if min_height > p_height:
            #         area += min_height - p_height

        return area

    def trap1(self, height: List[int]) -> int:
        """
        参考：接雨水：双指针解法说明【清晰易懂】
        https://leetcode.cn/problems/trapping-rain-water/solutions/2597032/jie-yu-shui-shuang-zhi-zhen-jie-fa-shuo-4f1f3/?envType=study-plan-v2&envId=top-100-liked
        """
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        volumn = 0
        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if leftMax < rightMax:
                volumn += leftMax - height[left]
                left += 1
            else:
                volumn += rightMax - height[right]
                right -= 1
        return volumn


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [0, 7, 1, 4, 6]

print(Solution().trap(height))
