class Unit:#부모 class
    def __init__(self,name,hp,speed):
        self.name=name
        self.hp=hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(name))
    
    def move(self,location):
        print("지상 유닛 이동")
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]"\
            .format(self.name,location,self.speed))
    def damaged(self,damage):
        print("{0} 유닛이 {1} 데미지를 입었습니다".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name,self.hp))
        if self.hp<=0:
            print("{0}유닛이 파괴되었습니다".format(self.name))
#self.name , self.hp 겹쳐 
#상속을 사용 
class attackUnit(Unit):#자식 클래스 
    def __init__(self,name,hp,speed,damage):
        # self.name = name
        # self.hp = hp
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
        attackUnit.__init__(self,"탱크",150,1,35)\

    
    def set_seize_mode(self):
        self.seize_mode=False
        if Tank.seize_developed==False:
            return
        if self.seize_mode==False:
            print("{0}시즈 모드로 전환합니다".format(self.name))
            self.damage *=2
            self.seize_mode==True
        else:
            print("{0}시즈 모드로 해제합니다".format(self.name))
            self.damage /=2
            self.seize_mode==False

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
        print("[공중 유닛 이동]")
        self.fly(self.name,location)

#문제 지상유닛 무브 공중 fly so we have to check everytime 

#건물  패스의 효용
# class BuildingUnit(Unit):
#     def __init__(self,name,hp,location):
#         pass#이 함수는 일단은 완성된것처럼 보여준다 

# supply_depot = BuildingUnit("서플라이디폿",500,"7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     pass#아무것도 안하고 지나가는것 

# game_start()
# game_over()

class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)#슈퍼를 쓸때는 () 그리고 self 없다
        self.location=location#다중 상속할때 문제가 생긴다 