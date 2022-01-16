# import pickle

# with open("profile.pickle","rb") as profile_file: # 이 파일을 열어서 profile_file 에 저장
#     print(pickle.load(profile_file))#profile_file 을 불러온다 

#with 는 자동으로 클로즈

# with open("study.txt","w",encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","r",encoding="utf-8") as study_file:
#     print(study_file.read())


for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf-8") as report_file:
        report_file.write("#부서 :\n #이름: \n #업무 요약: \n")
