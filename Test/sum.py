# 합 구하기

# 일반 반복문
def sum(arr):
    total = 0
    for x in arr:
        total += x

    return total

# 재귀 이용
def reculsiveSum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + reculsiveSum(arr[1:])


print(sum([1,2,3,4]))
print(reculsiveSum([1,2,3,4]))
