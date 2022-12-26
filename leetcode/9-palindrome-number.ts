/**
 * https://leetcode.cn/problems/palindrome-number/
 */

function isPalindrome(x: number): boolean {
  if (x < 0) return false

  let initVal = x
  let revVal = 0
  for(;initVal > 0;) {
    revVal = revVal * 10 + initVal % 10
    initVal = Math.floor(initVal / 10)
  }
  return revVal === x
};

let num = 12321
console.log(isPalindrome(num))