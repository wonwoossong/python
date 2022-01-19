word=input()
word=word.upper()
alphabet={}
for i in word:
    if i in alphabet:
        alphabet[i]+=1
    else:
        alphabet[i]=1
answer=0
big=0

for i in alphabet:
    #print(alphabet[i],i)
    if alphabet[i]>big:
        big=alphabet[i]
        answer=i
    elif alphabet[i]==big:
        answer='?'
print(answer)