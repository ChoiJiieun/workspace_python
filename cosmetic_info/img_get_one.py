# -*- coding: utf-8 -*-

from urllib.request import urlretrieve

import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

img_folder = 'C:/dev/dev_pro/image_repo'

img_url = "https://dn5hzapyfrpio.cloudfront.net/product/8a6/8a67bbc0-7193-11ef-990d-0f4a6ecab821.jpeg?w=456"
name = "녹두 모공 타이트업 수딩 크림"

num = name.find("|")

print(img_url)
print('['+name[num+2:]+']')
product = name[num+2:]

urlretrieve(img_url, f'C:/dev/dev_pro/image_repo/{product}.jpg')

# driver = webdriver.Chrome()
# driver.implicitly_wait(2)
# driver.get(url)
# time.sleep(2)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# div = soup.select_one('.product__image-wrapper')
# img = div.select_one('.image__img')
# # print(img)
# url = img.get_attribute_list('src')
# div2 = soup.select_one('.product__summary')
# name = div2.select_one('.product__summary__name').text
# print(url[0], '['+name.strip()+']')