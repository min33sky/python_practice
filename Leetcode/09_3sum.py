# https://leetcode.com/problems/3sum/
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()  # 정렬

    for i in range(len(nums) - 2):
        # 중복은 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0인 경우이므로 정답 및 스킵 처리
                results.append((nums[i], nums[left], nums[right]))

                # 다음 인덱스에 해당하는 값이 중복일 경우 스킵
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return results


print(threeSum([-1, 0, 1, 2, -1, -4]))
