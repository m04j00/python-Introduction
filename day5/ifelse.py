# if else
"""
else 
- if 조건이 맞지 않는 경우 항상 실행
- 반드시 if 뒤에 나와야 함

elif
- else와 if의 결합으로 조건이 맞지 않는 경우 다른 경우를 검사
- 기능의 차이가 아닌 보이는 것의 차이
"""

SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다'
DRAN = '비겼다'
LOSE = '졌다'

mine = '가위'
yours = '바위'

if mine == yours:
    result = DRAN
else :
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else :
            result = WIN
    elif mine == ROCK:
        if yours == PAPER:
            result = LOSE
        else : 
            result = WIN
    elif mine == PAPER:
        if yours == SCISSOR:
            result = LOSE
        else :
            result = WIN
    else :
        print("ERROR")

print(result)
                