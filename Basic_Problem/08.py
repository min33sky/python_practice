def checkio(num: int):
    if num % 15 == 0:
        return "Fizz Buzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print(checkio(15) == "Fizz Buzz")
print(checkio(6) == "Fizz")
print(checkio(5) == "Buzz")
print(checkio(7) == "7")

