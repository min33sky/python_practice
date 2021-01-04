# 딕셔너리에서 키 값만을 가져오자.


def keys_only(flat_dict: dict):
    return list(flat_dict.keys())

age = {
    "peter": 10,
    "Isabel": 11,
    "Anna": 12,
}

print(keys_only(age))
