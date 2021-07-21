#pickle 프로그램상에서 사용하는 것을 파일 형태로 저장하는 것
import pickle
# profile_file = open('profile.pickle', 'wb')#쓰기목적 + 바이너리 : 피클을 쓰기 위해서
# profil = {'1':'a', '2':'b', '3':['c','d','e']}
# print(profil)
# pickle.dump(profil, profile_file) #프로필에 있는 정보를 파일에 저장
# profile_file.close()

profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file)
print(profile)
profile_file.close()



#with
import pickle

with open('profile.pickle', 'rb') as profile_file: #종료를 할 필요 없이 불러와준다.
    print(pickle.load(profile_file))

# with open('study.txt', 'w', encoding='utf8') as study_file:
#     study_file.write('안녕')

with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())



#퀴즈7
for bogo in range(1, 51):
    with open(f'{bogo}주차.txt', 'w', encoding='utf8') as bogoseo:
        bogoseo.write(f'- {bogo}주차 주간보고 -')
        bogoseo.write('\n부서 : ')
        bogoseo.write('\n이름 : ')
        bogoseo.write('\n업무 요약 : ') 



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



class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f'{self.name} 유닛이 생성되었습니다.\n체력은 {self.hp}, 공격력은 {self.damage}입니다.')

marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)