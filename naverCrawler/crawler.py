import urllib.request
import json


client_info = json.load(open("naverCrawler/userinfo.json", "r"))


def requestData(url) -> dict:
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_info["id"])
    request.add_header("X-Naver-Client-Secret", client_info["secret"])

    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        retData = response_body.decode('utf-8')
        return json.loads(retData)
    else:
        return None
    

def makeUrl(keyword, cat) -> str:
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/" + cat
    url += "?query=" + encText
    url += "&start=1&display=100"
    return url