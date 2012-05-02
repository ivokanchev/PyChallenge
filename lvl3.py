from urllib.request import *
import re
import webbrowser

regexp = re.compile("[^A-Z][A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]")
url = urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
webbrowser.open('http://www.pythonchallenge.com/pc/def/' +
                ''.join(re.findall(regexp, str(url.read()))) + '.php')



        
