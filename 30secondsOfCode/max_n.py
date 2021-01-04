# 리스트에서 내림차순으로 n개 뽑기


def max_n(lst, n=1):
    return sorted(lst, reverse=True)[:n]


print(max_n([1, 2, 3]))
print(max_n([1, 2, 3], 2))

