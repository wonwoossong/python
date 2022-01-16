# #출석번호 1 2 3 4 앞에 100을 붙이기로함 
# student=[1,2,3,4,5]
# student=[i+100 for i in student]
# print(student)

# #학생 이름을 길이로 변환
# # students = ["iron man","Thor","i am groot"]
# # students = [len(i) for i in students]
# # print(students)

# #학생이름을 대문자
# students = ["iron man","Thor","i am groot"]
# students = [i.upper() for i in students]
# print(students)






# student=["iron","thor","iamgroot"]
# #학생이름을 길이로 바꾸는법
# student=[len(i) for i in student]
# print(student)



# 조건 1 소요시간 은 5~50 분 사이 랜덤
#조건 2 5~15 분 사이에 승객만 탑승 

#변수가 소요 시간 
from random import * 
passenger=0
for i in range(50):
    time= randrange(5,51)
    i+=1
    if 5<=time<=15:
        print("[0] {0}번쩨 손님 (소요시간 : {1}분)".format(i,time))
        passenger +=1
    else:
        print("[] {0}번쩨 손님 (소요시간 : {1}분)".format(i,time))
print("총 탑승승객 {0}".format(passenger))