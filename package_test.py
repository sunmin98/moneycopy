
# 패키지 만들기 실습(package_test.py 파일 및 my_package 패키지 생성 후 실습)
# from 패키지 import 모듈 (ex. from my_package import sum)

from my_package import sum,sub
x=sum.sum_ab(1,2)
print(f"무야호{x}")

y=sub.sub_ab(3,9)
print(f"이애허{y}")

# from 패키지.모듈 import 함수, 클래스 (ex. from my_package.sum import sum_ab)

# __name__ ? => 현재 모듈의 이름을 담고 있는 내장 변수


