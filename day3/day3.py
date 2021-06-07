# 숫자
my_age = 18  # 변수에 숫자 넣기
my_next_age = my_age + 1  # 더하기
multiply = 9 * 9  # 곱하기
divide = 30 / 5  # 나누기
power = 2 ** 10  # 거듭제곱
remainder = 15 % 4  # 나머지

print(my_age, "살")
print("내년에는", my_next_age, "살")
print(multiply, divide, power, remainder)

#문자열 : 따옴표
my_name = 'LeeMJ'
text = '2021' + '2004'  # 텍스트는 더하기만 가능
print("내 이름은", my_name)
print(text)

# 실습 1

a = 33
b = 3

summation = a + b
multiply = a * b
divide = a / b
remainder = a % b
power = a ** b

print("summation은 {}입니다.".format(summation))
print("multiply는 {}입니다.".format(multiply))
print("divide는 {}입니다.".format(divide))
print("remainder는 {}입니다.".format(remainder))
print("power는 {}입니다.".format(power))

# 실습 2

birth_year='2004'
birth_date='0702'
year_and_date = birth_year + birth_date

print("year_and_date : {}".format(year_and_date))