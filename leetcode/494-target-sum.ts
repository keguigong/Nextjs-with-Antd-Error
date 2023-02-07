/**
 * 目标和
 * https://leetcode.cn/problems/target-sum/
 */

function findTargetSumWays(nums: number[], target: number): number {
  let len = nums.length;
  let count = 0;
  let exprList = [];

  function calcSum(
    nums: number[],
    index: number,
    sum: number,
    expr = ""
  ) {
    if (index >= len) {
      if (sum === target) {
        count += 1;
        exprList.push(expr + `=${target}`);
      }
    } else {
      let _expr: string;
      _expr = expr + "+" + nums[index];
      calcSum(nums, index + 1, sum + nums[index], _expr);
      _expr = expr + "-" + nums[index];
      calcSum(nums, index + 1, sum - nums[index], _expr);
    }
  }
  calcSum(nums, 0, 0);
  console.log(exprList.join("\n"));
  return count;
}

export let nums = [1, 1, 1, 1, 1];
let target = 3;
findTargetSumWays(nums, target);
