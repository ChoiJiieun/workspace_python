# -*- coding: utf-8 -*-
import time
import re
import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

json_data = '{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","item":{"@type":"Product","name":"1위 마녀공장 | 퓨어 클렌징 워터 센서티브","image":"https://dn5hzapyfrpio.cloudfront.net/product/026/026d3b90-dcf7-11ee-9627-7f80bf24c2ee.jpeg","url":"https://www.glowpick.com/products/171501","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.66","reviewCount":678}},"position":1},{"@type":"ListItem","item":{"@type":"Product","name":"2위 비오엠 | 에잇 티 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/164/164823e0-1480-11ee-a064-8f0bbb530807.jpeg","url":"https://www.glowpick.com/products/109158","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.64","reviewCount":393}},"position":2},{"@type":"ListItem","item":{"@type":"Product","name":"3위 니들리 | 마일드 미셀라 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/946/946260d0-8a1e-11ec-886f-21278cddeda6.jpeg","url":"https://www.glowpick.com/products/154630","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.61","reviewCount":207}},"position":3},{"@type":"ListItem","item":{"@type":"Product","name":"4위 아임유니 | 마일드 클렌징 워터 이엑스","image":"https://dn5hzapyfrpio.cloudfront.net/product/7c2/7c238d00-c340-11eb-8151-49b6f865b560.jpeg","url":"https://www.glowpick.com/products/126068","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.61","reviewCount":88}},"position":4},{"@type":"ListItem","item":{"@type":"Product","name":"5위 더샘 | 힐링 티 가든 티트리 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/d8d/d8dfea60-a04a-11ec-bb5e-f96d59d299e4.jpeg","url":"https://www.glowpick.com/products/21385","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.39","reviewCount":5465}},"position":5},{"@type":"ListItem","item":{"@type":"Product","name":"6위 로벡틴 | 클린 마린 미셀라 딥 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/eb0/eb0ca8f0-53ba-11eb-9f9d-4ffd996d83ea.jpeg","url":"https://www.glowpick.com/products/143388","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.47","reviewCount":86}},"position":6},{"@type":"ListItem","item":{"@type":"Product","name":"7위 라로슈포제 | 미셀라 클렌징워터 울트라 센시티브","image":"https://dn5hzapyfrpio.cloudfront.net/product/3f0/3f03ac20-6797-11eb-b591-07414105add5.png","url":"https://www.glowpick.com/products/88499","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.36","reviewCount":748}},"position":7},{"@type":"ListItem","item":{"@type":"Product","name":"8위 유리아쥬 | 미셀라 클렌징 워터 센서티브","image":"https://dn5hzapyfrpio.cloudfront.net/product/513/513b0f30-04a6-11ec-abe7-596b71ed79c1.jpeg","url":"https://www.glowpick.com/products/125091","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.44","reviewCount":101}},"position":8},{"@type":"ListItem","item":{"@type":"Product","name":"9위 더샘 | 힐링 티 가든 그린티 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/5d5/5d5418e0-da64-11ec-b462-a987197280d6.jpeg","url":"https://www.glowpick.com/products/12609","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.34","reviewCount":6641}},"position":9},{"@type":"ListItem","item":{"@type":"Product","name":"10위 바이오더마 | 센시비오 H2O","image":"https://dn5hzapyfrpio.cloudfront.net/product/42a/42ac1720-da61-11ec-9e20-e3779f83d594.jpeg","url":"https://www.glowpick.com/products/957","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.30","reviewCount":5042}},"position":10},{"@type":"ListItem","item":{"@type":"Product","name":"11위 가르니에 | 미셀라 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/20160222/1456109347785.jpg","url":"https://www.glowpick.com/products/66001","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.35","reviewCount":350}},"position":11},{"@type":"ListItem","item":{"@type":"Product","name":"12위 바이오더마 | 하이드라비오 H20","image":"https://dn5hzapyfrpio.cloudfront.net/product/fc4/fc4f7160-e9fb-11eb-ae81-9f90f1e03ef5.jpeg","url":"https://www.glowpick.com/products/18290","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.29","reviewCount":728}},"position":12},{"@type":"ListItem","item":{"@type":"Product","name":"13위 셀퓨전씨 | 약산성 패리어 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/ed9/ed9b63a0-f65c-11eb-ac38-adbd80e2789c.jpeg","url":"https://www.glowpick.com/products/149711","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.29","reviewCount":146}},"position":13},{"@type":"ListItem","item":{"@type":"Product","name":"14위 브라운랩 | 애시드 밸런스 페이셜 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/605/60581f20-0e16-11ec-a57c-ef2ca6862863.jpeg","url":"https://www.glowpick.com/products/122325","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.29","reviewCount":82}},"position":14},{"@type":"ListItem","item":{"@type":"Product","name":"15위 코스알엑스 | 약산성 나이아신아마이드 미셀라 클렌징 워터 ","image":"https://dn5hzapyfrpio.cloudfront.net/product/f24/f24c83c0-0c03-11ee-a4f8-ef1561aee92e.jpeg","url":"https://www.glowpick.com/products/166015","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.54","reviewCount":57}},"position":15},{"@type":"ListItem","item":{"@type":"Product","name":"16위 라운드랩 | 1025 독도 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/47e/47e68d80-7851-11ee-b842-db65e1eeb438.jpeg","url":"https://www.glowpick.com/products/127287","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.27","reviewCount":301}},"position":16},{"@type":"ListItem","item":{"@type":"Product","name":"17위 히야 | 마일드 벗 딥 클렌징 워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/657/657426b0-0673-11ed-b6ea-232d81500708.png","url":"https://www.glowpick.com/products/127262","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.68","reviewCount":53}},"position":17},{"@type":"ListItem","item":{"@type":"Product","name":"18위 비페스타 | 클렌징 워터 [브라이트닝]","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/product/20201110/1604991745389.jpg","url":"https://www.glowpick.com/products/1718","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.18","reviewCount":1311}},"position":18},{"@type":"ListItem","item":{"@type":"Product","name":"19위 발레아 | 미셀라 클렌징 워터 포 드라이 스킨","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/20190822/1566451995140.jpg","url":"https://www.glowpick.com/products/124794","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.19","reviewCount":91}},"position":19},{"@type":"ListItem","item":{"@type":"Product","name":"20위 뷰티레시피 | 리틀 머메이드 디스 이즈 프린세스 클렌징워터","image":"https://dn5hzapyfrpio.cloudfront.net/product/e9d/e9d2ba90-12f2-11ec-a1f1-af70ca25143d.jpeg","url":"https://www.glowpick.com/products/46369","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.31","reviewCount":175}},"position":20}]}'
data = json.loads(json_data)

cosmetic_no = [
	 '379'
	,'378'
	,'377'
	,'376'
	,'375'
	,'374'
	,'373'
	,'372'
	,'371'
	,'370'
	,'369'
	,'368'
	,'367'
	,'366'
	,'365'
	,'364'
	,'363'
	,'362'
	,'361'
	,'360'
]

for i in range(20):
    url = f'{data["itemListElement"][i]["item"]["url"]}'
    # url = 'https://www.glowpick.com/products/77236'
    cos_id = cosmetic_no[i]

    driver = webdriver.Chrome()
    driver.implicitly_wait(3) # 브라우저가 켜질 때까지 대기.

    driver.get(url)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.select('.review.review__item')
    # print(article)
    time.sleep(2)
    driver.quit()

    # print(articles[0:10])

    conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
    print(conn.version)

    cosmetic_issues = [
        "성분이 복잡하여 피부에 맞지 않을 수 있음",
        "가격이 비싼 제품이 많아 부담이 됨",
        "유통기한이 짧아 사용하기 어려움",
        "한정판 제품이 많아 구입 기회가 적음",
        "테스트 없이 구매해야 해서 위험함",
        "모든 피부 타입에 적합하지 않아 선택 어려움",
        "성분에 대한 정보가 부족하여 불안함",
        "브랜드마다 색상이 달라 선택이 어려움",
        "기타 제품과의 호환성이 떨어짐",
        "가끔씩 유통기한이 지난 제품이 판매됨",
        "세일 기간이 짧아 놓치기 쉬움",
        "브랜드의 품질이 일관되지 않음",
        "정보가 부족해 적절한 제품 선택 힘듦",
        "대체 제품이 부족하여 다양성 부족",
        "리뷰가 조작된 경우가 많아 신뢰가 안 됨",
        "전문가의 추천이 부족하여 혼란스러움",
        "패키징이 거추장스러워 사용 불편함",
        "인증 마크가 없는 제품들이 많음",
        "소량으로 판매되어 경제적이지 않음",
        "신제품 출시가 잦아 선택의 어려움",
        "피부 타입에 맞는 제품 찾기 힘듦",
        "사용 후 불만족스럽더라도 환불이 어려움",
        "패키지가 환경에 좋지 않은 소재로 제작됨",
        "향이 강해 알레르기 반응을 유발할 수 있음",
        "광고와 실제 제품의 차이가 큼",
        "사용 후 피부 트러블이 생기는 경우가 많음",
        "리뷰와 후기의 신뢰성이 낮음",
        "제품의 사용 방법이 불명확함",
        "제형이 너무 묽거나 너무 끈적임",
        "재구매 시 가격이 오르는 경우가 많음",
        "배송 지연으로 인해 제품을 제때 받지 못함",
        "자주 품절되어 구매하기 어려움",
        "샘플이 부족하여 체험하기 힘듦"
    ]

    memId = [
        "test26@naver.com",
        "test27@naver.com",
        "test28@naver.com",
        "test13@naver.com",
        "test14@naver.com",
        "test15@naver.com",
        "test16@naver.com",
        "test17@naver.com",
        "test18@naver.com",
        "test19@naver.com",
        "test1@naver.com",
        "test20@naver.com",
        "test21@naver.com",
        "test22@naver.com",
        "test23@naver.com",
        "test11@naver.com",
        "test12@naver.com",
        "test24@naver.com",
        "test10@naver.com",
        "test29@naver.com",
        "test30@naver.com",
        "test2@naver.com",
        "test3@naver.com",
        "test4@naver.com",
        "test5@naver.com",
        "test6@naver.com",
        "test7@naver.com",
        "test8@naver.com",
        "test9@naver.com",
        "test25@naver.com"
    ]

    idx = 0

    for article in articles[0:30]:
        try:
            star_div = article.select_one('.review__side-info')
            star_score = star_div.select_one('.stars__rating').text.strip()

            review_div = article.select_one('.review__contents')
            review_text = review_div.select_one('.cutter').text.strip()

            print(star_score, cosmetic_issues[idx])
            print("-" * 50)
            print(review_text)
            print("=" * 60)

            sql = """
                INSERT INTO review(review_no, good_comment, bad_comment, star_score, cosmetic_no, mem_id)
                VALUES(SEQ_REVIEW.NEXTVAL, :1, :2, :3, :4, :5)
            """
            cur = conn.cursor()

            cur.execute(sql, [review_text, cosmetic_issues[idx], star_score, cos_id, memId[idx]])

            idx = idx + 1
        except Exception as e:
            print(str(e))

    conn.commit()
    conn.close()

    driver.quit()