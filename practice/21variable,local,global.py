# gun=10#전역변수

# def checkpoint(soldier):#경계근무
#     # gun = 20 #지역변수
#     global gun#전역 공간에 있는 gun 을 사용할 것이다 
#     gun=gun-soldier
#     print("함수 내 남은 총 :{0}".format(gun))
# def checkpoint_return(gun,soldier):
#     gun= gun-soldier
#     print("함수 내 남은 총 :{0}".format(gun))
#     return gun # 바뀐 값을 밖으로 던질수가 있어서 첫번쪠 줄에 있는 gun 의 값이 변한다 
# print("전체 총의 수 {0}".format(gun))
# # checkpoint(2)
# gun=checkpoint_return(gun,2)# 전역 변수 건을 이 함수 안으로 넣어주는 라인 
# print("남은 총 : {0}".format(gun))

def std_weight(gender,height):
    if gender =="남자":
        avg_weight=height*height/10000*22
        print("키 {0}의 남자의 표준 체중은 {1} 입니다".format(height,round(avg_weight,2)))
    else:
        avg_weight=height*height/10000*21
        print("키 {0}의 여자의 표준 체중은 {1} 입니다".format(height,round(avg_weight,2)))

std_weight("여자",162)