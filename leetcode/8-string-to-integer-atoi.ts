/**
 * https://leetcode.cn/problems/string-to-integer-atoi/
 */
function myAtoi(s: string): number {
  let isNegtive = 1;
  let tempArr = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") continue;

    if (/[a-z]/.test(s[i])) return 0;

    if (s[i] === "+" && i + 1 < s.length && /[0-9]/.test(s[i + 1])) {
      while (i + 1 < s.length && /[0-9]/.test(s[i + 1])) {
        tempArr.push(parseInt(s[i + 1]));
        i += 1;
      }
      break;
    }

    if (s[i] === "-" && i + 1 < s.length && /[0-9]/.test(s[i + 1])) {
      isNegtive = -1;

      while (i + 1 < s.length && /[0-9]/.test(s[i + 1])) {
        tempArr.push(parseInt(s[i + 1]));
        i += 1;
      }
      break;
    }

    while (i < s.length && /[0-9]/.test(s[i])) {
      tempArr.push(parseInt(s[i]));
      i += 1;
    }
    break;
  }

  let prevVal = 0;
  let calcVal = prevVal;
  for (let i = 0; i < tempArr.length; i++) {
    calcVal = prevVal * 10 + tempArr[i];
    if (calcVal * isNegtive > Math.pow(2, 31) - 1) return Math.pow(2, 31) - 1;
    else if (calcVal * isNegtive < -Math.pow(2, 31)) return -Math.pow(2, 31);
    prevVal = calcVal;
  }
  return calcVal * isNegtive;
}

let str = "+-12";
console.log(myAtoi(str));
