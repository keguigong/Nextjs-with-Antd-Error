/**
 * **Q1. (20%)** Write a program in C, C++, Python or Java that 
 * inputs an array of 2023 numbers with distinct array entries 
 * chosen from the 2024 integers 0, 1, 2, …, 2022, 2023 and then 
 * prints the missing integer. For example, if the array stores 
 * the 2023 numbers 1, 2, 3, ..., 2022, 2023, then your program 
 * should print 0.
 * 
 * You may assume that the input has 2023 lines, each contains a 
 * distinct integer in {0, 1, 2,..., 2023}. Also, note that the 
 * mark will be determined by the correctness, efficiency, and 
 * memory usage of your program.
 */



function findMissingNum(arr: Array<number>): number {
  let kth = Math.floor(arr.length / 2)
  let leftKth = 0
  let rightKth = arr.length

  function findKthNum(kth: number, arr: Array<number>) {
    if (arr[kth - 1] < kth) {
      leftKth = kth
      kth = kth + Math.floor((rightKth - kth) / 2)
      findKthNum(kth, arr)
    } else {
      rightKth = kth
      kth = Math.floor((leftKth + kth) / 2)
      findKthNum(kth, arr)
    }
  }
}