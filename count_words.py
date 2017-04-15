import re
from pprint import pprint
para = input('Enter a paragraph: ').rstrip() + ' '
words = []
f = 0

while para != '':
    i = para.index(' ')
    if re.match('^[A-Za-z]+[^0-9A-Za-z]', para[:i]):
        words.append(para[:i-1].lower())
        para = para[i+1:]
    elif re.match('^[A-Za-z]+', para[:i]):
        words.append(para[:i].lower())
        para = para[i+1:]
    else:
        f = 1
        break

if f:
    print('Invalid input.')
else:
    wordfreq = {}
    for i in words:
        wordfreq[i] = words.count(i)
    pprint(wordfreq)

