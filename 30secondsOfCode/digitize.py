# 숫자를 문자 리스트로 변환하기


def digitize(n):
    return list(map(int, str(n)))


print(digitize(12345))
