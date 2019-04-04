#THIS SCRIPT IS CONVERTED TO AN EXECUTABLE THAT GANGA WILL TAKE AS AN APPLICATION .CONVERTED TO AN EXECUTABLE USING Pyinstaller,and is finally passed in the job script.


import os
import re
import sys
wordcount={}
filename=sys.argv[1]
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
