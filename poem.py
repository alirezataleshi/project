
words= set(open("poem.txt", errors="ignore" ))

print(words)
words2=set(open("poem.txt", errors="ignore").read().split())
print(words2)
print(len(words2))
