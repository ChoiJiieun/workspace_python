# -*- coding: utf-8 -*-
import time
import re
import cx_Oracle
import requests

from bs4 import BeautifulSoup
from selenium import webdriver

cos_list = []
cos_list.append([])
cos_list.append([])

# 브라우저 오픈
driver = webdriver.Chrome()
driver.implicitly_wait(3) # 브라우저가 켜질 때까지 대기.
# 아이크림
url = "https://www.glowpick.com/categories/1?ids=4"
# url 페이지로 이동
driver.get(url)
time.sleep(1) # 1초 멈춤
soup = BeautifulSoup(driver.page_source, 'html.parser')
uls = soup.select('.ranking__contents.contents li')
time.sleep(2)
driver.quit()

for ul in uls:
    company = ul.select_one('.details__brand').text
    product = ul.select_one('.details__product').text
    # print('['+company+']', '['+product.strip()+']')
    cos_list[0].append(company)
    cos_list[1].append(product.strip())

# print(cos_list[0])
# print(cos_list[1])

conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
print(conn.version)
sql = """
    INSERT INTO cosmetic(cosmetic_no, name, cos_image, cate_cd, company_name, company_logo)
    VALUES(SEQ_ID.NEXTVAL, :1, :2, :3, :4, :5)
"""
cur = conn.cursor()

for brand, name in zip(cos_list[0], cos_list[1]):
    cos_image = '/download?imageFileName='+name+'.jpg'
    brand_image = '/download?imageFileName='+brand+'.jpg'
    cur.execute(sql, [name, cos_image, 'SC09', brand, brand_image])
    print(name, brand)

conn.commit()
conn.close()