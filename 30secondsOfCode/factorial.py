# 팩토리얼 계산

def factorial(num: int):
    if not ((num >= 0) and (num % 1 == 0)):  # int형 양수여야 한다.
        raise Exception("Number can't be floating point or negative")
    return 1 if num == 0 else num * factorial(num - 1)


print(factorial(6))
