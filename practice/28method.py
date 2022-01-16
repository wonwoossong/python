from random import *

class Unit:#부모 class
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(name))
    
    def move(self,location):
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]"\
            .format(self.name,location,self.speed))

    def damaged(self,damage):
        print("{0} 유닛이 {1} 데미지를 입었습니다".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}유닛이 파괴되었습니다".format(self.name))

class attackUnit(Unit):#자식 클래스 
    def __init__(self,name,hp,speed,damage):
        # self.name = name
        # self.hp = hp #상속을 받아서 
        Unit.__init__(self,name,hp,speed)#상속할려고 만들었따.
        self.damage=damage

    def attack(self,location):
        print("{0} 유닛이 {1} 방향으로 공격합니다 공격력은 {2} 입니다"\
            .format(self.name,location,self.damage))

class Marine(attackUnit):
    def __init__(self):
        attackUnit.__init__(self,"마린",40,1,5)
    def stimpack(self):
        if self.hp>10:
            self.hp -= 10
            print("{0} 유닛이 스팀팩을 사용합니다 hp 10 감소".format(self.name))
        else:
            print("{0}체력이 부족하여 스팀팩을 사용할수 없습니다".format(self.name))

class Tank(attackUnit):
    seize_developed = False
    def __init__(self):
        attackUnit.__init__(self,"탱크",150,1,35)
    def set_seize_mode(self):
        self.seize_mode=False
        if Tank.seize_developed==False:
            return
        if self.seize_mode==False:
            print("{0}시즈 모드로 전환합니다".format(self.name))
            self.damage *=2
            self.seize_mode=True
        else:
            print("{0}시즈 모드로 해제합니다".format(self.name))
            self.damage /=2
            self.seize_mode=False

class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} 유닛이 {1}시 방향으로 날아갑니다. 속도{2} "\
        .format(name,location,self.flying_speed))

class FlyableAttackUnit(attackUnit,Flyable):#다중상속 어택유닛,날수있는
    def __init__(self,name,hp,damage,flying_speed):
        attackUnit.__init__(self,name,hp,0,damage)#멤버 변수 초기화
        Flyable.__init__(self,flying_speed)
    def move(self,location):
        self.fly(self.name,location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.clocked = False#클로킹 모드 아닌거

    def clocking(self):
        if self.clocked==True:
            print("{0}: 클로킹 모드 해제합니다".format(self.name))
            self.clocked=False
        else:
            print("{0}: 클로킹 모드 설정합니다".format(self.name))
            self.clocked=True

def game_start():
    print("새로운 게임을 시작합니다")

def game_over():
    print("player:GG")
    print("player 님이 게임에서 퇴장하셨습니다")

game_start()
m1=Marine()
m2=Marine()
m3=Marine()

t1=Tank()
t2=Tank()

w1=Wraith()

#유닛 일괄 관리
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

#전군 이동 
for unit in attack_unit:
    unit.move("1시")

Tank.seize_developed=True
print("탱크 시즈모드 개발이 완료되었습니다")

#공격모드 마린 스팀팩 탱크 시즈모드 레이스 클로킹
for unit in attack_unit:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()
#전군 공격
for unit in attack_unit:
    unit.attack("1시")

#전군 피해
for unit in attack_unit:
    unit.damaged(randint(5,21))

#게임종료
game_over()
