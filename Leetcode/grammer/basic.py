from functools import reduce
from operator import add, mul

# 함수형 기능에 람다 표현식 사용
print(list(map(lambda x: x + 10, [1, 2, 3])))

# 리스트 컴프리헨션 (List Comprehension)
print([n * 2 for n in range(1, 10 + 1) if n % 2 == 1])


original = {"a": 1, "b": 2, "c": 3}

print({key: value for key, value in original.items() if value > 1})


# 숫자형 리스트를 단일 값으로 병합하기

a = [1, 2, 3, 4, 5]

print("".join(map(str, a)))


print(reduce(lambda x, y: 10 * x + y, a, 0))


print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))
