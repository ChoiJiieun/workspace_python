import requests
from bs4 import BeautifulSoup

url = "https://www.hwahae.co.kr/rankings?english_name=category&theme_id=4156"
res = requests.get(url)
if res.status_code == 200:
    soup = BeautifulSoup(res.content, 'html.parser')
    # print(soup.prettify())
    uls = soup.select('.px-20 li')
    # print(uls)
    i = 1
    for ul in uls:
        li = ul.select('.space-y-4.ml-12 span')
        # hds-text-body-medium
        print(i, li[0].text, li[1].text)
        i += 1
else:
    print(res.text)
