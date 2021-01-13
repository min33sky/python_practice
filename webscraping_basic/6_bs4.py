import requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4, lxml (파서)

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
print(soup.title.get_text())
print(soup.a)  # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs)  # a element의 속성 정보를 출력
print(soup.a["href"])  # a element의 href 속성 값을 출력

print(soup.find("a", attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"class": "Nbtn_upload"}))

rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())

# rank2 = rank1.next_sibling.next_sibling
# print(rank1.find_next_sibling("li"))  # 형제 li 태그를 가져온다.
# print(rank1.find_next_siblings("li"))  # 모든 형제 li 태그를 가져온다.

webtoon = soup.find("a", text="여신강림-139화")
# print(webtoon)
