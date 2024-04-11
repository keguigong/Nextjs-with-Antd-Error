/**
 * 三数之和
 * https://leetcode.cn/problems/3sum/
 */

// 双指针
function threeSum(nums: number[]): number[][] {
  let ans = [];
  const len = nums.length;
  if (nums == null || len < 3) return ans;
  nums.sort((a, b) => a - b);

  for (let i = 0; i < len; i++) {
    if (nums[i] > 0) break;
    if (i > 0 && nums[i] == nums[i - 1]) continue;
    let left = i + 1;
    let right = len - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum == 0) {
        ans.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] == nums[left + 1]) left++;
        while (left < right && nums[right] == nums[right - 1]) right--;
        left++;
        right--;
      } else if (sum < 0) left++;
      else if (sum > 0) right--;
    }
  }
  return ans;
}

export let nums = [-1, 0, 1, 2, -1, -4];
console.log(threeSum(nums));

// 暴力解法
function threeSum1(nums: number[]): number[][] {
  let tempList: number[][] = [];

  function pick3Nums(nums: number[], index: number, pickedNums: number[]) {
    if (pickedNums.length === 3) {
      if (pickedNums.reduce((prev, curr) => prev + curr) === 0) {
        tempList.push(pickedNums);
      }
    } else if (index < nums.length) {
      pick3Nums(nums, index + 1, [...pickedNums, nums[index]]);
      pick3Nums(nums, index + 1, pickedNums);
    }
  }

  pick3Nums(nums, 0, []);

  let set = new Set<string>();
  tempList.forEach((element) =>
    set.add(element.sort((a, b) => a - b).join(","))
  );
  let numsList: number[][] = [];
  set.forEach((value) =>
    numsList.push(value.split(",").map((element) => parseInt(element)))
  );
  return numsList;
}
