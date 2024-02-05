import os

import pytagcloud


def generate(data, file_name="") -> str:
    # 현재 디렉터리 위치 받아오기
    path = os.getcwd() + "/img/"
    if not os.path.exists(path):
        os.mkdir("img")
    file_pos = path + file_name + "_cloudimg.jpg"
    taglist = pytagcloud.make_tags(data.items(), maxsize=90)
    pytagcloud.create_tag_image(taglist, file_pos, 
                                # size=(1080, 1080),
                                # size=(720, 720),
                                size=(640, 480),
                                layout=4,
                                fontname="koreanbd")
    return file_pos