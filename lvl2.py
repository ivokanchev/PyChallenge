from urllib.request import *
from html.parser import HTMLParser
import collections

def printChars(ls):
    print([charTuple[0] for charTuple in ls if charTuple[1] < 5])

class MyParser(HTMLParser):
    def handle_comment(self, data):    
            printChars(collections.Counter(data).most_common())

parser = MyParser()
url = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
parser.feed(str(url.read()))


        
