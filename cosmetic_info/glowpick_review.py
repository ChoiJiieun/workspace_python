# -*- coding: utf-8 -*-
import time
import re
import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

json_data = '{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","item":{"@type":"Product","name":"1위 어글리 러블리 | 멜론 수분크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/660/660d2ee0-5df7-11ef-a50d-4519fa071bd0.jpeg","url":"https://www.glowpick.com/products/174947","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.69","reviewCount":85}},"position":1},{"@type":"ListItem","item":{"@type":"Product","name":"2위 큐어코드 | 수딩 릴리프 젤","image":"https://dn5hzapyfrpio.cloudfront.net/product/83c/83c3c0f0-c787-11ed-8a0f-332a1b31f564.jpeg","url":"https://www.glowpick.com/products/152936","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.57","reviewCount":1003}},"position":2},{"@type":"ListItem","item":{"@type":"Product","name":"3위 주미소 | 워터풀 히알루론산 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/153/153c1c00-545c-11ef-ab15-d1201946d200.jpeg","url":"https://www.glowpick.com/products/147861","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.56","reviewCount":1136}},"position":3},{"@type":"ListItem","item":{"@type":"Product","name":"4위 백아율 | 모이스처 밸런싱 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/90a/90a160c0-21f6-11ed-9c94-ab05ebe52a8f.png","url":"https://www.glowpick.com/products/158842","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.63","reviewCount":329}},"position":4},{"@type":"ListItem","item":{"@type":"Product","name":"5위 스킨푸드 | 블루 캐모마일 히알루로닉 수분 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/82a/82af2550-0107-11ef-9a9c-1decd759a7c4.jpeg","url":"https://www.glowpick.com/products/172566","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.62","reviewCount":181}},"position":5},{"@type":"ListItem","item":{"@type":"Product","name":"6위 웰라쥬 | 리얼 히알루로닉 100 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/4ed/4eded440-785a-11ee-9c0c-8f13c8545ead.jpeg","url":"https://www.glowpick.com/products/161507","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.54","reviewCount":658}},"position":6},{"@type":"ListItem","item":{"@type":"Product","name":"7위 에스트라 | 아토베리어 365 하이드로 수딩크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/65a/65a2f050-e040-11ee-a311-917026a70323.jpeg","url":"https://www.glowpick.com/products/147139","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.48","reviewCount":933}},"position":7},{"@type":"ListItem","item":{"@type":"Product","name":"8위 퓨어트리 | 모이스트페어™ 수분 젤크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/f85/f8557e50-ea27-11ed-b802-57ab563c58f9.jpeg","url":"https://www.glowpick.com/products/165035","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.51","reviewCount":107}},"position":8},{"@type":"ListItem","item":{"@type":"Product","name":"9위 메이크프렘 | 세이프 미 릴리프 워터리 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/0dc/0dcee4a0-d93c-11eb-859b-f54486df86fe.jpeg","url":"https://www.glowpick.com/products/148679","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.53","reviewCount":215}},"position":9},{"@type":"ListItem","item":{"@type":"Product","name":"10위 더페이스샵 | 올티밋 히알루로닉 스쿠알란 1% 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/a25/a25b21a0-2fa7-11ef-a383-d17651385560.jpeg","url":"https://www.glowpick.com/products/173626","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.51","reviewCount":97}},"position":10},{"@type":"ListItem","item":{"@type":"Product","name":"11위 오아이브 | 턴오버 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/2fd/2fdf9d60-6e91-11ec-9aad-c33b288806ca.jpeg","url":"https://www.glowpick.com/products/150386","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.48","reviewCount":124}},"position":11},{"@type":"ListItem","item":{"@type":"Product","name":"12위 잇츠스킨 | 파워 10 포뮬라 엘아이 수딩 젤 크림 감초줄렌","image":"https://dn5hzapyfrpio.cloudfront.net/product/fba/fba62820-fdd3-11ec-ae4d-57daf0824ff2.jpeg","url":"https://www.glowpick.com/products/157909","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.51","reviewCount":143}},"position":12},{"@type":"ListItem","item":{"@type":"Product","name":"13위 아비브 | 수분초 히알루론 크림 하이드레이팅 팟","image":"https://dn5hzapyfrpio.cloudfront.net/product/7ec/7ec0bd10-f852-11ec-a990-01d119690e0a.jpeg","url":"https://www.glowpick.com/products/157802","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":114}},"position":13},{"@type":"ListItem","item":{"@type":"Product","name":"14위 투비건 | 컬러 푸드 시리즈 그린 글로우업 크림 ","image":"https://dn5hzapyfrpio.cloudfront.net/product/ac8/ac86f650-ee81-11eb-a078-b7d9c923bed1.jpeg","url":"https://www.glowpick.com/products/149310","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.46","reviewCount":252}},"position":14},{"@type":"ListItem","item":{"@type":"Product","name":"15위 아이소이 | 모이스춰 닥터 크림 (장수진수분크림)","image":"https://dn5hzapyfrpio.cloudfront.net/product/564/56498970-d4ae-11eb-a083-3f906d6382b4.jpeg","url":"https://www.glowpick.com/products/148513","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.40","reviewCount":698}},"position":15},{"@type":"ListItem","item":{"@type":"Product","name":"16위 코스톡 | 톡톡 수딩 아쿠아 크림","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/product/20200820/1597884882764.jpg","url":"https://www.glowpick.com/products/139205","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.41","reviewCount":261}},"position":16},{"@type":"ListItem","item":{"@type":"Product","name":"17위 토리든 | 다이브인 저분자 히알루론산 수딩 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/18d/18d1f370-7458-11ed-b309-a373581b56f8.jpeg","url":"https://www.glowpick.com/products/148073","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.46","reviewCount":566}},"position":17},{"@type":"ListItem","item":{"@type":"Product","name":"18위 아크웰 | 리얼 아쿠아 밸런싱 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/00c/00c952a0-e795-11ec-87eb-b794c6fb9301.jpeg","url":"https://www.glowpick.com/products/141520","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":100}},"position":18},{"@type":"ListItem","item":{"@type":"Product","name":"19위 닥터지 | 레드 블레미쉬 시카 수딩 크림","image":"https://dn5hzapyfrpio.cloudfront.net/product/b84/b840a5a0-d8a5-11eb-a408-65581bf06388.jpeg","url":"https://www.glowpick.com/products/148665","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.41","reviewCount":1055}},"position":19},{"@type":"ListItem","item":{"@type":"Product","name":"20위 에스네이처 | 아쿠아 스쿠알란 수분크림","image":"https://dn5hzapyfrpio.cloudfront.net/home/glowmee/upload/product/20201008/1602125956906.jpg","url":"https://www.glowpick.com/products/87348","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.40","reviewCount":764}},"position":20}]}'
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
        "test25@naver.com",
        "allergy@naver.com",
        "jjin@naver.com",
        "profilenew@naver.com",
        "swlee",
        "spring@naver.com"
    ]

    idx = 0

    for article in articles[0:34]:
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