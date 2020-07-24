# https://leetcode.com/problems/valid-palindrome/


def isPalindrome(s: str) -> bool:
    org = [char.lower() for char in s if char.isalnum()]
    return org == org[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

