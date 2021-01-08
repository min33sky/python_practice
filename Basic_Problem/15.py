def digits_multiplication(num: int):
    num = str(num).replace("0", "")
    result = 1
    for n in num:
      result *= int(n)
    return result


print(digits_multiplication(123405))
print(digits_multiplication(999))
print(digits_multiplication(1000))
print(digits_multiplication(1111))
