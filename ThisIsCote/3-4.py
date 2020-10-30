"""
그리디 알고리즘
- 1이 될 때까지
"""

# N, K값을 입력 받는다.
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 빼기
    target = (n // k) * k
    result += n - target
    n = target
    # N이 K보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    n //= k
    result += 1

# 나머지 값이 1이 될때까지 뺀 횟수를 더한다
result += n - 1
print(result)
