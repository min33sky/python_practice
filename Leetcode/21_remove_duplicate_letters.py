# https://leetcode.com/problems/remove-duplicate-letters/

from collections import Counter


def removeDuplicateLetters(s: str) -> str:
    # counter : 문자들의 개수, seen : 이미 처리한 문자를 기록, stack: 결과물
    counter, seen, stack = Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        # 이미 처리한 문자라면 다음 문자로 넘어간다
        if char in seen:
            continue

        # 뒤에 붙일 문자가 있으면 스택에서 제거 한다
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return "".join(stack)

