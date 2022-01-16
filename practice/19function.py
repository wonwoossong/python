def profile(name,age,main_lang):
    print("이름:{0}\t 나이 : {1} \t 주 사용 언어: {2}"\
        .format(name,age,main_lang))     
profile(name="유재석",main_lang="파이썬",age=25)
profile(main_lang="자바",age=12,name="김태호")

#키워드값 입력하면 자리 바꿔도 상관없다