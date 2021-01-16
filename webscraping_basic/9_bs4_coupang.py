import requests
import re
from bs4 import BeautifulSoup
from requests.api import head  # pip install beautifulsoup4, lxml (파서)

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

notebooks = soup.find_all("li", attrs={"class": re.compile("^search-product")})

# result = notebooks[0].find("div", attrs={"class": "name"}).get_text()

# 이름, 가격, 평점, 평가개수
for notebook in notebooks:
    name = notebook.find("div", attrs={"class": "name"}).get_text()
    price = notebook.find("strong", attrs={"class": "price-value"}).get_text()

    rate = notebook.find("em", attrs={"class": "rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"

    rating_cnt = notebook.find("span", attrs={"class": "rating-total-count"})
    if rating_cnt:
        rating_cnt = rating_cnt.get_text()
    else:
        rating_cnt = "평점 개수 없음"

    print(name, price, rate, rating_cnt)
