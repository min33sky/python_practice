# 주어진 범위에 가장 가까운 수를 출력

def clamp_number(num: int, a: int, b: int):
    return max(min(num, max(a, b)), min(a, b))


print(clamp_number(2, 3, 5))
print(clamp_number(1, -1, -5))
