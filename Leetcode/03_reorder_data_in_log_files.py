# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda k: (k.split()[1:], k.split()[0]))
    return letters + digits


print(
    reorderLogFiles(
        [
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    )
)

