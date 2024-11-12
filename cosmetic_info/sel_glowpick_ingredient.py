# -*- coding: utf-8 -*-
import time
import re
import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

json_data = '{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","item":{"@type":"Product","name":"1위 시초 | 단델리온 래디언스 세럼 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/e72/e728dca0-f354-11ec-be34-6176c6ef657f.jpeg","url":"https://www.glowpick.com/products/157686","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.74","reviewCount":94}},"position":1},{"@type":"ListItem","item":{"@type":"Product","name":"2위 이니스프리 | 레티놀 시카 흔적 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/869/8696b750-5e9f-11ef-b04c-ddb06322ab03.jpeg","url":"https://www.glowpick.com/products/174969","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.74","reviewCount":235}},"position":2},{"@type":"ListItem","item":{"@type":"Product","name":"3위 잇츠스킨 | 파워 10 포뮬라 엘아이 젤리 패드 감초줄렌","image":"https://dn5hzapyfrpio.cloudfront.net/product/980/9801bfb0-79ac-11ec-bdc7-0d2a9b367bb9.jpeg","url":"https://www.glowpick.com/products/154086","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.60","reviewCount":1680}},"position":3},{"@type":"ListItem","item":{"@type":"Product","name":"4위 잇츠스킨 | 파워 10 포뮬라 엘아이 토너 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/64a/64a4f0b0-d504-11ed-a4a5-839a5e04241c.jpeg","url":"https://www.glowpick.com/products/164238","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.67","reviewCount":311}},"position":4},{"@type":"ListItem","item":{"@type":"Product","name":"5위 셀퓨전씨 | 포스트 알파 쿨링패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/578/57870440-0bf6-11ed-972f-238fd06b7478.jpeg","url":"https://www.glowpick.com/products/158272","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.64","reviewCount":422}},"position":5},{"@type":"ListItem","item":{"@type":"Product","name":"6위 어터 | 스퀘어 팩 패드 모이스처","image":"https://dn5hzapyfrpio.cloudfront.net/product/f12/f1241d00-d1f2-11ed-9e4b-0b5cf4b72039.jpeg","url":"https://www.glowpick.com/products/163246","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.64","reviewCount":214}},"position":6},{"@type":"ListItem","item":{"@type":"Product","name":"7위 이니스프리 | 비타C 그린티 엔자임 잡티 토닝 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/ac5/ac51c1a0-d516-11ee-b566-0f94d0235309.jpeg","url":"https://www.glowpick.com/products/171233","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.71","reviewCount":225}},"position":7},{"@type":"ListItem","item":{"@type":"Product","name":"8위 웰라쥬 | 리얼 히알루로닉 블루 100 토너 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/725/725d6000-728d-11ec-bf1a-3f45b37d9094.jpeg","url":"https://www.glowpick.com/products/153805","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.59","reviewCount":648}},"position":8},{"@type":"ListItem","item":{"@type":"Product","name":"9위 이퀄베리 | 빅 카밍 스위밍풀 토너패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/ce4/ce4fc880-2467-11ed-84b1-438ed58f8c59.png","url":"https://www.glowpick.com/products/158961","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.60","reviewCount":120}},"position":9},{"@type":"ListItem","item":{"@type":"Product","name":"10위 스킨푸드 | 포테이토 마데카소사이드 수딩 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/52c/52c21af0-dd0d-11ee-8995-b3abb6d562b9.jpeg","url":"https://www.glowpick.com/products/171291","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.64","reviewCount":244}},"position":10},{"@type":"ListItem","item":{"@type":"Product","name":"11위 메이크프렘 | 인테카 수딩 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/032/0320eba0-0d4f-11ed-bb4b-cd6d9a639ff1.png","url":"https://www.glowpick.com/products/158332","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.61","reviewCount":254}},"position":11},{"@type":"ListItem","item":{"@type":"Product","name":"12위 바이오힐 보 | 판테셀™ 리페어시카 거즈패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/f0e/f0e61be0-2760-11ee-9d97-3d0481603a6d.jpeg","url":"https://www.glowpick.com/products/166801","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.58","reviewCount":288}},"position":12},{"@type":"ListItem","item":{"@type":"Product","name":"13위 더마펌 | 수딩 리페어 토닝 패드 R4","image":"https://dn5hzapyfrpio.cloudfront.net/product/6ec/6ece7bb0-0c44-11ef-9662-4fa46ae74dbe.jpeg","url":"https://www.glowpick.com/products/172839","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.58","reviewCount":198}},"position":13},{"@type":"ListItem","item":{"@type":"Product","name":"14위 메디힐 | 콜라겐 채움 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/6ec/6ec0bd50-3977-11ed-b894-89ad6ed09a0f.jpeg","url":"https://www.glowpick.com/products/159536","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.58","reviewCount":129}},"position":14},{"@type":"ListItem","item":{"@type":"Product","name":"15위 스킨푸드 | 캐롯 카로틴 카밍 워터 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/533/533472c0-785a-11ee-82a0-977fcb093fe5.jpeg","url":"https://www.glowpick.com/products/137691","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.53","reviewCount":3992}},"position":15},{"@type":"ListItem","item":{"@type":"Product","name":"16위 바이 오디 티디 | 아미노 바하 거즈 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/ca9/ca9b9110-0360-11ed-aab6-7d8754efd32d.png","url":"https://www.glowpick.com/products/158086","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.54","reviewCount":167}},"position":16},{"@type":"ListItem","item":{"@type":"Product","name":"17위 마녀공장 | 히더 카밍 에센스 패드 ","image":"https://dn5hzapyfrpio.cloudfront.net/product/96d/96d0e8c0-7859-11ee-9ff9-c9fe075a60f2.jpeg","url":"https://www.glowpick.com/products/164396","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.50","reviewCount":693}},"position":17},{"@type":"ListItem","item":{"@type":"Product","name":"18위 블리블리 | 밀싹 수분 진정 패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/4e2/4e209a70-6ef0-11ee-b52c-5da613375228.jpeg","url":"https://www.glowpick.com/products/168626","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.66","reviewCount":65}},"position":18},{"@type":"ListItem","item":{"@type":"Product","name":"19위 오어스 | 순한 진정 순진 비건 토너패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/404/4042f1f0-7850-11ee-b842-db65e1eeb438.jpeg","url":"https://www.glowpick.com/products/159941","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":364}},"position":19},{"@type":"ListItem","item":{"@type":"Product","name":"20위 웰스킨 | 센텔라 목화솜 토너패드","image":"https://dn5hzapyfrpio.cloudfront.net/product/b31/b316ca40-7241-11ee-89ca-bb233a5d6df4.png","url":"https://www.glowpick.com/products/134094","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":463}},"position":20}]}'
data = json.loads(json_data)

cosmetic_no = [
	 '600'
	,'601'
	,'602'
	,'603'
	,'604'
	,'605'
	,'606'
	,'607'
	,'608'
	,'609'
	,'610'
	,'611'
	,'612'
	,'613'
	,'614'
	,'615'
	,'616'
	,'617'
	,'618'
	,'619'
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
