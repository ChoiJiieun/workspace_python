import cx_Oracle

# Oracle 데이터베이스 연결 설정
conn = cx_Oracle.connect("project2", "oracle", "localhost:1521/xe")
cursor = conn.cursor()

# cosmetic 테이블에서 해시태그를 포함한 모든 데이터 가져오기
cursor.execute("SELECT cosmetic_no, hashtag FROM cosmetic")
cosmetics = cursor.fetchall()

# 태그 및 관계 데이터를 삽입
for cosmetic_no, hashtags in cosmetics:
    if hashtags:
        tags = set(hashtags.split())  # 공백으로 해시태그 분리 및 중복 제거

        for tag_name in tags:
            # tag 테이블에 태그 삽입 (중복 방지)
            cursor.execute("SELECT tag_no FROM tag WHERE tag_name = :tag_name", {"tag_name": tag_name})
            tag_row = cursor.fetchone()

            if tag_row is None:
                cursor.execute("INSERT INTO tag (tag_no, tag_name) VALUES (tag_seq.NEXTVAL, :tag_name)", {"tag_name": tag_name})
                conn.commit()
                cursor.execute("SELECT tag_no FROM tag WHERE tag_name = :tag_name", {"tag_name": tag_name})
                tag_row = cursor.fetchone()

            tag_no = tag_row[0]

            # relation 테이블에 cosmetic_no와 tag_no의 관계 추가
            cursor.execute("""
                MERGE INTO relation r
                USING dual
                ON (r.cosmetic_no = :cosmetic_no AND r.tag_no = :tag_no)
                WHEN NOT MATCHED THEN
                    INSERT (cosmetic_no, tag_no) VALUES (:cosmetic_no, :tag_no)
            """, {"cosmetic_no": cosmetic_no, "tag_no": tag_no})

conn.commit()
cursor.close()
conn.close()
