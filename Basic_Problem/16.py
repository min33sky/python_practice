def number_base(text: str, num: int):
    try:
        return int(text, num)
    except ValueError:
        return -1


print(number_base("AF", 16))
print(number_base("101", 2))
print(number_base("101", 5))
print(number_base("Z", 36))
print(number_base("AB", 10))

