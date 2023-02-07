/**
 * 整数反转
 * https://leetcode.cn/problems/reverse-integer/
 */

function reverse(x: number): number {
  let num = 0;
  let x1 = Math.abs(x);
  while (x1 !== 0) {
    num = num * 10 + (x1 % 10);
    x1 = Math.floor(x1 / 10);
    if (num < -Math.pow(2, 31) || num > Math.pow(2, 31) - 1) return 0;
  }
  return x > 0 ? num : -num;
}

export let input = -123;
// let input = 1534236469;
console.log(reverse(input));
