#표준 입출력 
print("Python","java",sep=",")
print("Python","java",sep=" vs ")
print("Python","java","c",sep=" vs ")

print("Python","java",sep="," ,end=" ? ")
print("무엇이 더 재미있을까요?")

import sys
print("Python","java",file=sys.stdout)#standard out
print("Python","java",file=sys.stderr)#standard error

scores= {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():#items 하면 키와 벨류 둘다 그러면 키가 서브젝 벨류가 스코어로 들간다 
    print(subject.ljust(8), str(score).rjust(4), sep=":")#오른쪽 왼쪽 정렬

# 은행 대기순번표
#001, 002, 003 101 102 103 
for num in range(1,21):
    print("대기번호: "+str(num).zfill(3))

#표준 입력
answer = input("아무 값이나 입력하세요:")#사용자 입력에 의해서 받게되면 
print(type(answer))                    # 항상 문자 형태로 받게된다 
print("입력하신 값은"+answer+"입니다")