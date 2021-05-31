#가변인자
def profile(name, age, *language):
    print(f'이름 : {name}\t나이 : {age}', end=' ') # 엔드 띄어쓰기 하나 넣어주면 줄바꿈없이 출력됨
    for lang in language:
        print(lang, end=' ')
    print()
        
profile('유재석', 20, 'a', 'b', 'c', 'd', 'e')
profile('김태호', 25, 'f', 'e')


#지역변수와 전역변수
gun = 10
def check(sol):
    global gun # 전역공간에 있는 gun을 사용하겠다. 가급적 사용하지 않는게 좋음
    gun = gun - sol
    print(f'남은 총 : {gun}')

def check_ret(gun, sol):
    gun = gun - sol
    return gun

print(f'전체 총 : {gun}')
gun = check_ret(gun, 2)
print(f'남은 총: {gun}')


#퀴즈6

def m_std_wei(wei):
    std_wei = round(wei * wei * 22 / 10000, 2) #라운드는 반올림
    print(std_wei)

def w_std_wei(wei):
    std_wei = round(wei * wei * 21 / 10000, 2)
    print(std_wei)


m_std_wei(175)
w_std_wei(166)



#표준 입출력
import sys
print('a', 'b', sep=',', end='?') #사이에 나올 값을 정해줌
print('a', 'b', file=sys.stderr)# 표준 에러 : 로그처리를 할 때 확인을 해서 프로그램 코드를 수정해야함. 
print('a', 'b', file=sys.stdout) #표준출력

scores = {'수학':0, '영어':50, '코딩':100}
for sub, sco in scores.items():
    print(sub.ljust(3), str(sco).rjust(4), sep=':') #공간확보 및 정렬



for num in range(1, 21):
    print('대기번호 : ' + str(num).zfill(3)) #3크기만큼의 채우는데 빈공간은 0으로

ans = input('안녕? : ') #항상 문자열 형태만 인풋됨
print('입력하신 값은 ' + ans + '입니다.')



#출력포맷
#빈자리는 빈공간으로두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0: >10}'.format(500))
#양수일 땐 +로 표시, 음수일땐 -로 표시
print('{0: >+10}'.format(500))
print('{0: >+10}'.format(-500))
#왼쪽정렬
print('{0:_<+10}'.format(500))
#세자리마다 콤마
print('{0:,}'.format(10000000000))
print('{0:+,}'.format(10000000000))
#세자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
print('{0:_>+30,}'.format(10000000000))
#소수점 출력
print('{0:f}'.format(5/3))
#소수점 특정 자리수까지만 표시 
print('{0:.2f}'.format(5/3))



#파일입출력
score_file = open('score.txt', 'w', encoding='utf8') #쓰기용도
print('안녕', file=score_file)
print('귀요미', file=score_file)
score_file.close()


score_file = open('score.txt', 'a', encoding='utf8') # 원래 있던 파일에 추가하기
score_file.write('반가워')
score_file.write('\n재밌니?')
score_file.close()


score_file = open('score.txt', 'r', encoding='utf8') #읽기
print(score_file.readline(), end='') #줄별로 읽고 커서를 다음줄로 이동
print(score_file.readline(), end='')
print(score_file.readline(), end='')
print(score_file.readline())
score_file.close()


score_file = open('score.txt', 'r', encoding='utf8') #읽기
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end='')
score_file.close()

score_file = open('score.txt', 'r', encoding='utf8') #읽기
lines = score_file.readline() #list 형태로 저장
for line in lines:
    print(line, end='')
score_file.close()