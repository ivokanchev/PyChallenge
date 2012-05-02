import pickle
from urllib import request

url = request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
unp = pickle.Unpickler(url)
data = unp.load()

print(*[''.join([tpl[0] * tpl[1] for tpl in row]) for row in data], sep="\n")
