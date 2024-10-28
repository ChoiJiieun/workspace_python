import time
import re
import cx_Oracle
import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

json_data = '{"@context":"https://schema.org","@type":"ItemList","itemListElement":[{"@type":"ListItem","item":{"@type":"Product","name":"1위 주미소 | 포어 퓨리파잉 살리실산 포밍 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/d7b/d7b964c0-2790-11ef-b74b-79316ef070e9.jpeg","url":"https://www.glowpick.com/products/170360","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.72","reviewCount":205}},"position":1},{"@type":"ListItem","item":{"@type":"Product","name":"2위 닥터릴리프 | 디에이씨투 카렌듈라 카밍 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/cdd/cddb3ea0-0089-11ec-8d15-f5a4c111a76c.jpeg","url":"https://www.glowpick.com/products/150003","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.59","reviewCount":322}},"position":2},{"@type":"ListItem","item":{"@type":"Product","name":"3위 라프텔 | 페이셜 클렌저 딥클린","image":"https://dn5hzapyfrpio.cloudfront.net/product/4c0/4c04cbd0-8809-11ee-a267-8dd48385bbd2.jpeg","url":"https://www.glowpick.com/products/169300","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.58","reviewCount":145}},"position":3},{"@type":"ListItem","item":{"@type":"Product","name":"4위 휴캄 | 어성초 진정 클린 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/c73/c732ff90-a8e8-11ec-9bd8-c5044ba0ab0c.jpeg","url":"https://www.glowpick.com/products/147177","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.60","reviewCount":159}},"position":4},{"@type":"ListItem","item":{"@type":"Product","name":"5위 토르홉 | 카모스 블랙 소금거품 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/9bb/9bbde300-60fd-11ef-b954-67bd70304544.jpeg","url":"https://www.glowpick.com/products/175078","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.67","reviewCount":67}},"position":5},{"@type":"ListItem","item":{"@type":"Product","name":"6위 일루미엘 | AC 솔루션 폼클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/736/736545b0-b40f-11ee-a054-3f67d73ea0d5.jpeg","url":"https://www.glowpick.com/products/170347","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.55","reviewCount":106}},"position":6},{"@type":"ListItem","item":{"@type":"Product","name":"7위 포이유이 | 딥 포어 펀클렌징 약산성 발효 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/d72/d72f1290-189a-11ed-b7df-6beca1cf3622.png","url":"https://www.glowpick.com/products/158650","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.57","reviewCount":115}},"position":7},{"@type":"ListItem","item":{"@type":"Product","name":"8위 와이비케이 | 릴리프 하이드레이션 라이트 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/5f6/5f6cb940-46e5-11ee-81cb-0f28cefa70d2.jpeg","url":"https://www.glowpick.com/products/167618","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.74","reviewCount":62}},"position":8},{"@type":"ListItem","item":{"@type":"Product","name":"9위 프리메라 | 오가니언스 BR 소프트 필링 투 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/b2a/b2ad0370-fea7-11ed-82ee-7fedbc034a57.jpeg","url":"https://www.glowpick.com/products/164756","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.52","reviewCount":148}},"position":9},{"@type":"ListItem","item":{"@type":"Product","name":"10위 토코보 | 코코넛 클레이 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/ddd/ddd75620-9ac3-11ec-84e0-b7c2ecdee61c.jpeg","url":"https://www.glowpick.com/products/155201","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":202}},"position":10},{"@type":"ListItem","item":{"@type":"Product","name":"11위 쥬스 투 클렌즈 | 레스 레스 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/1e4/1e4e7880-7850-11ee-b842-db65e1eeb438.jpeg","url":"https://www.glowpick.com/products/152829","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":263}},"position":11},{"@type":"ListItem","item":{"@type":"Product","name":"12위 토리든 | 다이브인 저분자 히알루론산 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/15a/15ab92c0-3405-11ed-acac-8da0e32203af.jpeg","url":"https://www.glowpick.com/products/159365","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.55","reviewCount":224}},"position":12},{"@type":"ListItem","item":{"@type":"Product","name":"13위 이니스프리 | 화산송이 바하 모공 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/91d/91d7e300-bd88-11ed-b46b-d9632ba1c8bb.jpeg","url":"https://www.glowpick.com/products/162105","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.52","reviewCount":201}},"position":13},{"@type":"ListItem","item":{"@type":"Product","name":"14위 블랑네이처 | 아크네 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/6d1/6d1a61d0-24ff-11ee-89e2-8f2524962d30.jpeg","url":"https://www.glowpick.com/products/165650","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.48","reviewCount":254}},"position":14},{"@type":"ListItem","item":{"@type":"Product","name":"15위 듀이트리 | AC 컨트롤 딥 그린 카밍 트러블 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/cd0/cd079420-068f-11ee-a168-1156b8df51df.jpeg","url":"https://www.glowpick.com/products/165909","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":76}},"position":15},{"@type":"ListItem","item":{"@type":"Product","name":"16위 브이앤코 | 브이 코어텍틴 클렌징폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/dde/ddeb7df0-480f-11ec-aee9-87d52af0404f.jpeg","url":"https://www.glowpick.com/products/152489","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.47","reviewCount":121}},"position":16},{"@type":"ListItem","item":{"@type":"Product","name":"17위 아크네스 | 더마 릴리프 모이스처 폼클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/9b2/9b252a60-8a59-11ed-934c-a5f7267a0f0b.jpeg","url":"https://www.glowpick.com/products/161806","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":113}},"position":17},{"@type":"ListItem","item":{"@type":"Product","name":"18위 메디필 | 그린 시카 콜라겐 클리어 2.0","image":"https://dn5hzapyfrpio.cloudfront.net/product/911/91163290-ae93-11ed-8f8a-317bf280196c.jpeg","url":"https://www.glowpick.com/products/163018","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.46","reviewCount":157}},"position":18},{"@type":"ListItem","item":{"@type":"Product","name":"19위 에스트라 | 테라크네365 클리어 딥 클렌징 폼","image":"https://dn5hzapyfrpio.cloudfront.net/product/424/424b9660-d9a3-11ed-8cc7-35b762171ff0.jpeg","url":"https://www.glowpick.com/products/147534","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.43","reviewCount":663}},"position":19},{"@type":"ListItem","item":{"@type":"Product","name":"20위 코이 | 플로우 에센스 폼 클렌저","image":"https://dn5hzapyfrpio.cloudfront.net/product/e12/e12381a0-a756-11ed-b852-933e07cf2550.jpeg","url":"https://www.glowpick.com/products/152394","aggregateRating":{"@type":"AggregateRating","ratingValue":"4.49","reviewCount":103}},"position":20}]}'
data = json.loads(json_data)

url = f'{data["itemListElement"][19]["item"]["url"]}'

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 브라우저가 켜질 때까지 대기.

driver.get(url)
time.sleep(1)
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

        cur.execute(sql, [review_text, cosmetic_issues[idx], star_score, 359, memId[idx]])

        idx = idx + 1
    except Exception as e:
        print(str(e))

conn.commit()
conn.close()

driver.quit()