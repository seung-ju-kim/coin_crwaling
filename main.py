from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_coin():
    try:
        URL = "https://www.kimpga.com"
        column_list = ["순위", "코인명", "티커 ", "현재가", "전일대비", "업비트", "바이낸스"]

        # 드라이버 설치
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(5)

        # 접속
        driver.get(URL)
        time.sleep(1)
        # 개인화 설정 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div[1]/span').click()
        time.sleep(1)
        # 해외 거래소에 있는 자산만 보기 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div[2]/div/div/div[2]/div[4]/span').click()
        time.sleep(1)
        # 기준거래소 해외 마켓 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div[5]/div[2]/div/div[1]').click()
        time.sleep(1)
        # 바이낸스 선물 USDS-M 마켓 클릭
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div[5]/div[2]/div/div[2]/ul/li[3]').click()
        time.sleep(3)
        # tbody
        table_body = driver.find_element(By.TAG_NAME, 'tbody')
        # tr
        table_row = table_body.find_elements(By.TAG_NAME, 'tr')

        index = 1
        result = []
        # 테이블을 돌면서 필요한 정보 csv에 추가 후 파일로 저장
        for td in table_row:
            data = []
            coin_row = td.text
            coin_row_list = coin_row.split("\n")
            time.sleep(1)
            data.append(index)
            data.append(coin_row_list[0])
            data.append(coin_row_list[1])
            data.append(coin_row_list[-11])
            data.append(coin_row_list[-7].replace("%", ""))
            data.append(coin_row_list[-2].split()[1].replace("억", ""))
            data.append(coin_row_list[12].replace("조 ", "").replace("억", ""))
            result.append(data)
            index += 1

        driver.quit()
        return {"success": True, "data": result}
    except:
        driver.quit()
        return {"success": False, "data": []}







