/**
 * 字符串转换整数 (atoi)
 * https://leetcode.cn/problems/string-to-integer-atoi/
 */

function myAtoi(s: string): number {
  let index = 0;
  while (index < s.length && s[index] === " ") {
    index++;
  }

  let sign = 1;
  if (s[index] === "-") {
    sign = -1;
    index++;
  } else if (s[index] === "+") {
    index++;
  }

  let calcVal = 0;
  while (index < s.length && /[0-9]/.test(s[index])) {
    calcVal = calcVal * 10 + Number.parseInt(s[index]);
    index++;
  }
  if (sign * calcVal > Math.pow(2, 31) - 1) return Math.pow(2, 31) - 1;
  else if (sign * calcVal < -Math.pow(2, 31)) return -Math.pow(2, 31);
  return calcVal * sign;
}

let str = "-12";
console.log(myAtoi(str));
