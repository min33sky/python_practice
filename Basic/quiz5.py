from random import *


# 50명의 승객 중에 탑승 인원 선정하기

"""
  조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수
  조건2: 5분 ~ 15분 사이의 승객만 매칭
"""

count = 0

for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분".format(i, time))

print("총 탑승 승객 : {0}분".format(count))

