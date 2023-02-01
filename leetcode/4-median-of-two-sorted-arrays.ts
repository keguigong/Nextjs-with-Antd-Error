/**
 * 寻找两个正序数组的中位数
 * https://leetcode.cn/problems/median-of-two-sorted-arrays/
 */

function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
  let m = nums1.length;
  let n = nums2.length;
  let k1 = Math.floor((m + n + 1) / 2);
  let k2 = Math.floor((m + n + 2) / 2);
  return (
    (findKth(nums1, 0, nums2, 0, k1) + findKth(nums1, 0, nums2, 0, k2)) / 2
  );

  function findKth(
    nums1: number[],
    left1: number,
    nums2: number[],
    left2: number,
    k: number
  ): number {
    let len1 = nums1.length - left1;
    let len2 = nums2.length - left2;

    if (len1 > len2) return findKth(nums2, left2, nums1, left1, k);
    if (len1 === 0) return nums2[left2 + k - 1];

    if (k === 1) return Math.min(nums1[left1], nums2[left2]);

    let i = left1 + Math.min(len1, Math.floor(k / 2)) - 1;
    let j = left2 + Math.min(len2, Math.floor(k / 2)) - 1;

    if (nums1[i] > nums2[j]) {
      return findKth(nums1, left1, nums2, j + 1, k - (j - left2 + 1));
    } else {
      return findKth(nums1, i + 1, nums2, left2, k - (i - left1 + 1));
    }
  }
}

let nums1 = [0, 0, 0, 0, 0];
let nums2 = [-1, 0, 0, 0, 0, 0, 1];
console.log(findMedianSortedArrays(nums1, nums2));
