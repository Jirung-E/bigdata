# menuChoice   -> 메뉴
# naverCrawler -> 네이버 크롤링
# apiCrawler   -> 공공 Data 크롤링

import os
import json
import webbrowser

import naverCrawler as nc
import apiCrawler as pc
import graph
import wordcloud


def printMenu():
    print("============== 하고자하는 아래의 내용을 선택 ============== ")
    print("메뉴 목록")
    print("""1. 네이버 크롤링 (블로그, 뉴스, 카페)
2. 공공 Data 크롤링(출입국)
3. 그래프 출력
4. 워드클라우드
5. 종료""")
    print("=========================================================== ")


num = 0

while True:
    printMenu()

    num = int(input("번호 입력: "))

    if num == 1:
        nc.run()
    elif num == 2:
        pc.run()
    elif num == 3:
        graph.showDataList()
        graph.draw()
    elif num == 4:
        wordcloud.showDataList()
        wordcloud.generate()
    elif num == 5:
        print("종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue