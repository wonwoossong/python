python="Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","java"))

index=python.index("n")#몇번째 위치에 있는지
print(index)#인덱스 =5
index=python.index("n",index+1)#스타트 위치가 6이야 5+1
print(index)

print(python.find("Java"))#이거는 -1
# print(python.index("java"))#이거는 오류
print("hi")

print(python.count("n"))