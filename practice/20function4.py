# def profile(name,age,lang1,lang2,lang3,lang4):
#     print("이름:{0}\t 나이 : {1} \t ".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4)
# profile("유재석",20,"java","python","c","c#")
# profile("김태호",25,"kotlin","swift"," "," ")#빈칸 만들어야돼 
# #유재석이 코틀린을 배우면 추가 할려면 함수를 바꿔야돼

def profile(name,age,*language):
    print("이름 : {0}\t 나이: {1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석",20,"java","python","c","c#")
profile("김태호",25,"kotlin","swift")#빈칸 만들어야돼