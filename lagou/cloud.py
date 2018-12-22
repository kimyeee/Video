import random
from PIL import Image
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import numpy as np
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator, random_color_func
from lagou.models import Comment, Lagou

engine = create_engine("mysql+mysqlconnector://root:root@localhost:3306/test", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()
text = ''

comments = session.query(Lagou)
for comment in comments:
    text += comment.description

backgroud_Image = plt.imread('test.png')
alice_mask = np.array(Image.open('test.png'))
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(
    background_color='white',  # 设置背景颜色
    mask=alice_mask,  # 设置背景图片
    prefer_horizontal=0.6,  # 将词横放
    # color_func=lambda *args, **kwargs: (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
    font_path='C:\Windows\Fonts\simsun.ttc',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=200,  # 设置最大现实的字数
    stopwords=set('职位描述岗位职责任职要求岗位要求'),  # 设置停用词
    max_font_size=60,  # 设置字体最大值
    random_state=3  # 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(text)
print('开始加载文本')
# 改变字体颜色
img_colors = ImageColorGenerator(backgroud_Image)
# 字体颜色为背景图片的颜色
wc.recolor(color_func=random_color_func)
# 显示词云图
plt.imshow(wc)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
# 获得模块所在的路径的
d = path.dirname(__file__)
# os.path.join()：  将多个路径组合后返回
wc.to_file(path.join(d, "h11.png"))
print('生成词云成功!')
