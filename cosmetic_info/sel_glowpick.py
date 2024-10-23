import time
import re
import cx_Oracle

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.glowpick.com/products/144830"
cos_num = '286'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
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
        cur.execute(sql, [ing_kor, ing_eng, ing_desc, ewg_real, idx, cos_num])
    except Exception as e:
        print(str(e))

conn.commit()
conn.close()

driver.quit()

# 124 1025 독도로션 할 차례