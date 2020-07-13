url = "http://naver.com"

# 규칙1) http:// 제거
step1 = url.split("//")[1]

# 규칙2) .이후 제외

idx = step1.index(".")

step2 = step1[:idx]

print(step2)

# 규칙3) 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성

theFirstThree = step2[:3]
length = len(step2)
eCount = step2.count("e")


password = theFirstThree + str(length) + str(eCount) + "!"

# print("{0}의 비밀번호는 {1} 입니다".format(url, password))

# 파이썬 3.6이상 사용 가능 문법
print(f"{url}의 비밀번호는 {password} 입니다.")
