from math import comb

# 이항 계수
# n 개가 주어졌을때 순서에 상관없이 k개를 고르는 방법의 수

def binomial_coefficient(n: int, k: int):
    return comb(n, k)


print(binomial_coefficient(8, 2))
