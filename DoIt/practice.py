import copy

# copy()

x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()  # x를 y로 얕은 복사
x[0][1] = 9
print(x)
print(y)  # 이 리스트도 위의 원솟값 변경으로 값이 변경되었다.

x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x)  # x를 y로 깊은 복사
x[0][1] = 9
print(x)
print(y)  # 영향을 받지 않음

"""
    얕은 복사와 깊은 복사
    1. 얕은 복사: 참조값만 복사
    2. 깊은 복사: 참조값과 참조하는 객체 자체를 복사
"""
