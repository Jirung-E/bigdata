import os
import json

import naverCrawler as nc
import webbrowser


def showDataList():
    print("데이터 목록")
    print("=====================================")
    for file_name in os.listdir("result/naver"):
        print(" - " + file_name)
    print("=====================================")



def generate():
    print("워드클라우드로 보고싶은 파일명을 입력해주세요")
    keyword = input("json 파일을 선택해주세요: ")
    keyword = keyword.split(".")[0]
    file_name = f"result/naver/{keyword}.json"
    data = json.load(open(file_name, "r", encoding="utf-8"))
    nc.wordcloud.generate(nc.getWordInfo(data), keyword)
    path = os.getcwd() + f"/img/{keyword}_cloudimg.jpg"
    print(path)
    webbrowser.open(path)