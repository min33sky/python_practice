# 리스트 컴프리헨션

a = [i for i in range(10) if i % 2 == 1]

print(a)


# 2차원 배열 초기화하기
# 3 X 4 행렬 초기화

b = [[0] * 4 for _ in range(3)]

print(b)


# lambda 활용

array = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))


from itertools import permutations, combinations

data = ["A", "B", "C"]

# 순열
result = list(permutations(data, 3))

print(result)

# 조합
result = list(combinations(data, 2))

print(result)

from itertools import product, combinations_with_replacement

# 중복 순열

result = list(product(data, repeat=2))

print(result)

# 중복 조합

result = list(combinations_with_replacement(data, 2))

print(result)


# 등장 횟수 세기

from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])

print(counter["blue"])
print(counter["green"])
print(dict(counter))

# 최대 공략수, 최소 공배수

from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


a = 21
b = 14

print(gcd(a, b))
print(lcm(a, b))

