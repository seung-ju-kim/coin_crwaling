# coin_crwaling
kimpga.com에서 제공하는 코인 시세를 크롤링합니다.

kimpa.com에 접속하여 개인화 설정 > 해외 거래소에 있는 자산만 보기 > 기준 거래소 해외 마켓 > 바이낸스 선물 USDS-M 마켓 클릭 후
테이블에 뿌려지는 업비트 거래액 기준 내림차순으로 데이터를 스크래핑한다.
순위, 코인명, 티커, 현재가, 전일대비, 업비트 거래량, 바이낸스 거래량을 가져오기 위해 tbody태그 중 tr 태그를 찾아 반복문을 돌며 FAST API의 HTMLResponse를 통해 테이블로 결과를 반환한다.
