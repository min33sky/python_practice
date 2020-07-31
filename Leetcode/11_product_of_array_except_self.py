# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:

    result = []
    p = 1

    for idx in range(len(nums)):
        result.append(p)
        p = p * nums[idx]

    p = 1

    for idx in range(len(nums) - 1, 0 - 1, -1):
        result[idx] = result[idx] * p
        p = p * nums[idx]


    return result


print(productExceptSelf([1, 2, 3, 4]))

