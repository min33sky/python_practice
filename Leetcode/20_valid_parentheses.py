# https://leetcode.com/problems/valid-parentheses/


def isValid(s: str) -> bool:

    stack = []
    table = {")": "(", "]": "[", "}": "{"}

    # 문자열 반복
    for char in s:
        # 여는 괄호일 경우에 스택에 push
        if char not in table:
            stack.append(char)
        # 닫는 괄호일 때 스택이 비어있거나 팝한 괄호와 같지 않을 경우
        elif not stack or table[char] != stack.pop():
            return False

    # 스택이 비어있지 않으면 False
    return len(stack) == 0

