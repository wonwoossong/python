#리스트 만들어서 index 마다 * num 해주면 되지 않을까?
case=int(input())

while case>0:
    N,S=input().split(" ")
    N=int(N)  
    S=list(S)
    for i in range(len(S)):
        print(N*S[i],end="")
    print()
    case-=1