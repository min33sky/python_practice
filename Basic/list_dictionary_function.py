# reserved(), items(), enumerate()
# 일회용 함수라 한번만 사용할 수 있다. (따로 변수에 담아서 사용하지 말자)

list1 = [321, 253, 112, 532, 664, 1123]

for idx, item in enumerate(list1):
    print(f"{idx} {item}")

print(list(reversed(list1)))

obj = {
    "key1": 1,
    "key2": 2,
    "key3": 3,
}

for key, value in obj.items():
    print(f"{key}, {value}")

