"""
그리디 알고리즘
- 곱하기 혹은 더하기
"""

data = input()

result = int(data[0])


for idx in range(1, len(data)):
    # 두 수중에 하나라도 '0'이거나 '1'일 경우 더하고 아닐 경우 곱한다.
    num = int(data[idx])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
