str=input()
alpha_lst=list("abcdefghijklmnopqrstuvwxyz")
for i in alpha_lst:
    if i in str:
        print(str.index(i),end=" ")
    else:
        print(-1,end = " ")