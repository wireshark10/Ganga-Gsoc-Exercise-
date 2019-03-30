import os
import re
directory = '/home/wireshark10/Desktop/text'
wordcount={}



for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        f = open(filename)
        for word in f.read().split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

        f.close()
        word="the"

        print word, wordcount[word]
        wordcount[word]=0
