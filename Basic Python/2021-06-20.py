# 모듈 : 부품처럼 만들어진 파일 
import module
module.price(3)
module.price_m(3)
module.price_s(3)

import module as mv # 별명으로 만들어서 호출할 수 있음.
mv.price_s(4)

from module import * # 그냥 사용할 수 있음.
price_m(3)

from module import price, price_m # 어떤 함수만 가져다 쓸 지 정의할 수 있음.
price_m(4)

from module import price_s as ps # 하나의 함수에도 별명을 붙여줄 수 있음.
ps(4)
# 모듈을 불러 올 수 있는 다섯가지 방법



# 패키지 : 모듈들을 모아놓은 집합
import travel.thai # 클래스나 함수는 바로 임포트를 할 수 없다.
trip = travel.thai.ThaiPack()
trip.detail()

from travel.thai import ThaiPack
trip = ThaiPack()
trip.detail()
