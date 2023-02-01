/**
 * 罗马数字转整数
 * https://leetcode.cn/problems/roman-to-integer/
 */

function romanToInt(s: string): number {
  let romanMap = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let result = 0;

  for(let i = 0; i < s.length; i++) {
    if (i + 1 < s.length && romanMap[s[i]] < romanMap[s[i + 1]]) {
      result -= romanMap[s[i]]
    } else {
      result += romanMap[s[i]]
    }
  }
  return result;
}

let roman = "MCMXCIV";
console.log(romanToInt(roman));
