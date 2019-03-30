
import re
#text from cern.pdf is copied and a new file is created named as cerntext.txt
logfile = open("/home/wireshark10/Desktop/Cerntext.txt", "r")

wordcount={}
for word in logfile.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
# print only the count for my_word only
my_word="the"
print my_word, wordcount[my_word]
