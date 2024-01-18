/**
 *
 */

export function combinationSum(candidates: number[], target: number): number[][] {
  const ans = []
  const dfs = (target: number, combine: number[], idx: number) => {
    if (idx === candidates.length) {
      return
    }
    if (target === 0) {
      ans.push(combine)
      return
    }
    dfs(target, combine, idx + 1)
    if (target - candidates[idx] >= 0) {
      dfs(target - candidates[idx], [...combine, candidates[idx]], idx)
    }
  }

  dfs(target, [], 0)
  return ans
}

let candidates = [2, 3, 6, 7],
  target = 7
console.log(combinationSum(candidates, target))
