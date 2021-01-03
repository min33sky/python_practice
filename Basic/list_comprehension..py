# 10진수와 2진수 변환
print("{:b}".format(10))
print(int("1010", 2))


# 1 ~ 100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고 그 숫자들의 합을 구하라


output = [x for x in range(1, 100 + 1) if "{:b}".format(x).count("0") == 1]


for i in output:
    print("{} : {:b}".format(i, i))


print("합계", sum(output))

