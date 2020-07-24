from re import sub

# https://leetcode.com/problems/valid-palindrome/


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = sub("[^a-z0-9]", "", s)

    return s == s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

