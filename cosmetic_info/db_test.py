import cx_Oracle
import datetime
import requests

#1. 오라클에서 테이블을 생성합니다.
conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
print(conn.version) #잘 연결 됐는지 확인...
#2. 테이블 설정
sql = """
    SELECT *
    FROM cosmetic
"""
cur = conn.cursor()
rows = cur.execute(sql)
# 3. 테이블에 데이터 불러와 추가하기
# for i in range(1, 46):
#     url = f"https://m.stock.naver.com/api/stocks/marketValue/KOSPI?page={i}&pageSize=50"
#     res = requests.get(url)
#     if res.status_code == 200:
#         data = res.json()
#         arr = data['stocks']
#         for v in arr:
#             data = {'itemCode': v['itemCode'], 'stockName': v['stockName']
#                                             , 'closePrice': v['closePrice'].replace(',','')
#                                             , 'create_dt': datetime.datetime.now()}
#             cur.execute("INSERT INTO stocks VALUES(:itemCode, :stockName, :closePrice, :create_dt)", data)
#         conn.commit()
conn.close()