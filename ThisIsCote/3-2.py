"""
그리디 알고리즘
- 큰 수의 법칙
"""


# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)  # 입력받은 수를 역순으로 정렬

first = data[0]  # 첫 번째로 큰 수
second = data[1]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (m // (k + 1)) * k
count += m % (k + 1)  # 나누어 떨어지지 않는 경우에 큰 수가 더해질 횟수 추가

# 총 횟수 계산하기
result = first * count  # 가장 큰 수 더하기
result += second * (m - count)  # 두 번째로 큰 수 더하기

print(result)
