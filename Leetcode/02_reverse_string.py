# https://leetcode.com/problems/reverse-string/


def reverseString(s) -> None:
    # s = s[::-1] 리트코드에서는 오류 발생
    s[:] = s[::-1]


reverseString(["h", "e", "l", "l", "o"])

