from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}  # 검색 속도를 높이기 위한 딕셔너리
    for idx, num in enumerate(nums):
        if target - num in nums_map:  # 딕셔너리에 존재하면 인덱스들을 리턴
            return [idx, nums_map[target - num]]
        nums_map[num] = idx  # 딕셔너리에 현재 값이 존재하지 않으므로 숫자와 인덱스 삽입


print(twoSum([2, 7, 11, 15], 9,))
print(twoSum([2, 5, 5, 11], 10,))
print(twoSum([3, 2, 4], 6,))

