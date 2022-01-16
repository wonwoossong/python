from math import trunc
from random import * 

class Unit:
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed=speed
        print("{0}유닛이 {1} 체력으로 {2} 스피드를 가지고 생성되었습니다"\
            .format(self.name,self.hp,self.speed))
    def move(self,location):
        print("{0} 유닛이 {1} 방향으로 {2} 스피드로 이동합니다"\
            .format(self.name,location,self.speed))
    def damaged(self,damaged):
        print("{0} 유닛이 {1} 데미지를 받았습니다".format(self.name,damaged))
        self.hp -= damaged
        print("{0}의 현제 체력은 {1} 입니다".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} 유닛이 파괴되었습니다".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed,damage):
        Unit.__init__(self,name,hp,speed) # 그러면 이름 체력 스피드 정보를 유닛으로부터 받아온다
        self.damage=damage
    def attack(self,location):
        print("{0}유닛이 {1} 시 방향으로 {2}데미지로 공격합니다".format(self.name,location,self.damage))
    
class jogelen(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"jegelen",10,5,3)
    def burrow(self):
        self.burrow=False  
        if self.burrow == True:
            print("저글링이 버로우를 해제합니다 ")
            self.burrow==False
        elif self.burrow == False:
            print("저글링이 버로우 합니다 ")
            self.burrow==True

class hydra(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"hydra",20,4,7)
    def lurk(self):
        self.lurk=False
        if self.lurk == True:
            print("히드라가 럴커를 해제합니다 ")
            self.damage/=2
            self.lurk==False
        elif self.lurk == False:
            print("히드라가 럴커 모드 합니다 ")
            self.damage *=2
            self.lurk==True

class flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} 유닛이 {1}시 방향으로 날아갑니다. 속도{2} "\
        .format(name,location,self.flying_speed))

class flyableAttackunit(AttackUnit,flyable):
    def __init__ (self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage)
        flyable.__init__(self,flying_speed)
    def move(self,location):
        self.fly(self.name,location)

class mutal(flyableAttackunit):
    def __init__(self):
        flyableAttackunit.__init__(self,"뮤탈",30,7,10)

def gamestart():
    print("게임을 시작합니다")

def gamefinish():
    print("good game")
    print("플레이어가 게임을 종료합니다")

j1=jogelen()
j2=jogelen()
j3=jogelen()
j4=jogelen()
j5=jogelen()
j6=jogelen()
h1=hydra()
h2=hydra()
h3=hydra()
m1=mutal()
m2=mutal()
#생성 끝 깔끔!~
#이제 다 같이 움직이게 할래
units=[]
units.append(j1)
units.append(j2)
units.append(j3)
units.append(j4)
units.append(j5)
units.append(j6)
units.append(h1)
units.append(h2)
units.append(h3)
units.append(m1)
units.append(m2)

for unit in units:
    unit.move("1시")



for unit in units:
    if isinstance(unit,jogelen):
        unit.burrow()
    if isinstance(unit,hydra):
        unit.lurk()

for unit in units:
    unit.attack("1시")

for unit in units:
    unit.damaged(randint(1,30))

gamefinish()