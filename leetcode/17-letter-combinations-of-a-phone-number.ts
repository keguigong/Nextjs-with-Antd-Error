/**
 * 电话号码的字母组合
 * https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
 */

function letterCombinations(digits: string): string[] {
  const keyMap = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
  };
  let comb = [];

  function backtrace(digits: string, index: number, letters: string) {
    if (index >= digits.length) {
      letters && comb.push(letters);
      return;
    }

    const key: string[] = keyMap[digits[index]];
    key.forEach((elememt) => {
      let _letters = letters + elememt;
      backtrace(digits, index + 1, _letters);
    });
  }

  backtrace(digits, 0, "");
  return comb;
}

export let digits = "234";
console.log(letterCombinations(digits));
