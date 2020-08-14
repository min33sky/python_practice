# https://leetcode.com/problems/valid-parentheses/


def isValid(s: str) -> bool:

    stack = []
    table = {")": "(", "]": "[", "}": "{"}

    # 문자열 반복
    for char in s:
        # 여는 괄호일 경우에 스택에 push
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != table.pop():
            return False

    return len(stack) == 0

