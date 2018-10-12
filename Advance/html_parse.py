import urllib.request
from html.parser import HTMLParser

url = 'https://www.yahoo.co.jp/'


#HTML文字列の取得
# htmldata = urllib.request.urlopen(url)
# print(htmldata.read().decode('UTF-8'))
#
# htmldata.close()

#ヘッダー情報の設定

# opener = urllib.request.build_opener()
# opener.addheaders = [
#     (
#         'User-agent',
#         'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)'
#     )
# ]
#
# htmldata = opener.open(url)
# print(htmldata.read().decode('UTF-8'))
#
# htmldata.close()
# opener.close()

#タグ情報の取得

class TestParser(HTMLParser):

    def handle_starttag(self, tagname, attribute):
        if tagname.lower() == 'a':
            for i in attribute:
                if i[0].lower() == 'href':
                    print(i[1])


htmldata = urllib.request.urlopen(url)

parser = TestParser()
parser.feed(htmldata.read().decode('UTF-8'))

parser.close()
htmldata.close()
