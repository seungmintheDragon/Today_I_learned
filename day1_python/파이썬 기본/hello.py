print("안녕하세요.")

string1 = "안녕하세요1"
print(string1)

#python 파일을 실행시키는 가장 기본적인 방법
#python '파이썬파일이름'.py

# "안녕하세요!"를 4번 반복해서 출력하는 코드 작성(while사용)

count = 0 #반복 횟수 세는 변수
print("=============================")
while count < 4: # 반복횟수가 4가 될 때까지
    print(string1)
    count = count + 1  # count+= 1

print("=============================")
# for 에서 단순히 반복만 할떄 사용하는 방법 range() 함수 사용 : 기본적으로 0부터 시작, 주어진 숫자 -1까지
# range(4) : 0, 1, 2, 3 리스트가 아님! 파이썬에는 range라는 타입이 따로 존재
for i in range(4): # 4번 반복
    print(string1)

# module 모듈 : 비슷한 문맥에서 사용되는 함수들을 묶어서 보관(비슷한 기능을 가짐)
# 모듈 사용 1. 함수 포함된 파일을 불러온다(import) 2. 함수를 사용한다