/**
 * 整数转罗马数字
 * https://leetcode.cn/problems/integer-to-roman/
 */

function intToRoman(num: number): string {
  let valueMap = [
    ["M", 1000],
    ["CM", 900],
    ["D", 500],
    ["CD", 400],
    ["C", 100],
    ["XC", 90],
    ["L", 50],
    ["XL", 40],
    ["X", 10],
    ["IX", 9],
    ["V", 5],
    ["IV", 4],
    ["I", 1],
  ];

  let str = "";
  for (const [roman, value] of valueMap) {
    while (num >= value) {
      num -= value as number;
      str += roman;
    }

    if (num === 0) break;
  }
  return str;
}

export let num = 58;
console.log(intToRoman(num));
