def second_index(text: str, c: str):
    # 문장 내에서 찾을 문자 개수 확인
    if text.count(c) < 2:
        return None

    # 첫 번째 인덱스
    first_index = text.find(c)

    return text.find(c, first_index + 1)


print(second_index("sims", "s"))
print(second_index("find the river", "e"))
print(second_index("hi", " "))
