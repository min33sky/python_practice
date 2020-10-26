"""
그리디 알고리즘
- 숫자 카드 게임
"""

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0

# 한 줄씨 입력 받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 행에서 가장 작은 수를 찾기
    min_value = min(data)
    # 가장 작은 수중에서 가장 큰 수를 찾기
    result = max(min_value, result)

print(result)

