# f(x) = 2x + 1


def f1(x):
    return 2 * x + 1


print(f1(10))

# f(x) = x제곱 + 2x + 1


def f2(x):
    return x ** 2 + 2 * x + 1


print(f2(10))


# 가변 매개변수의 곱을 리턴하는 함수


def mul(*values):
    return sum(x for x in values)


print(mul(5, 7, 9, 10))

