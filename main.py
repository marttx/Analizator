text=input()
rep=text.lower()
punctuation = [".", ",", "!", "?"]
for i in rep:
    if i in punctuation:
        text=rep.replace(i, "")

words=text.split()
word_frequency={}

for j in words:
    if j in word_frequency:
        word_frequency[j]+=1
    else:
        word_frequency[j]=1
print(len(set(words)))
for j, new_count in word_frequency.items():
    print(f"{j}:{new_count}")


