import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager


def draw(data: dict):
    # 폰트 설정
    font_location = "C:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc("font", family=font_name)

    plt.xlabel("연도")
    plt.ylabel("출입국 인원수")

    plt.bar(range(len(data)), data.values(), align="center")
    plt.xticks(range(len(data)), list(data.keys()), rotation=70)
    
    plt.show()