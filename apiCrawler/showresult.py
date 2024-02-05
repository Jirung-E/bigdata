import json

import graphdrawer


if __name__ == "__main__":
    # data = json.loads(open("result.json", "r", encoding="utf-8").read())
    data = json.loads(open("saveDA.json", "r", encoding="utf-8").read())
    print(data)

    counter = {}

    for item in data:
        counter[item["yymm"]] = item["visitCnt"]

    graphdrawer.draw(counter)