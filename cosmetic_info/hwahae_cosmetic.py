import requests
import cx_Oracle
from bs4 import BeautifulSoup

url = "https://www.hwahae.co.kr/rankings?english_name=category&theme_id=4174"
res = requests.get(url)

cos_list = []
cos_list.append([])
cos_list.append([])

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
        cos_list[0].append(li[0].text)
        cos_list[1].append(li[1].text)

        i += 1
else:
    print(res.text)

# print(cos_list)

# for brand, name in zip(cos_list[0], cos_list[1]):
#     print(brand, "이름 : ", name)

conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
print(conn.version)
#2. 테이블 설정
sql = """
    INSERT INTO cosmetic(cosmetic_no, name, cos_image, cate_cd, company_name, company_logo)
    VALUES(SEQ_ID.NEXTVAL, :1, :2, :3, :4, :5)
"""
cur = conn.cursor()

for brand, name in zip(cos_list[0], cos_list[1]):
    cos_image = '/download?imageFileName='+name
    brand_image = '/download?imageFileName='+brand
    cur.execute(sql, [name, cos_image, 'SC03', brand, brand_image])

conn.commit()
conn.close()
