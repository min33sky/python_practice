import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4, lxml (파서)

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
# cartoons = soup.find_all("td", attrs={"class": "title"})
# print(cartoons[0].a.get_text())
# print(cartoons[0].a["href"])

# for cartoon in cartoons:
#     text = cartoon.a.get_text()
#     url = 'https://comic.naver.com' + cartoon.a["href"]
#     print(text, url)

# 가우스 전자 평점 가져오기
cartoons = soup.find_all("div", attrs={"class": "rating_type"})


total_rates = 0
for cartoon in cartoons:
    print(cartoon.strong.get_text())
    total_rates += float(cartoon.strong.get_text())

print("평균 평점:", round(total_rates / len(cartoons), 3))
