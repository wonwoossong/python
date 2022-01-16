# def profile(name,age,main_lang):
#     print("이름:{0}\t 나이 : {1} \t 주 사용 언어: {2}"\
#         .format(name,age,main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

#같은 학교 같은 학년 같은반 같은수업.
#기본 값 사용된다

def profile(name,age=17,main_lang="파이썬"):
    print("이름:{0}\t 나이 : {1} \t 주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile("송원우")
profile("이예은")
profile("송원우",26)
profile("이예은",23,"자바")