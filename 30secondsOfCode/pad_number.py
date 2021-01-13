# 주어진 숫자를 특정 길이에 맞게 0으로 채운다.

def pad_number(n: int, l: int):
    return str(n).zfill(l)


print(pad_number(1234, 7))
