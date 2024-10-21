import cx_Oracle

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
for row in rows:
    print(row)



conn.close()