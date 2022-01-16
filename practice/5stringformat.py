print("a"+"b")
print("a","b")

# 방법 1
print("나는 %d살 입니다"% 20)#d는 정수를 의미
print("나는 %s을 좋아해요"% "파이썬")#s 는 string
print("Apple 은 %c로 시작해요"%"A")#c는 캐릭터 1 글자 의미

#%s 는 쓰면 다 가능 ~ 
print("나는 %s살 입니다"% 20)#d는 정수를 의미
print("나는 %s을 좋아해요"% "파이썬")#s 는 string
print("Apple 은 %s로 시작해요"%"A")#c는 캐릭터 1 글자 의미

print("나는 %s 색과 %s 색을 좋아해요"%("파란", "빨간"))

#방법2 
print("나는 {}살 입니다".format(20))
print("나는 {0} 색과 {1} 색을 좋아해요".format("파란", "빨간"))

#방법3
print("나는 {age}살이며 {color}색을 좋아해요".format(age=20,color="red"))

#방법4
age=20
color="red"
print(f"나는 {age}살이며 {color}색을 좋아해요")