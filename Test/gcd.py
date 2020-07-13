# 최대공약수 구하기
# gcd(640, 400) -> 80

def getGcd(num1, num2):

    # 나누기 계산을 위해서 위치 변경
    if(num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp

    # 마지막으로 나눈 값(num2)이 최대공약수
    while(num1 % num2 != 0):
        remainder = num1 % num2
        num1 = num2
        num2 = remainder

    result = num2

    return result


print(getGcd(400, 640))