class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Flyable, Unit): # 먼저 오는 유닛
    def __init__(self):
        super().__init__()