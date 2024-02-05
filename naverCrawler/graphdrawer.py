import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager


def draw(data):
    # 폰트 설정
    font_location = "C:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc("font", family=font_name)

    plt.xlabel("주요 단어")
    plt.ylabel("빈도수")
    
    sorted_dict = dict(sorted(data.items(), 
                              key = lambda x: x[1], 
                              reverse = True))

    plt.bar(range(len(sorted_dict)), sorted_dict.values(), align="center")
    plt.xticks(range(len(sorted_dict)), list(sorted_dict.keys()), rotation=70)
    
    plt.show()