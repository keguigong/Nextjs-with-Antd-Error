/**
 * 括号生成
 * https://leetcode.cn/problems/generate-parentheses/
 */

export function generateParenthesis(n: number): string[] {
  if (n === 1) return ["()"]
  let result = []
  let length = 2 * n - 2

  function backtrace(res = "(", len = length, index = 0) {
    if (index < length) {
      backtrace(res + "(", len, index + 1)
      backtrace(res + ")", len, index + 1)
    } else {
      const tmpRes = res + ")"
      let calcRes = tmpRes.slice()

      while (/\(\)/.test(calcRes)) {
        calcRes = calcRes.replace("()", "")
      }

      if (!calcRes.length) {
        result.push(tmpRes)
      }
    }
  }

  backtrace()

  return result
}

console.log(generateParenthesis(3))
