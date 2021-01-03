file = open("test.txt", "w")
file.write("안녕하세요")
file.close()


file = open("test.txt", "a")
file.write("ㅋ")
file.close()


file = open("test.txt", "r")
print(file.read())
file.close()

# open, close를 축약해놓은 문법
with open("test.txt", "r") as file:
    print(file.read())

