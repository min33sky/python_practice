# 팩토리얼 함수

# 1) n! = 1 x 2 x 3 x 4 x ....... (n-2) x (n-1) x n


def factorial1(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


print(factorial1(10))

# 2) n! = n * (n-1)!, 0! = 1


def factorial2(n):
    if n == 0:
        return 1
    return n * factorial2(n - 1)


print(factorial2(10))

# 피보나치 수열

# fibo(1) = 1, fibo(2) = 1, fibo(3) = 2, fibo(4) = 3.... fibo(n) = fibo(n-1) + fibo(n-2)

count = 0


def fibo(n):
    global count
    count += 1
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(35))
print(count)

# 메모화 적용

memo = {1: 1, 2: 1}

count = 0


def fibo_memo(n):
    global count
    count += 1
    if n in memo:
        return memo[n]
    result = fibo_memo(n - 1) + fibo_memo(n - 2)
    memo[n] = result
    return result


print(fibo_memo(35))
print(count)

