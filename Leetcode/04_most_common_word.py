from typing import List
from collections import *
from re import sub


def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [
        word
        for word in sub(r"[^\w]", " ", paragraph).lower().split()
        if word not in banned
    ]

    # counts = defaultdict(int)
    # for word in words:
    #     counts[word] += 1

    # return max(counts, key=counts.get)

    return Counter(words).most_common()[0][0]


print(
    mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
)

