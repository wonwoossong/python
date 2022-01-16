subway= [10,20,30]
print(subway)

subway= ["유재석","조세호","박명수"]
print(subway) 

# 조세호가 몇번쩨 칸에 타고있는지 
print(subway.index("조세호"))

#하하가 탑승 맨 뒤에 
subway.append("하하")
print(subway)

#사이에 집어넣는다 
subway.insert(1,"정형돈") # insert(인덱스 값, 벨류)
print(subway)

#뒤에서부터 꺼냄 
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명있는지 확인하기ㅏ
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능 
print("정렬줄")
num_list=[5,2,3,1,4,2,]
num_list.sort()
print(num_list)

#뒤집기도 가능 
num_list.reverse()
print(num_list)

#모두 지우고 싶어 
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
num_list=[5,2,3,1,4,2,]
mix_list=["이예은",1,5,True]
#mix_list.sort() 안되네 으쓱..
print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)