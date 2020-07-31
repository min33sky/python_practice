# https://leetcode.com/problems/array-partition-i/https://leetcode.com/problems/array-partition-i/
from typing import List


def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


print(arrayPairSum([1, 4, 3, 2]))

