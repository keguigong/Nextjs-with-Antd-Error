/**
 * https://leetcode.cn/problems/two-sum/
 */

function twoSum(nums: number[], target: number): number[] {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
    let calc = target - nums[i];
    if (map.has(calc)) {
      return [i, map.get(calc)];
    }
    map.set(nums[i], i);
  }
  return [];
}
