from random import *

"""
1명 치킨, 3명 커피 당첨 추첨 프로그램
조건 1: 댓글은 20명이 작성. 아이디는 1~20이라고 가정
조건 2: 무작위 추첨. 중복 불가
조건 3: random 모듈의 shuffle과 sample 활용

(출력 예제)
  -- 당첨자 발표 --
    치킨 당첨자 : 1
    커피 당첨자 : [2, 3, 4]
  -- 축하합니다 --
"""

list = list(range(1, 21))

shuffle(list)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(list.pop(0)))
print("커피 당첨자 : {0}".format(sample(list, 3)))
print(" -- 축하합니다--")

