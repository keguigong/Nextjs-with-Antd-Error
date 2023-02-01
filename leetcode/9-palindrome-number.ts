/**
 * 回文数
 * https://leetcode.cn/problems/palindrome-number/
 */

function isPalindrome(x: number): boolean {
  if (x < 0) return false
  if (x > 0 && x % 10 === 0) return false

  let initVal = x
  let revVal = 0
  for(;initVal > revVal;) {
    revVal = revVal * 10 + initVal % 10
    initVal = Math.floor(initVal / 10)
  }
  return initVal === revVal || initVal === Math.floor(revVal / 10)
};

(function () {
  let num = 10
  console.log(isPalindrome(num))
})();