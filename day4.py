# if문
"""
구조 
1. if 예악어 : 조건문의 시작
2. 조건 : 참 / 거짓을 판단할 수 있는 조건
3. : 조건이 끝났음을 표현하는 명령
4. :실행하고자 하는 코드, 탭키를 이용해 틀여씀
"""

people = 3
apple = 20

if people < apple / 5:
    print("사과 배터지게 먹자@@!@!")
if apple % apple > 0 :
    print("사과가 적어!!!!!!")
if people > apple:
    print("사람이 너무 많아@!@!@!@!!")

if True:
    print("조건식이 True이면 실행됩니다.")
if False :
    print("조건식이 False이면 실행되지 않습니다.")


# 조건식

# 1. 조건
print(10 > 5) # 크다
print(10 <= 5) # 크거나 같다
print(10 == 5) # 같다
print(10 != 5) # 같지 않다.
# True 또는 False 출력

# 2. boolean 연산

a = 22
if 20 <= a and a < 30:
    print("20대입니다.")

a = 65
if a < 18 or 60 <= a:
    print("18세 미만 또는 60세 이상입니다.")