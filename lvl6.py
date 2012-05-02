import zipfile
import re

regexp = re.compile("nothing is ([0-9]*)")

file_name = '90052.txt'
with zipfile.ZipFile('channel.zip','a') as archive:
    while(True):
        current_file = archive.read(file_name)
        if re.findall(regexp,str(current_file))==[]:
            break
        file_name = re.findall(regexp,str(current_file))[0] + '.txt'
        print(''.join(chr(ord(archive.getinfo(file_name).comment))), end='')     
