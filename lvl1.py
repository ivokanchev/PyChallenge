import webbrowser

initial = "abcdefghijklmnopqrstuvwxyz"
output = "cdefghijklmnopqrstuvwsyzab"
cipher = str.maketrans(initial, output)
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

text.translate(cipher)
text = "map"
url = 'http://www.pythonchallenge.com/pc/def/' + text.translate(cipher) + '.html'
webbrowser.open(url)
