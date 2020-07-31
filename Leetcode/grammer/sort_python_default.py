# #############################################
# 파이선에서 제공하는  여러가지 정렬 방법
# #############################################


# sorted() : 정렬한 값을 리스트로 리턴하는 함수
a = [2, 5, 1, 9, 7]

print(sorted(a))

b = "zbdaf"

print(sorted(b))

print("".join(sorted(b)))


# sort() : 리스트의 메소드. 제자리 정렬로 리턴 값이 없다

alist = ["b", "a", "c"]

alist.sort()

print(alist)

# sorted()에서 key 옵션 사용하기

c = ["ccc", "aaaa", "d", "bb"]

print(sorted(c, key=len))

a = ["cde", "cfc", "abc"]


def fn(s):
    return s[0], s[-1]


print(sorted(a, key=fn))

# lamda를 사용해서 동일한 결과 출력

print(sorted(a, key=lambda s: (s[0], s[-1])))

