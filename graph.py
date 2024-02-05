import os
import json
import naverCrawler as nc
import apiCrawler as pc


def showDataList():
    print("데이터 목록")
    print("=====================================")
    print(" naver:")
    for file_name in os.listdir("result/naver"):
        print(" ├─ " + file_name)
    print(" api:")
    for file_name in os.listdir("result/api"):
        print(" ├─ " + file_name)
    print("=====================================")


def draw():
    print("그래프로 보고싶은 파일명을 입력해주세요")

    file_name = input("json 파일을 선택해주세요: ")

    file_name = file_name.split(".")[0]
    file_name = f"result/{file_name}.json"
    # print(file_name)

    data = json.load(open(file_name, "r", encoding="utf-8"))

    cat = file_name.split("/")[1]
    
    if cat == "naver":
        nc.graphdrawer.draw(nc.getWordInfo(data))
    elif cat == "api":
        pc.graphdrawer.draw(data)
    else:
        print("잘못된 입력입니다.")