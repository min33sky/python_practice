# 리스트에서 중복이 아닌 값들만 가져오기


from collections import Counter


def filter_non_unique(lst):
    return [item for item, count in Counter(lst).items() if count == 1]

print(filter_non_unique([1,2,2,3,4,4,5]))



