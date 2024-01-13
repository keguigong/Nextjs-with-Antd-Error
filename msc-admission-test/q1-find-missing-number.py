from typing import List


def find_missing_number(nums: List[int]):
    """
    Write a program in C, C++, Python or Java that inputs an array of 2023 numbers with distinct array entries chosen from the 2024 integers 0, 1, 2, …, 2022, 2023 and then prints the missing integer.

    For example, if the array stores the 2023 numbers 1, 2, 3, ..., 2022, 2023, then your program should print 0.

    You may assume that the input has 2023 lines, each contains a distinct integer in {0, 1, 2,..., 2023}. Also, note that the mark will be determined by the correctness, efficiency, and memory usage of your program.
    """
    for i in range(2024):
        if nums[i] != i:
            return i


def testbench():
    nums = [0] * 2024
    for i in range(2024):
        nums[i] = i
    del nums[1000]
    return find_missing_number(nums)


print(testbench())
