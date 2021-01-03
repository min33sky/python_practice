import sys
from datetime import datetime
import time
from urllib import request


# 명령 매개변수
print(sys.argv)


now = datetime.now()
print(now.year)
print(now.month)  # 파이썬은 월이 1부터 시작한다.
print(now.day)
print(now.hour)

# print("A")
# time.sleep(2)
# print("B")


target = request.urlopen("http://hanbit.co.kr")
content = target.read()

print(content[:100])
