# score_file = open("score.txt","w",encoding="utf8")
# print("수학 : 0",file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file=open("score.txt","a",encoding="utf-8")
# score_file.write("과학:80")
# score_file.write("\n코딩:100")
# score_file.close() 추가 시키는법

#파일 꺼낸는법
# score_file = open("score.txt","r",encoding="utf-8")
# print(score_file.read())
# score_file.close()

#한줄 한줄 불러오는법
# score_file = open("score.txt","r",encoding="utf-8")
# print(score_file.readline())#줄별로 읽기동작 커서 다음줄로
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# #총 몇줄인지 모를때 
# score_file = open("score.txt","r",encoding="utf-8")
# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# #     print(line)
# # score_file.close()

# #리스트에 값을 넣을수도 있따
# score_file = open("score.txt","r",encoding="utf-8")
# lines=score_file.readlines() #리스트 형태로 저장
# for line in lines:
#     print(line)
# score_file.close()