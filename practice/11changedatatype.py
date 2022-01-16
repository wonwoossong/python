# #자료구조의 변경 
# menu={"커피","우유","주스"}
# print(menu,type(menu))

# menu=list(menu)
# print(menu,type(menu))

# menu=tuple(menu)
# print(menu,type(menu))

# menu=set(menu)#첫글짜가 키로 가고 두번쩨가 벨류로 간다 
# print(menu,type(menu))
# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst) # 섞는다
# a=sample(lst,1)
# a=set(a)
# lst=set(lst)
# lst=lst-a
# #해결하고 싶은게 a 모양인데
# b=sample(lst,3)
# print("-- 당첨자 발표 --")
# print("치킨 당첨잠"+str(a))#(어디에서,몇개만큼 뽑는다)
# print("커피 당첨자"+str(b))
# print("--축하합니다--")

# 아 그러네 중복이 안되니까 한번에 4 명을 뽑으면 되네   

from random import *
users=range(1,21)
users=list(users)
shuffle(users)
print(users,type(users))
users=sample(users,4)
print(users)
print("-- 당첨자 발표 --")
print("치킨 당첨잠 {0}".format(users[0]))#(어디에서,몇개만큼 뽑는다)
print("커피 당첨자 {0}".format(users[1:]))
print("--축하합니다--")