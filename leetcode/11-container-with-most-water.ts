/**
 * 盛最多水的容器
 * https://leetcode.cn/problems/container-with-most-water/
 */

function maxArea(height: number[]): number {
  let left = 0;
  let right = height.length - 1;
  let area = 0;
  while (left < right) {
    area = Math.max(area, (right - left) * Math.min(height[left], height[right]));
    if (height[left] <= height[right]) {
      left++;
    } else {
      right--;
    }
  }
  return area
}
