word = input().upper()
word_set = list(set(word))
wordCntList = list()
maxCnt = 0

for c in word_set:
    wordCntList.append(word.count(c))

maxCnt = max(wordCntList)
if(wordCntList.count(maxCnt) >1 ):
    print("?")
else:
    index = wordCntList.index(maxCnt)
    print(word_set[index])
    
