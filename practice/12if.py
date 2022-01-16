# weather=input("오늘 날씨는 어때요?")
# #if 조건:
#     #실행 명령문

# if weather=="rain" or "snow":
#     print("우산을 챙기세요")
# elif weather=="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물이 필요없어요")


temp =int(input("기온이 어때요?"))
if temp>= 30:
    print("더워요")
elif 10<= temp <30:
    print("날씨가 좋아요")
elif 0<= temp <10:
    print("추운 날씨에요")
else:
    print("추워요 나가지 마세요 ")