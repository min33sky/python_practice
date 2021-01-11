
korean = ["사과", "포도", "바나나", "멜론"]
english = ["apple", "grape", "banana", "melon"]


mixed = list(zip(korean, english))
print(mixed)

kor, eng = list(zip(*mixed))
print(kor, eng)
