# 주어진 문자의 바이트 길이를 리턴한다.


def byte_size(s: str):
    return len(s.encode("utf-8"))


print(byte_size('😂'))
print(byte_size('Hello World'))
