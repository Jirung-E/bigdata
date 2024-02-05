import pandas as pd
import json

import apiCrawler.graphdrawer as graphdrawer
import apiCrawler.crawler as crawler



def getNatCd():
    print("검색하고자 하는 나라의 코드 입력")
    print("113: 대만")
    print("170: 태국")
    print("321: 프랑스")
    print("374: 스위스")
    return input("> ")


def getEdCd():
    print("출/입국구분코드 입력")
    print("D: 국민해외관광객")
    print("E: 방한외래관광객")
    ed_cd = input("> ").upper()

    # if ed_cd != "D" and ed_cd != "E":
    #     print("잘못된 입력입니다.")
    #     return

    return ed_cd


def getItem(data):
    if data["response"]["header"]["resultMsg"] == "OK":
        if data["response"]["body"]["items"] != "":
            return data["response"]["body"]["items"]["item"]
    return None


def jsonFileWrite(data):
    with open("./saveDA.json", "w", encoding="utf-8") as outfile:
        jsonFile = json.dumps(data, indent=4, sort_keys=True, 
                             ensure_ascii=False)
        outfile.write(jsonFile)
    
    print("json파일이 생성되었습니다.")


def csvFileWrite(data): 
    cols = ["출입국", "방문객수", "연월"]

    result_df = pd.DataFrame(data, columns=cols)
    result_df.to_csv("./saveDA.csv", index=True, encoding="cp949")

    print("csv파일이 생성되었습니다.")


def crawl():
    yyyy_s = int(input("검색을 시작할 년도 입력(yyyy): "))
    yyyy_e = int(input("검색을 종료할 년도 입력(yyyy): "))

    nat_cd = getNatCd()
    ed_cd = getEdCd()

    counter = {}

    result_json = []
    result_csv = []
    
    for year in range(yyyy_s, yyyy_e + 1):
        print(f"{year}년의 데이터를 불러옵니다.")

        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(year, month)

            url = crawler.makeUrl(yyyymm, nat_cd, ed_cd)
            d = crawler.requestData(url)

            if d is None:
                print("데이터를 불러오지 못했습니다.")
                break

            data = json.loads(d)
            item = getItem(data)

            if item == None:
                print(f"{yyyymm}에 해당하는 데이터가 없습니다.")
                break

            # 국가코드
            natKorNm: str = item["natKorNm"]
            natKorNm = natKorNm.replace(' ', '')

            # 방문자수
            visitCnt = item["num"]

            result_json.append( {
                "natKorNm": natKorNm,
                "visitCnt": visitCnt,
                "yymm": yyyymm
            })

            result_csv.append([natKorNm, visitCnt, yyyymm])

            counter[yyyymm] = int(visitCnt)
            # print(data)

            percentage = (month / 12.0) * 100
            cnt = 40 * month // 12
            progress_bar = "━" * cnt
            remain_bar = "━" * (40 - cnt)
            print(f"\r{percentage:4.1f}%", end="")
            print(f"\033[92m {progress_bar}", end="")
            print(f"\033[91m{remain_bar}", end="")
            print(f"\033[0m", end="")

        print(end="\n")

    return result_json, result_csv

    jsonFileWrite(result_json)
    csvFileWrite(result_csv)


def run():
    json_result, csv_result = crawl()

    json.dump(json_result, 
                open("result/api/data.json", "w", encoding="utf-8"), 
                ensure_ascii=False, 
                indent=4)

    cols = ["출입국", "방문객수", "연월"]
    result_df = pd.DataFrame(csv_result, columns=cols)
    result_df.to_csv("result/api/data.csv", index=True, encoding="utf-8")
    #                                                             cp949
    

# 년도 입력시 해당 년의 월별 관광객 수 출력
def main():
    yyyy_s = int(input("검색을 시작할 년도 입력(yyyy): "))
    yyyy_e = int(input("검색을 종료할 년도 입력(yyyy): "))

    nat_cd = getNatCd()
    ed_cd = getEdCd()

    counter = {}

    result_json = []
    result_csv = []
    
    for year in range(yyyy_s, yyyy_e + 1):
        print(f"{year}년의 데이터를 불러옵니다.")

        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(year, month)

            url = crawler.makeUrl(yyyymm, nat_cd, ed_cd)
            d = crawler.requestData(url)

            if d is None:
                print("데이터를 불러오지 못했습니다.")
                break

            data = json.loads(d)
            item = getItem(data)

            if item == None:
                print(f"{yyyymm}에 해당하는 데이터가 없습니다.")
                break

            # 국가코드
            natKorNm: str = item["natKorNm"]
            natKorNm = natKorNm.replace(' ', '')

            # 방문자수
            visitCnt = item["num"]

            result_json.append( {
                "natKorNm": natKorNm,
                "visitCnt": visitCnt,
                "yymm": yyyymm
            })

            result_csv.append([natKorNm, visitCnt, yyyymm])

            counter[yyyymm] = int(visitCnt)
            # print(data)

            percentage = (month / 12.0) * 100
            cnt = 40 * month // 12
            progress_bar = "━" * cnt
            remain_bar = "━" * (40 - cnt)
            print(f"\r{percentage:4.1f}%", end="")
            print(f"\033[92m {progress_bar}", end="")
            print(f"\033[91m{remain_bar}", end="")
            print(f"\033[0m", end="")

        print(end="\n")

    print(result_json)
    print(result_csv)
    graphdrawer.draw(counter)

    jsonFileWrite(result_json)
    csvFileWrite(result_csv)





if __name__ == "__main__":
    main()