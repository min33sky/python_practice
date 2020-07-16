"""
 남자 : 키(m) * 키(*) * 22
 여자 : 키(m) * 키(*) * 21

 함수명 : std_weight
 전달값 : 키(height), 성별(gender)
 표준 체중은 소수점 두 자리까지만 표시
"""


def std_weight(height, gender):
    if gender == "남자":
        standardWeight = (height / 100) * (height / 100) * 22
    else:
        standardWeight = (height / 100) * (height / 100) * 21

    print(
        "키 {0}cm {1}의 표준 체중은 {2}kg 입니다".format(height, gender, round(standardWeight, 2))
    )


std_weight(175, "남자")
std_weight(160, "여자")

