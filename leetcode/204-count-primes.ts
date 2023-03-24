/**
 * 计数质数
 * https://leetcode.cn/problems/count-primes/
 */

function countPrimes(n: number) {
  const isPrime = new Array(n).fill(1)
  let ans = 0
  for (let i = 2; i < n; ++i) {
    if (isPrime[i]) {
      ans += 1
      for (let j = i * i; j < n; j += i) {
        isPrime[j] = 0
      }
    }
  }
  return ans
}

let n = 3
console.log(countPrimes(3))
