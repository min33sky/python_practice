# 특정 값으로 리스트 채우기


def initialize_list_with_value(n, val=0):
    return [val for _ in range(n)]


print(initialize_list_with_value(5, 2))

