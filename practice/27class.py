# #class 는 중요한 개념이다
# #마린 : 공격 유닛 , 군인 총을 쏜다
# name = "marin"
# hp = 40
# damage = 5

# print("{}유닛이 생성되었습니다".format(name))
# print("체력 {0} 공격력 {1}".format(hp,damage))

# tank_name="tank"
# tank_hp=150
# tank_damage=35

# print("{}유닛이 생성되었습니다".format(tank_name))
# print("체력 {0} 공격력 {1}".format(tank_hp,tank_damage))

# tank2_name="tank"
# tank2_hp=150
# tank2_damage=35

# print("{}유닛이 생성되었습니다".format(tank2_name))
# print("체력 {0} 공격력 {1}".format(tank2_hp,tank2_damage))


# def attack(name, location, damage):
#     print("{0} : {1} 방햑으로 적군을 공격합니다 공격력은 {2} 입니다"\
#         .format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)
# attack(tank2_name,"1시",tank2_damage)
#만약에 유닛이 수십가지인데 그러면 힘들자나 그래서 클래스가 필요 
#하나의 틀이라고 보면 된다 연관되어 있는 변수라 함수의 관계라고 보면된다

class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("hp: {0} damage: {1} ".format(self.hp,self.damage))

# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)
#하나의 클래스를 통해서 마린이랑 탱크 생성했다 
#__init__ : 마린 3 을 만들때 init 변수랑 (self 제외하고) 똑같은 갯수가 들어가야된다
#멤버 변수 class 안에 
#self.name/self.damage/self.hp 가 있다
wraith1=Unit("레이스",80,5)#클로킹 기능하고싶다 
print("유닛이름 : {0} 공격력 {1} ".format(wraith1.name,wraith1.damage))

wraith2=Unit("레이스",80,5)#클로킹 기능하고싶다 
wraith2.clocking =True
if wraith2.clocking == True:
    print("{0} 는 현제 클로킹 상태입니다".format(wraith2.name))

# if wraith1.clocking == True:
#     print("{0} 는 현제 클로킹 상태입니다".format(wraith1.name)) # error 
#이처럼 clocking 이라는 기능을 클래스 외부에서 원하는  변수를 확장할수는 있지만 확장된 변수는
#확장을 한 객체에서만 적용된다 ex)wraith2.clocking