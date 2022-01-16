#집합
#중복안됨,순서없음
my_set={1,2,3,3,3} # {} 사전이랑 같은데 키 벨류가 없어 셋에는   
print(my_set)#-->1,2,3, 만 출력

java={"유재석","김태호","조세호"} # 데이터 타입이 set 이네 
python=set(["유재석","박명수"])
print(type(java))

#교집합 자바 파이썬 모두할수있는사람
print(java & python)
print(java.intersection(python))

#합집합도 가능
print(java | python)
print(java.union(python))

#차집합 (java 할수있찌만 파이선 할수 없는 개발자)
print(java-python)
print(java.difference(python))

#python 을 할수 있는 사람이 늘어남 
python.add("김태호")
print(python)

#java 를 까먹음
java.remove("김태호")
print(java)

