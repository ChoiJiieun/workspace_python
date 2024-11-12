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