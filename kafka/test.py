import redis

data = open("data.txt", "r", encoding="utf-8")
all_dats = []

for i in data.readlines():
    all_dats.append(i.strip())

print(all_dats)

"""

腰腹  23 12
疤痕治疗  27
脚部  6  2
美容技术  8    14
面部   9       15
瘦身  13   18
私密部位 14   19
胸部  15   20
牙部 15   21

眼部  17  22
腿部 30

颈部 10 3
耳部 24 26
除皱  20  29
皮肤 26 25

毛发  27  24

祛斑   28

腿部  30

下巴 29 16

腋下 1 13

腰腹  23 12

臀部 21 9

手臂 18 6
体检 19 8

眉毛 12 5

祛痘  11


额头 22  28
"""
