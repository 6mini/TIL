
#숫자자료형
print(5)
print(-10)
print(3.14)
print(5+3) #8

#문자자료형
print('이윤민')
print("이윤푸") # '와 "의 차이?
print("ㅋㅋㅋㅋㅋ")
print("ㅋ"*5)
 
#boolean
print(5 > 10) #False
print(True) #True
print(not True) #False
print(not 5 > 10) # true

#변수
animal = '강아지' #변수가 너무 쉬워서 놀랬다 그리고 ;를 안붙이는거도 매력이다.
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '에요')
hobby = '공놀이'
print('' + name + '는 ' + str(age) + '살이고, ' + hobby + '을 좋아해요') #정수형 출력할땐 str로 감싸주기
print(name,'는 ',age,'살이고, ',hobby,'을 좋아해요')
print('' + name + '는 어른일까요? ' + str(is_adult) +'')


#quiz1
station = '사당'

print(station + '행 열차가 들어오고 있습니다.')

#연산자
print(1+1)

print(2**3) #2^3 = 8
print(5%3) #나머지 2
print(5//3) #몫 1
print(5/3)

print((3 > 0) and (3 < 5)) #둘다 만족
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)


#수식
print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number += 2
print(number)

number *= 3
print(number) #자바스크립트와 비슷하다.

number %= 5
print(number)


#숫자 처리 함수
print(abs(-5)) #절대값 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) #최대값 12
print(min(5, 12)) #최대값 12
print(round(3.14)) #반올림값

from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4

#랜덤함수

from random import *

print(random()) #0.0 ~ 1.0 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 임의의 값 생성
print(int(random() * 10)) #0 ~ 10 임의의 값 생성

#로또
print(int(random() * 45) + 1) # 1~45 임의값
print(int(random() * 45) + 1) # 1~45 임의값
print(int(random() * 45) + 1) # 1~45 임의값
print(int(random() * 45) + 1) # 1~45 임의값
print(int(random() * 45) + 1) # 1~45 임의값
print(int(random() * 45) + 1) # 1~45 임의값

print(randrange(1, 46)) # 1부터 46 미만의 임의값

print(randint(1,45)) #1이상 45이하


#퀴즈 2
from random import *

study = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 '+ str(study) +'일로 선정되었습니다.') #str을 처음에 안붙임.


#문자열
sentence = '나는 바보입니다.'
print(sentence)
sentence2 = "파이썬은 어려워요."
print(sentence2)
sentence3 = '''
# 나는 바보라서,
# 파이썬은 어려워요.
'''
print(sentence3)

#슬라이싱
jumin = '940926-1234567'

print('성별 : ' + jumin[7])
print('생년 : ' + jumin[:2]) #0번째부터 2번째 직전까지
print('월일 : ' + jumin[2:6])
print('뒷자리 : ' + jumin[7:])
print('뒷자리(뒤에부터) : ' + jumin[-7:])


#문자열 처리함수
python = 'Python is Hard'
print(python.lower()) #모두 소문자로 변환
print(python.upper()) #모두 대문자로 
print(python[0].isupper()) # 첫번째 문자열이 대문자인지? True
print(len(python)) #길이 14
print(python.replace('Python', 'Java'))

index = python.index('n') #문자열이 어디 있는지?
print(index)

print(python.find('n')) #find에서 원하는 값이 없으면 -1 index는 오류를 내버림

print(python.count('n'))#몇번 나오는지? 1


#문자열 포맷
print('a' + 'b')
print('a', 'b')

#방법1
print('나는 %d살입니다.' % 20)  # d 는 정수
print("나는 %s을 좋아해요" % '파이썬') # s는 스트링
print('Apple은 %c로 시작해요' % 'a') # c는 문자 하나

print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))

#방법2
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요.'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요.'.format('파란', '빨간'))

#방법3
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color = '빨간'))

#방법4(v3.6이상)
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')



#탈출문자
print('백문이 불여일견.\n백견이 불여일타.') #줄바꿈
# print('나는 '이윤민'입니다.') #오류
print('나는 \'이윤민\'입니다.') #문장내에서 따옴표처럼 사용가능
print('\\')#하나만 나옴
#\r : 커서를 맨 앞으로 이동
#\b : 한글자 삭제
#\t : 탭

#퀴즈3

site = 'http://naver.com'
my_str = site.replace('http://', '')
my_str = my_str[0:my_str.find('.')]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'

print(f'{site}의 비밀번호는 \'{password}\'입니다.') 


#리스트
sub = [10, 20, 30]

print(sub.index(20))
sub.append(40) #추가

print(sub) #[10, 20, 30, 40]

sub.insert(1, 50) #1번째 위치에 50을 넣겠다.
print(sub) #[10, 50, 20, 30, 40]

sub.pop() #맨뒤를 없앰
print(sub) #[10, 50, 20, 30]
print(sub.count(10))
sub.sort() #정렬
print(sub)
sub.reverse() #뒤집기
print(sub)
print(sub.clear())#없애기

mix = ['이윤민', 28, True]
num = [1,2,3,4,5]

num.extend(mix) #하나의 리스트로 합치기
print(num)


#사전
cab = {
    3 : '유재석',
    100 : '조세호'
}

print(cab[3])
print(cab.get(3))
#print(cab[5]): 오류
print(cab.get(5)) #none
print(cab.get(5, '사용가능')) #사용가능

print(3 in cab) #확인하는 기능 True
cab[37] = '김태호'

del cab[100] #키삭제

print(cab)
print(cab.keys()) #키만 출력
print(cab.values())#벨류만 출력
print(cab.items()) #쌍으로 출력

#튜플
menu = ('돈까스', '치즈까스') #고정된 값
name, age, hobby = '김종국', 20, '헬스'

print(name, hobby)

#세트 집합 : 중복안됨, 순서없음

my_set = {1,2,3,4,4}
print(my_set)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

#교집합
print(java & python) #유재석
print(java.intersection(python))

#합집합
print(java | python) #유재석 김태호 양세형
print(java.union(python))

#차집합
print(java - python) # 양새형 김태호
print(java.difference(python))
python.add('김태호')
print(python) # 추가 가능



#자료구조의 변경
menu = {'커피', '우유', '주스'} #세트로 들어감

menu = list(menu) #세트를 리스트로 바꿈
print(menu)

menu = tuple(menu) #튜플로 바꿈
print(menu) # 소괄호: 튜플 /중괄호: 세트 /대괄호: 리스트


#퀴즈4

from random import *
first = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(first)
chik = sample(first,1)
coff = []
coff += sample(first,3)
print(chik)
print(coff)

print(f'''
 -- 당첨자 발표 -- 
 치킨 당첨자 : {chik} 
 커피 당첨자 : {coff}
 -- 축하합니다 --
''')



from random import *
users = range(1, 21) #1부터 20까지 숫자를 생성
users = list(users)

shuffle(users)

win = sample(users, 4)

print(win)
print(f'''
 -- 당첨자 발표 -- 
 치킨 당첨자 : {win[0]} 
 커피 당첨자 : {win[1:]}
 -- 축하합니다 --
''')



#조건문
weather = input('오늘 날씨는 어때요? ') #입력을 기다림
# if 조건 :
#     실행 명령문

if weather == '비' or weather == '눈':
    print('우산을 챙기세요')
elif weather == '미세먼지':
    print('마스크를 챙기세요')
else:
    print('필요없음.')



temp = int(input('기온이 어때요? ')) #숫자열로바꿔줌
if 30 <= temp:
    print('넘나 더워.')
elif 10 <= temp and temp < 30:
    print('딱 좋음.')
elif 0 <= temp <10:
    print('외투 필요.')
else:
    print('넘나 추운것.')



#반복문 for문

for wait in range(1,101):
    print(f'대기번호 : {wait}')



sb = ['아이언맨', '토르', '그루트']
for custom in sb:
    print(f'{custom}님 커피 준비 됐어영')


#while문

customer = '6mini'
index = 5
while index >= 1:
    print(f'{customer}님, 커피 준 완. {index}번 남음.')
    index -= 1
    if index == 0:
        print('커피 버림.')



#컨티뉴와 브레이크

absent = [2, 5] #결석
noBook = [7]
for student in range(1,10):
    if student in absent:
        continue #해당자 빼고 진행
    elif student in noBook:
        print(f'오늘수업 끝. {student}는 교무실로 따라와.')
        break #바로 반복문 끝
    print(f'{student}, 안녕')


#한줄 포문
student = range(1,6)
student = list(student)
student = [i+100 for i in student] #어렵다
print(student)

student = ['ironman', 'thor', 'groot']
student = [len(i) for i in student]
print(student)


# 퀴즈5
from random import *

cont = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print(f'[O] {i}번째 손님 (소요시간 : {time}분')
        cont += 1
    else:
        print(f'[ ] {i}번째 손님 (소요시간 : {time}분')

print(f'총 탑승 승객 : {cont}명')


#함수
def open():
    print('hello')

open()

def deposit(bal, mon):
    print(f'입금완료. 잔액은 {bal+mon}원 입니다.')
    return bal + mon #여기서 리턴을 왜하는지? = bal의 값을 변경

def withdraw_night(bal, mon):
    com = 100
    return com, bal - mon - com

bal = 0
bal = deposit(bal, 1000)
com, bal = withdraw_night(bal, 500)
print(f'수수료는 {com}이며, 잔액은 {bal}입니다.')



#기본값
def profile(name, age, leng):
    print(f'이름 : {name}, 나이 : {age}, 언어 : {leng}')

profile('유재석', 20, '파이썬')

def profile(name, age = 17, leng = '파이썬'):
    print(f'이름 : {name}, 나이 : {age}, 언어 : {leng}')

profile('유재석')



#키워드 값을 이용한 함수 호출
def profile(name, age, leng):
    print(f'이름 : {name}, 나이 : {age}, 언어 : {leng}')

profile(
    name='귀여워',
    leng='파이썬',
    age=20
)

#가변인자를 이용한 함수 호출
 