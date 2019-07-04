
words= set(open("poem.txt", errors="ignore" ))

print(words)
words2=set(open("poem.txt", errors="ignore").read().split())
print(words2)
print(len(words2))

file=open("poem.txt", "r", errors="ignore")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print(k, v)