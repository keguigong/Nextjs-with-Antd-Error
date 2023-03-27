/**
 * 最长有效括号
 * https://leetcode.cn/problems/longest-valid-parentheses/
 */

export function longestValidParentheses(s: string): number {
  let maxLen = 0
  let stack: number[] = []
  stack.push(-1)
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(") {
      stack.push(i)
    } else {
      stack.pop()
      if (stack.length) {
        maxLen = Math.max(maxLen, i - stack[stack.length - 1])
      } else {
        stack.push(i)
      }
    }
  }
  return maxLen
}

export function longestValidParentheses1(s: string): number {
  const dp = new Array(s.length).fill(0)
  let maxLen = 0
  for (let i = 1; i < s.length; i++) {
    if (s[i] === ")") {
      if (s[i - 1] === "(") {
        dp[i] = (i >= 2 ? dp[i - 2] : 0) + 2
      } else if (i - dp[i - 1] > 0 && s[i - dp[i - 1] - 1] === "(") {
        dp[i] = dp[i - 1] + (i - dp[i - 1] >= 2 ? dp[i - dp[i - 1] - 2] : 0) + 2
      }
      maxLen = Math.max(maxLen, dp[i])
    }
  }

  return maxLen
}

let s = "(()"
console.log(longestValidParentheses(s))
