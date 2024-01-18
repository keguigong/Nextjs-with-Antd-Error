/**
 * 507. 完美数
 * https://leetcode.cn/problems/perfect-number/
 */

export function checkPerfectNumber(num: number): boolean {
  let sum = 0
  for (let i = 1; i < num; i++) {
    num % i === 0 ? (sum += i) : null
  }
  return sum === num
}

const num = 28
console.log(checkPerfectNumber(num))
