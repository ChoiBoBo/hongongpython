# 과제
# 원의 반지름을 사용자로부터 입력받아 둘레와 면접을 구하는 프로그램 작성 후, github 업로드 (circle.py)

# from math import pi

# 사용자 입력값의 반지름 받기
r = float(input())
pi = 3.14
# 그 입력을을 통해 원의 둘레 구하기 // 2 * pi * r
round = 2 * pi * r
# print(round)

# 그 입력을을 통해 원의 면접 구하기 // pi * (r**2)
area = pi * (r ** 2)
print(area)

print("반지름 {}의 원의 둘레는 {}, 면적은 {} 입니다.".format(r, round, area))
