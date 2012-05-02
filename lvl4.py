from urllib.request import *
import re

regexp = re.compile("nothing is ([0-9]*)")

a=str(12345)
while(True):
    url_string = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + a
    print(url_string)
    url = urlopen(url_string)
    url_content = str(url.read())
    a = ''.join(re.findall(regexp, url_content))
    print(url_content)
    print(a)    


