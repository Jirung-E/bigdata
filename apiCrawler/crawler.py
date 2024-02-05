import urllib.request
import json


def requestData(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)

    if response.getcode() == 200:
        return response.read().decode('utf-8')
    else:
        return None
    

def makeUrl(yymm, nat_cd, ed_cd) -> str:

    serviceKey = json.loads(open("apiCrawler/key.json", "r", encoding="utf-8").read())["key"]

    url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    param = "?_type=json"
    param += "&serviceKey=" + serviceKey
    param += "&YM=" + str(yymm)
    param += "&NAT_CD=" + str(nat_cd)
    param += "&ED_CD=" + str(ed_cd)

    # print(url + param)

    return url + param