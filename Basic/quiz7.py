for i in range(1, 11):
    fileName = str(i) + "주차.txt"
    with open(fileName, "w", encoding="utf8") as test:
        test.write("- {0} 주차 주간보고 - \n".format(i))
        test.write("부서 : \n")
        test.write("이름 : \n")
        test.write("업무 요약 : \n")

