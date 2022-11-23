from starlette.responses import HTMLResponse
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fastapi import FastAPI
# uvicorn main:app --reload
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_coin():
    try:
        coin_list = ["순위", "코인명", "티커", "현재가", "전일대비", "업비트", "바이낸스"]
        thead = ""
        for coin in coin_list:
            thead += f"<th>{coin}</th>"
        URL = "https://www.kimpga.com"
        # 드라이버 설치
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
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
        time.sleep(10)
        # tbody
        table_body = driver.find_element(By.TAG_NAME, 'tbody')
        # tr
        table_row = table_body.find_elements(By.TAG_NAME, 'tr')

        index = 1
        tbody=""
        # 테이블을 돌면서 필요한 정보 추가
        for td in table_row:
            coin_row = td.text
            coin_row_list = coin_row.split("\n")
            tbody += f"""
            <tr>
                <td>{index}
                <td>{coin_row_list[0]}</td>
                <td>{coin_row_list[1]}</td>
                <td>{coin_row_list[-11]}</td>
                <td>{coin_row_list[-7].replace("%", "")}</td>
                <td>{coin_row_list[-2].split()[1].replace("억", "")}</td>
                <td>{coin_row_list[12].replace("조 ", "").replace("억", "")}</td>
            </tr>
            """
            index += 1
        driver.quit()
        return f"""
        <html>
            <head>
                <title>코인 가격</title>
            </head>
            <body>
                <table>
                    <thead>
                        <tr>
                            {thead}
                        </tr>
                    </thead>
                    <tbody>
                            {tbody}
                    </tbody>
                </table>
                
            </body>
        </html>
        """
    except:
        driver.quit()
        return f"""
        <html>
            <head>
                <title>코인 가격</title>
            </head>
            <body>
                <p>
                    크롤링 실패, 다시 시도해주세요
                </p>
                
            </body>
        </html>
        """







