"""
그리디 알고리즘
- 거스름돈 문제
"""

n = 1260  # 잔액
count = 0  # 동전 개수

# 큰 단위의 화폐부터 차례대로 확인
# ? 큰 단위는 항상 작은 단위의 배수이므로 알고리즘이 정당하다
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n = n % coin  # 남은 잔액

print(count)
