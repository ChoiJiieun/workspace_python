import time
import re
from urllib.request import urlretrieve

import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

json_data = '{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","item":{"@type":"Product","name":"1위 주미소 | 포어 퓨리파잉 살리실산 포밍 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/d7b/d7b964c0-2790-11ef-b74b-79316ef070e9.jpeg","url":"https://www.glowpick.com/products/170360","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.72","reviewCount":205}},"position":1},{"@type":"ListItem","item":{"@type":"Product","name":"2위 닥터릴리프 | 디에이씨투 카렌듈라 카밍 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/cdd/cddb3ea0-0089-11ec-8d15-f5a4c111a76c.jpeg","url":"https://www.glowpick.com/products/150003","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.59","reviewCount":322}},"position":2},{"@type":"ListItem","item":{"@type":"Product","name":"3위 라프텔 | 페이셜 클렌저 딥클린","image":"https://dn5hzapyfrpio.cloudfront.net/product/4c0/4c04cbd0-8809-11ee-a267-8dd48385bbd2.jpeg","url":"https://www.glowpick.com/products/169300","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.58","reviewCount":145}},"position":3},{"@type":"ListItem","item":{"@type":"Product","name":"4위 휴캄 | 어성초 진정 클린 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/c73/c732ff90-a8e8-11ec-9bd8-c5044ba0ab0c.jpeg","url":"https://www.glowpick.com/products/147177","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.60","reviewCount":159}},"position":4},{"@type":"ListItem","item":{"@type":"Product","name":"5위 토르홉 | 카모스 블랙 소금거품 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/9bb/9bbde300-60fd-11ef-b954-67bd70304544.jpeg","url":"https://www.glowpick.com/products/175078","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.67","reviewCount":67}},"position":5},{"@type":"ListItem","item":{"@type":"Product","name":"6위 일루미엘 | AC 솔루션 폼클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/736/736545b0-b40f-11ee-a054-3f67d73ea0d5.jpeg","url":"https://www.glowpick.com/products/170347","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.55","reviewCount":106}},"position":6},{"@type":"ListItem","item":{"@type":"Product","name":"7위 포이유이 | 딥 포어 펀클렌징 약산성 발효 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/d72/d72f1290-189a-11ed-b7df-6beca1cf3622.png","url":"https://www.glowpick.com/products/158650","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.57","reviewCount":115}},"position":7},{"@type":"ListItem","item":{"@type":"Product","name":"8위 와이비케이 | 릴리프 하이드레이션 라이트 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/5f6/5f6cb940-46e5-11ee-81cb-0f28cefa70d2.jpeg","url":"https://www.glowpick.com/products/167618","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.74","reviewCount":62}},"position":8},{"@type":"ListItem","item":{"@type":"Product","name":"9위 프리메라 | 오가니언스 BR 소프트 필링 투 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/b2a/b2ad0370-fea7-11ed-82ee-7fedbc034a57.jpeg","url":"https://www.glowpick.com/products/164756","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.52","reviewCount":148}},"position":9},{"@type":"ListItem","item":{"@type":"Product","name":"10위 토코보 | 코코넛 클레이 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/ddd/ddd75620-9ac3-11ec-84e0-b7c2ecdee61c.jpeg","url":"https://www.glowpick.com/products/155201","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":202}},"position":10},{"@type":"ListItem","item":{"@type":"Product","name":"11위 쥬스 투 클렌즈 | 레스 레스 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/1e4/1e4e7880-7850-11ee-b842-db65e1eeb438.jpeg","url":"https://www.glowpick.com/products/152829","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":263}},"position":11},{"@type":"ListItem","item":{"@type":"Product","name":"12위 토리든 | 다이브인 저분자 히알루론산 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/15a/15ab92c0-3405-11ed-acac-8da0e32203af.jpeg","url":"https://www.glowpick.com/products/159365","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.55","reviewCount":224}},"position":12},{"@type":"ListItem","item":{"@type":"Product","name":"13위 이니스프리 | 화산송이 바하 모공 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/91d/91d7e300-bd88-11ed-b46b-d9632ba1c8bb.jpeg","url":"https://www.glowpick.com/products/162105","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.52","reviewCount":201}},"position":13},{"@type":"ListItem","item":{"@type":"Product","name":"14위 블랑네이처 | 아크네 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/6d1/6d1a61d0-24ff-11ee-89e2-8f2524962d30.jpeg","url":"https://www.glowpick.com/products/165650","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.48","reviewCount":254}},"position":14},{"@type":"ListItem","item":{"@type":"Product","name":"15위 듀이트리 | AC 컨트롤 딥 그린 카밍 트러블 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/cd0/cd079420-068f-11ee-a168-1156b8df51df.jpeg","url":"https://www.glowpick.com/products/165909","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":76}},"position":15},{"@type":"ListItem","item":{"@type":"Product","name":"16위 브이앤코 | 브이 코어텍틴 클렌징폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/dde/ddeb7df0-480f-11ec-aee9-87d52af0404f.jpeg","url":"https://www.glowpick.com/products/152489","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.47","reviewCount":121}},"position":16},{"@type":"ListItem","item":{"@type":"Product","name":"17위 아크네스 | 더마 릴리프 모이스처 폼클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/9b2/9b252a60-8a59-11ed-934c-a5f7267a0f0b.jpeg","url":"https://www.glowpick.com/products/161806","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":113}},"position":17},{"@type":"ListItem","item":{"@type":"Product","name":"18위 메디필 | 그린 시카 콜라겐 클리어 2.0","image":"https://dn5hzapyfrpio.cloudfront.net/product/911/91163290-ae93-11ed-8f8a-317bf280196c.jpeg","url":"https://www.glowpick.com/products/163018","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.46","reviewCount":157}},"position":18},{"@type":"ListItem","item":{"@type":"Product","name":"19위 에스트라 | 테라크네365 클리어 딥 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/424/424b9660-d9a3-11ed-8cc7-35b762171ff0.jpeg","url":"https://www.glowpick.com/products/147534","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.43","reviewCount":663}},"position":19},{"@type":"ListItem","item":{"@type":"Product","name":"20위 코이 | 플로우 에센스 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/e12/e12381a0-a756-11ed-b852-933e07cf2550.jpeg","url":"https://www.glowpick.com/products/152394","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":103}},"position":20}]}'
data = json.loads(json_data)

img_folder = 'C:/dev/dev_pro/image_repo'

for i in range(20):
    img_url = data["itemListElement"][i]["item"]["image"]
    name = data["itemListElement"][i]["item"]["name"]

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