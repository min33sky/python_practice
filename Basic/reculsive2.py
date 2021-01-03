# 리스트를 평탄화하는 함수 (중첩된 리스트의 중첩을 모두 제거하고 1차원 리스트로 만들기)


def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten(item)
        else:
            output += [item]  # output.append(item)
    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
# example = [[1, 2, 3]]
print("원본:", example)
print("변환:", flatten(example))
