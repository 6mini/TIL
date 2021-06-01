#클래스 : 파이선 코딩에서 중요함
name = '마린'
hp = 40
damage = 5

print(f'{name} 유닛이 생성되었습니다.\n체력은 {hp}, 공격력은 {damage}입니다.')

t_name = '탱크'
t_hp = 150
t_damage = 35

print(f'{t_name} 유닛이 생성되었습니다.\n체력은 {t_hp}, 공격력은 {t_damage}입니다.')

def attack(name, lacation, damage):
    print(f'{name} : {lacation} 방향으로 적군을 공격합니다. [공격력 {damage}]')

attack(name, '1시', damage)
attack(t_name, '1시', t_damage)


'''
marine1 = Unit('마린', 40, 5) #유닛의 인스턴스 객체
marine2 = Unit('마린', 40, 5) #인자를 다 넣지 않으면 작동이 안댐
tank = Unit('탱크', 150, 35)

wraith1 = Unit('레이스', 80, 5)
print(f'{wraith1.name},{wraith1.hp}') #외부에서도 사용가능함.

wraith1.cloking = True
if wraith1 == True:
    print('안녕') #클래스 외부에서 변수를 확장할 수도 있음. 확장을 한 변수에만 할당이 됨.
'''

class Unit: #일반유닛
    def __init__(self, name, hp, speed): # init : 생성자 셀프를 제외하고 값을 던져줘야함.
        self.name = name # 멤버변수
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print(f'{self.name} : {location}으로 이동합니다. 속도 : {self.speed}')



class AttackUnit(Unit): #공격유닛 , 괄호가 되면 그냥 유닛에게 상속받음
    def __init__(self, name, hp, speed, damage): # init : 생성자 셀프를 제외하고 값을 던져줘야함.
        Unit.__init__(self, name, hp, speed) #상속
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.\n체력은 {self.hp}, 공격력은 {self.damage}입니다.')

    def attack(self, location):
        print(f'{self.name} : {location}방향으로 공격합니다. [공격력{self.damage}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 만큼의 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp}입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 죽었습니다.')

class Flyable:
    def __init__(self, fly_speed):
        self.fly_speed = fly_speed

    def fly(self, name, location):
        print(f'{name} : {location}으로 날아갑니다. [속도 : {self.fly_speed}]')

class FlyableAttackUnit(AttackUnit, Flyable): #다중상속받음
    def __init__(self, name, hp, damage, fly_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, fly_speed)

    def move(self, location): #지상유닛에 무브가 쓰였지만 재정의를 하면 여기 안에서 상속받은 함수만 사용됨.
        print('[공중 유닛 이동]')
        print(f'{self.name} : {location}으로 이동합니다. 속도 : {self.fly_speed}')

class BuildingUnit(Unit):
    def __init__(self, name, hp, speed):
        super().__init__(name, hp, speed)

vul = AttackUnit('벌쳐', 80, 10, 20)
bc = FlyableAttackUnit('배틀크루저', 500, 25, 3)

#메소드 오버라이딩
vul.move('11시')
bc.fly(bc.name, '11시')
bc.move('9시')



firebat1 = AttackUnit('파이어뱃', 50, 16)
firebat1.attack('5시')

firebat1.damaged(25)
firebat1.damaged(25)



#pass : 함수에서 그냥 넘어갈수있음. 완성할수있음.