/**
 * 删除有序数组中的重复项
 * https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
 */

function removeDuplicates(nums: number[]): number {
  let left = 0;
  const len = nums.length;

  for (let right = 1; right < len; right++) {
    if (nums[right] != nums[left]) {
      nums[left + 1] = nums[right];
      left++;
    }
  }
  return left + 1;
}

export let nums = [1, 1, 2];
console.log(removeDuplicates(nums));

// 简单做法
function removeDuplicates1(nums: number[]): number {
  let index = 0;
  while (index < nums.length) {
    while (index + 1 < nums.length && nums[index] === nums[index + 1]) {
      nums.splice(index, 1);
    }
    index++;
  }
  return nums.length;
}
