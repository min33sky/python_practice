import requests  # pip request requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()  # 에러가 있다면 발생 시킨다.

# ? 아래 코드 대신 raise_for_status() 코드를 쓰자
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러 코드: ", res.status_code, "]")

print(len(res.text))
# print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
