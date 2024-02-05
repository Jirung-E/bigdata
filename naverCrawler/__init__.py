import re
import json
import webbrowser
from konlpy.tag import Okt
from collections import Counter

import naverCrawler.graphdrawer as graphdrawer
import naverCrawler.wordcloud as wordcloud
import naverCrawler.crawler as crawler


def getSearchCat():
    print("블로그: 1   뉴스: 2   카페: 3")
    cat = input("> ")
    if cat == '1':
        print("블로그로 검색합니다.")
        cat = "blog"
    elif cat == '2':
        print("뉴스로 검색합니다.")
        cat = "news"
    elif cat == '3':
        print("카페로 검색합니다.")
        cat = "cafearticle"
    else:
        print("잘못된 입력입니다. 블로그로 검색합니다.")
        cat = "blog"
    return cat
    

def naverCrawling(keyword):
    cat = getSearchCat()
    url = crawler.makeUrl(keyword, cat)
    print("url: ", url)
    return crawler.requestData(url)


def getNouns(data):
    message = ""
    for item in data:
        if "description" in item.keys():
            message += re.sub(r"[^\w]", " ", item["description"]) + " "

    nlp = Okt()
    return nlp.nouns(message)


def filterData(data):
    resultD = []
    for item in data["items"]: 
        resultD.append({
            "description": item["description"]
        })
    return resultD


def crawl():
    keyword = input("검색할 단어 입력: ")
    data = naverCrawling(keyword)

    if data is not None:
        print("검색된 개수: ", data["total"])

        data = filterData(data)
        return keyword, data

        nouns = getNouns(data)
        counters = Counter(nouns)
        
        print("nouns: ", nouns)
        print("counters: ", counters)

        wordInfo = {}
        for tag, count in counters.most_common(100):
            if len(str(tag)) > 1:
                wordInfo[tag] = count

        return keyword, wordInfo

        json.dump(wordInfo, 
                open(f"result/{keyword}.json", "w", encoding="utf-8"), 
                ensure_ascii=False, indent=4)
        
    return keyword, None


def getWordInfo(data):
    nouns = getNouns(data)
    counters = Counter(nouns)
    
    print("nouns: ", nouns)
    print("counters: ", counters)

    wordInfo = {}
    for tag, count in counters.most_common(100):
        if len(str(tag)) > 1:
            wordInfo[tag] = count

    return wordInfo


def run():
    keyword, data = crawl()
    json.dump(data, 
                open(f"result/naver/{keyword}.json", "w", encoding="utf-8"), 
                ensure_ascii=False, 
                indent=4)


def main():
    keyword = input("검색할 단어 입력: ")
    data = naverCrawling(keyword)

    if data is not None:
        print("검색된 개수: ", data["total"])

        nouns = getNouns(filterData(data))
        counters = Counter(nouns)
        
        print("nouns: ", nouns)
        print("counters: ", counters)

        wordInfo = {}
        for tag, count in counters.most_common(100):
            if len(str(tag)) > 1:
                wordInfo[tag] = count
        print("wordInfo: ", wordInfo)

        graphdrawer.draw(wordInfo)

        json.dump(wordInfo, 
                open(f"result/{keyword}.json", "w", encoding="utf-8"), 
                ensure_ascii=False, indent=4)

        file_pos = wordcloud.generate(wordInfo, keyword)
        webbrowser.open(file_pos)


if __name__ == "__main__":
    main()