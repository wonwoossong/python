kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","orange"]

print(list(zip(kor,eng)))#리스트 두개를 합친다 세로로 

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))#합친것을 푸는법 첫번쩨꺼 끼리 두번쩨꺼 끼리

kor2,eng2=zip(*mixed)
print(kor2)
print(eng2)