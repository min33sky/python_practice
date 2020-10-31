"""
그리디 알고리즘
-모험가 길드
"""

n = int(input())
data = list(map(int, input().split()))

data.sort()  # 오름차순 정렬

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹 인원 수


for i in data:  # 공포도를 낮은 것부터 확인한다
    count += 1  # 현재 그룹에 인원 추가
    if count >= i:  # 현재 그룹에 포함된 모험자 수가 현재 공포도 이상이라면 그룹 결성
        result += 1  # 그룹 수 증가
        count = 0  # 그룹 인원 초기화


print(result)

