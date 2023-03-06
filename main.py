import re
import jieba
import zhon.hanzi
import wordcloud

filename = "C:/Users/shiye/Desktop/python/weibo.txt"  # 设置文件

punc = zhon.hanzi.punctuation  # 要去除的中文标点符号

with open('C:/Users/shiye/Desktop/python/cn_stopwords.txt', encoding="UTF-8") as fp:
    words = fp.read()

# 读入文件
with open(filename, encoding="utf-8") as fp:
    text = fp.read()

text = re.sub('[^\u4e00-\u9fa5]+', '', text)

ls = jieba.lcut(text)  # 分词

# 统计词频
counts = {}
for i in ls:
    if len(i) > 1:
        counts[i] = counts.get(i, 0) + 1

words_1 = ''.join(counts.keys())

for word in words:  # 去掉停用词
    counts.pop(word, 0)

ls1 = sorted(counts.items(), key=lambda x: x[1], reverse=True)  # 词频排序

c = wordcloud.WordCloud(font_path="C:/Users/shiye/Desktop/simhei.ttf", width=800, height=600, min_font_size=30,
                        max_font_size=300, max_words=100)
c.generate(" ".join(jieba.lcut(words_1)))
c.to_file("C:/Users/shiye/Desktop/python/pywordcloud.png")


