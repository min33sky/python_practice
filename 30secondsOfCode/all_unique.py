# all_unique : 리스트에서 중복이 있는지 체크
# set : 중복을 허용하지 않고 순서가 없는 자료구조

def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]

print(all_unique(x))
print(all_unique(y))
