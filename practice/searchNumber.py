import random

print("숫자 맞추기 게임")

choice = random.randrange(100)

while True:
    user_choice = int(input("100보다 작은 숫자를 입력하세요!! "))

    if user_choice == choice:
        break

    if choice < user_choice:
        print("입력한 값이 너무 높아요!!")
    else:
        print("입력한 값이 너무 낮아요!!")


print("정답입니다!! 축하합니다!! 프로그램 종료하겠습니다.")

