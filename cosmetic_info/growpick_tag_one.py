# -*- coding: utf-8 -*-
import time
import re
import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.glowpick.com/products/173413'
cos_num = 189
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get(url)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 500)")
soup = BeautifulSoup(driver.page_source, 'html.parser')
div = soup.select_one('.info__article.description')
tag_div = div.select_one('.info__article__contents')
tag = tag_div.select_one('.description__list')
arrs = tag.select('.description__list__item')

driver.quit()

tag_name = ""

for arr in arrs:
    # print(arr.text.strip())
    tag_name = tag_name + arr.text.strip() + " "

print(tag_name)

conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
print(conn.version)

try:

    sql = """
        UPDATE cosmetic SET hashtag = :1
        WHERE cosmetic_no = :2
    """
    cur = conn.cursor()

    # idx를 바인딩 파라미터에 추가
    cur.execute(sql, [tag_name, cos_num])
except Exception as e:
    print(str(e))

conn.commit()
conn.close()
