sentence1=input("Enter first sentence : ")
sentence2=input("Enter second sentence: ")
longSentence=sentence1+sentence2
print("Result of concatenation : ",longSentence)
wordList=list()
while True:
    a=sentence1.find(" ")
    if a==-1:
        wordList.append(sentence1)
        break
    b=0
    word=sentence1[b:a]
    wordList.append(word)
    sentence1=sentence1[a+1:]
    b=a+1
while True:
    a=sentence2.find(" ")
    if a==-1:
        wordList.append(sentence2)
        break
    b=0
    word=sentence2[b:a]
    wordList.append(word)
    sentence2=sentence2[a+1:]
    b=a+1
wordList.sort()
print("Sorted List of words : ")
print(wordList)
dictionary=dict()
for word in wordList:
    dictionary[word]=0
for word in wordList:
    dictionary[word]=dictionary[word]+1
print(dictionary)
