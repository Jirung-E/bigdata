import json
import webbrowser
import graphdrawer
import wordcloud


keyword = input("keyword: ")
wordInfo = json.load(open(f"result/{keyword}.json", "r", encoding="utf-8"))

graphdrawer.draw(wordInfo)

file_pos = wordcloud.generate(wordInfo, keyword)
webbrowser.open(file_pos)