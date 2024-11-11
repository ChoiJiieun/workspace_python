# -*- coding: utf-8 -*-
import time
import re
import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

json_data = '{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","item":{"@type":"Product","name":"1위 랩클 | 스텝 다운 모이스처라이징 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/fa6/fa6c7380-8cc9-11ed-b540-a9ad6d038df5.jpeg","url":"https://www.glowpick.com/products/161911","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.73","reviewCount":344}},"position":1},{"@type":"ListItem","item":{"@type":"Product","name":"2위 마녀공장 | 판테토인 크림 ","image":"https://dn5hzapyfrpio.cloudfront.net/product/f7b/f7b858e0-784e-11ee-bdb8-a9fd59bf9d4f.jpeg","url":"https://www.glowpick.com/products/161330","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.65","reviewCount":874}},"position":2},{"@type":"ListItem","item":{"@type":"Product","name":"3위 헤브블루 | 펜타베리 판테놀 리페어 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/309/309a0580-63ee-11ed-a59a-17ce736231dc.jpeg","url":"https://www.glowpick.com/products/160775","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.75","reviewCount":106}},"position":3},{"@type":"ListItem","item":{"@type":"Product","name":"4위 에스트라 | 아토베리어365 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/4ff/4ffddc50-8812-11ee-b2fa-3b16a1075b95.jpeg","url":"https://www.glowpick.com/products/169302","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.65","reviewCount":1236}},"position":4},{"@type":"ListItem","item":{"@type":"Product","name":"5위 큐어코드 | 더블 베리어 크림","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/20191113/1573611704518.jpg","url":"https://www.glowpick.com/products/127636","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.60","reviewCount":874}},"position":5},{"@type":"ListItem","item":{"@type":"Product","name":"6위 에스트라 | 아토베리어 크림 MD","image":"https://dn5hzapyfrpio.cloudfront.net/product/0e1/0e1c8350-512a-11ee-8002-fd47423b13e2.jpeg","url":"https://www.glowpick.com/products/118872","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.67","reviewCount":255}},"position":6},{"@type":"ListItem","item":{"@type":"Product","name":"7위 네오스랩 | 에센스 락커 리피드세라","image":"https://dn5hzapyfrpio.cloudfront.net/product/597/597286b0-117f-11ed-924b-fb81df6b1480.png","url":"https://www.glowpick.com/products/158483","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.60","reviewCount":70}},"position":7},{"@type":"ListItem","item":{"@type":"Product","name":"8위 플로디카 | 얼웨이즈 유스 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/982/9824a2d0-3d71-11ed-90e3-db6c752b910e.png","url":"https://www.glowpick.com/products/159702","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.62","reviewCount":125}},"position":8},{"@type":"ListItem","item":{"@type":"Product","name":"9위 아우어와이 | 오트 스킨베리어 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/724/72435fa0-4f0a-11ef-b6d3-e70388da0769.jpeg","url":"https://www.glowpick.com/products/174470","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.61","reviewCount":209}},"position":9},{"@type":"ListItem","item":{"@type":"Product","name":"10위 비판톨 | 리플레니싱 데일리 모이스처 페이스 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/60f/60fb48a0-3e63-11ef-8ab0-15fc56ebf8ba.jpeg","url":"https://www.glowpick.com/products/153952","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.59","reviewCount":190}},"position":10},{"@type":"ListItem","item":{"@type":"Product","name":"11위 시메스 | 노르딕 버치 딥 모이스처 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/80f/80fb7870-1461-11ec-a208-3d01ec65d3ca.jpeg","url":"https://www.glowpick.com/products/147865","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.55","reviewCount":261}},"position":11},{"@type":"ListItem","item":{"@type":"Product","name":"12위 일리윤 | 세라마이드 아토 집중 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/352/3524c9d0-8f4a-11ef-b9f1-19409e0192d5.jpeg","url":"https://www.glowpick.com/products/49861","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.47","reviewCount":2665}},"position":12},{"@type":"ListItem","item":{"@type":"Product","name":"13위 바이오더마 | 아토덤 인텐시브 밤","image":"https://dn5hzapyfrpio.cloudfront.net/product/58f/58f66da0-20e4-11ec-98c2-4d15ad70e488.jpeg","url":"https://www.glowpick.com/products/83793","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":670}},"position":13},{"@type":"ListItem","item":{"@type":"Product","name":"14위 누텍스처 | 컴포팅 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/9e6/9e68bf10-67f4-11ee-857b-5f817e901fbb.jpeg","url":"https://www.glowpick.com/products/163151","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.47","reviewCount":654}},"position":14},{"@type":"ListItem","item":{"@type":"Product","name":"15위 닥터지 | 더모이스처 배리어 D 인텐스 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/a3b/a3b0f000-642d-11eb-a25d-3d3b800e98cf.jpeg","url":"https://www.glowpick.com/products/144286","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.51","reviewCount":300}},"position":15},{"@type":"ListItem","item":{"@type":"Product","name":"16위 제로이드 | 인텐시브 크림 엠디","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/20180209/1518137889792.png","url":"https://www.glowpick.com/products/103222","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.54","reviewCount":276}},"position":16},{"@type":"ListItem","item":{"@type":"Product","name":"17위 구달 | 비건 라이스 밀크 보습 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/b0f/b0f40560-0ac5-11ec-9b54-ab93951abab9.jpeg","url":"https://www.glowpick.com/products/150373","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.52","reviewCount":121}},"position":17},{"@type":"ListItem","item":{"@type":"Product","name":"18위 이퀄베리 | 비건 더 깊은 수영장 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/d07/d07e0510-2465-11ed-95a0-07f2d288964c.png","url":"https://www.glowpick.com/products/158960","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.46","reviewCount":120}},"position":18},{"@type":"ListItem","item":{"@type":"Product","name":"19위 쥬스 투 클렌즈 | 비니거 콤부차 비건 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/07f/07f6d420-4088-11ed-af38-e1fdfec0d43a.png","url":"https://www.glowpick.com/products/159845","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.72","reviewCount":61}},"position":19},{"@type":"ListItem","item":{"@type":"Product","name":"20위 제나벨 | PDRN 리쥬비네이팅 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/a90/a9052e10-8bd4-11ed-a870-c92b0697ede1.jpeg","url":"https://www.glowpick.com/products/133772","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.45","reviewCount":266}},"position":20}]}'
data = json.loads(json_data)

cosmetic_no = [
	 '500'
	,'501'
	,'502'
	,'503'
	,'504'
	,'505'
	,'506'
	,'507'
	,'508'
	,'509'
	,'510'
	,'511'
	,'512'
	,'513'
	,'514'
	,'515'
	,'516'
	,'517'
	,'518'
	,'519'
]

for i in range(20):
    url = f'{data["itemListElement"][i]["item"]["url"]}'
    cos_id = cosmetic_no[i]

    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get(url)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 500)")
    time.sleep(2)
    ingredient_div = driver.find_element(By.CSS_SELECTOR, '.info__article.ingredient')
    time.sleep(2)
    ingredient_div.find_element(By.CLASS_NAME, 'info__article__h3__button').click()
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    arr = soup.select('.ingredient__list li')
    # print(arr)
    # arr = ul.find_all('li')

    driver.quit()

    conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
    print(conn.version)

    for idx, li in enumerate(arr, start=1):
        try:
            ewg_test = li.select_one('.item__wrapper__tag').text
            ewg_test2 = ewg_test.replace("\n", "")
            ewg_real = re.sub(' +', ' ', ewg_test2).strip()

            ing_div = li.select_one('.item__wrapper__text')
            ing_test = ing_div.select_one('.item__wrapper__text__kor').text
            ing_test2 = ing_test.replace("\n", "")
            ing_kor = re.sub(' +', ' ', ing_test2).strip()

            ing_eng_test = ing_div.select_one('.item__wrapper__text__eng').text
            ing_eng_test2 = ing_eng_test.replace("\n", "")
            ing_eng = re.sub(' +', ' ', ing_eng_test2).strip()

            ing_desc_test = ing_div.select_one('.item__wrapper__text__desc').text
            ing_desc_test2 = ing_desc_test.replace("\n", "")
            ing_desc = re.sub(' +', ' ', ing_desc_test2).strip()

            if ewg_real == "":
                ewg_real = 0

            print(ewg_real, ing_kor, ing_eng, ing_desc)

            sql = """
                INSERT INTO ingredient(name_kor, name_eng, explain, ewg_rank, index_num, cosmetic_no)
                VALUES(:1, :2, :3, :4, :5, :6)
            """
            cur = conn.cursor()

            # idx를 바인딩 파라미터에 추가
            cur.execute(sql, [ing_kor, ing_eng, ing_desc, ewg_real, idx, cos_id])
        except Exception as e:
            print(str(e))

    conn.commit()
    conn.close()
