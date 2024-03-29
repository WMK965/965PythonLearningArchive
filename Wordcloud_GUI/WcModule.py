import jieba
import wordcloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

size = None  # 210
maxword = None  # 75
font = None  # "AdobeHeitiStd-Regular.otf"
file = None  # "../resources/111.txt"
mask = None  # "../resources/mask.png"
stopwords = None  # {'王勃', '一'}
codec = None


def generate(size, maxword, font, file, mask, stopwords, codec):
    raw_data = open(file, encoding=f"{codec}").read()
    ls = jieba.lcut(raw_data)
    for word in ls:
        if len(word) == 1:
            ls.remove(word)
        else:
            continue
    text = ' '.join(ls)
    open(file, encoding="utf-8").close()
    mask = np.array(Image.open(mask))
    wc = wordcloud.WordCloud(font_path=font,
                             mask=mask,
                             background_color='white',
                             max_font_size=size,
                             max_words=maxword,
                             stopwords=stopwords)
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()


#generate(210, 75, "AdobeHeitiStd-Regular.otf", "C:\\Users\\965\\Builds\PythonLearning\\resources\\333.txt", "../resources/mask.png", {'王勃', '一'})
