"""
URL的一般格式是： protocol:// hostname[:port] / path / [;parameters][?query]#fragment
基本上是由三部分组成：
协议(HTTP呀，FTP呀~~等等)
主机的IP地址(或者域名)
请求主机资源的具体地址（目录，文件名等）

下面看几个URL例子：

http://xianluomao.sinaapp.com/ga
其中  协议http，  计算机域名xianluomao.sinaapp.com,    请求目录game

http://help.qunar.com/list.ht
其中协议http，         计算机域名help.qunar.com          文件list.html


https://blog.csdn.net/sunon_/article/details/90634253
"""
import urllib.request, chardet, re

page = urllib.request.urlopen('http://photo.sina.com.cn/')  # 打开网页
htmlCode = page.read()  # 获取网页源代码

data = htmlCode.decode('utf-8')  # print(chardet.detect(htmlCode)) #查看编码方式

# print(data) #打印网页源代码
# pageFile = open('pageCode.txt','wb')#以写的方式打开pageCode.txt

# pageFile.write(htmlCode)#写入

# pageFile.close()#开了记得关
reg = r'src="(.+?\.jpg)"'  # 正则表达式
reg_img = re.compile(reg)  # 编译一下，运行更快

imglist = reg_img.findall(data)  # 进行匹配

x = 0
for img in imglist:
    print(img)
    urllib.request.urlretrieve('http://photo.sina.com.cn/', '%s.jpg' % x)
    x += 1
