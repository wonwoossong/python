#단어가 있고 뜻이 있는 사전처럼 
cabinet={3:"송원우",100:"이예은"} #{키:벨류}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 또 다른 방법 값을 가져오는 
# print(cabinet[6]) error
print(cabinet.get(5))#--> none
print(cabinet.get(5,"사용가능"))

print(3 in cabinet)#캐비넷에 있으면 true 없으면 false
print(5 in cabinet)

print(cabinet)
cabinet[3]="정민우"#값 업데이트 가능 
cabinet[20]="박정은"
print(cabinet)
# 딜리트
del cabinet[3]
print(cabinet)

#key 만 출력
print(cabinet.keys())

#value 만 출력
print(cabinet.values())

#둘다 출력 하고 싶어
print(cabinet.items())

#다 지우기
cabinet.clear()
print(cabinet)