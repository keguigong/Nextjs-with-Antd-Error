/**
 * 最长回文子串
 * https://leetcode.cn/problems/longest-palindromic-substring/submissions/
 */

export function longestPalindrome(s: string): string {
  let str = ""
  for (let i = 0, start = 0, end = 0; i < s.length; i++) {
    start = i
    end = i
    while (end + 1 < s.length && s[end + 1] === s[i]) {
      end += 1
    }
    while (start - 1 >= 0 && end + 1 < s.length && s[end + 1] === s[start - 1]) {
      start -= 1
      end += 1
    }
    if (end > start && str.length < end - start + 1) {
      str = s.slice(start, end + 1)
    }
  }

  return str ? str : s[0]
}

export function dpLongestPalindrome(s: string): string {
  if (s === null || s.length < 2) return s

  const len = s.length
  let maxStart = 0
  let maxEnd = 0
  let maxLen = 0

  const dp: boolean[][] = Array.from(Array(len), () => Array(len).fill(false))

  for (let r = 1; r < len; r++) {
    for (let l = 0; l < r; l++) {
      if (s[l] == s[r] && (r - l <= 2 || dp[l + 1][r - 1])) {
        dp[l][r] = true
        if (r - l + 1 > maxLen) {
          maxLen = r - l + 1
          maxStart = l
          maxEnd = r
        }
      }
    }
  }

  return s.slice(maxStart, maxEnd + 1)
}

let str1 =
  "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"
console.log(dpLongestPalindrome(str1))
