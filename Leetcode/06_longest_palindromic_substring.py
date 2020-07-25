# https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome(s: str) -> str:
    # 예외 조건
    if len(s) < 2 or s == s[::-1]:
        return s

    # 팰린드롭 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # ! 슬라이싱 할 때의 인덱스와 조회 할 때의 인덱스는 표기방식이 다르다
        # 시작 인덱스가 -1된 상태이므로 원상태로 복구시킨다.
        # 종료 인덱스는 +1 됐지만 종료 인덱스 전까지 슬라이싱 되므로 바꿀 필요가 없다
        return s[left + 1 : right]

    result = ""
    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("c"))
print(longestPalindrome("cbskhksbd"))
