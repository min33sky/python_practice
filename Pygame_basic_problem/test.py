def max_digit(number: int) -> int:
    return max(int(num) for num in str(number))


print(max_digit(52))


print(max(item for item in [1, 2, 3, 44, 2, 4]))

