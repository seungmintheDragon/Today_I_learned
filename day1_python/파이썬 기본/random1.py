# random 모듈 불러오기
# 파이썬 파일이름이 겹쳐서 자기자신 불러오게 되었음
# 실행할 파이썬 파일 이름을 모듈의 이름과 겹치게 사용하지 않도록 주의!
import random


# 저녁 메뉴 고민중
menu = ["치킨", "마라탕", "시리얼", "피자", "갈비"]

# 이중에서 랜덤으로 하나를 고르고 싶다.
# random 모듈의 choice라는 함수를 사용해서 리스트 안의 값을 랜더므로 선택
# 모듈안의 함수를 사용하는 방법 ==> 모듈이름.함수이름()
dinner = random.choice(menu)
print(dinner)

# 로또 번호 1 ~ 45 사이의 수를 6개
numbers = range(1,46) # 1부터 시작해서 46 - 1 까지의 범위
# 그 범위중에 6개를 뽑아서 리스트로 만들기
lucky_numbers = random.sample(numbers, 6) # sample(값의 범위, 갯수) ==> 갯수만큼의 크기를 가진 리스트를 반환
# 그 리스트 안의 값의 범위가 numbers가 된다.
print(lucky_numbers) # 6개의 숫자, 범위는 1~45까지의 숫자중 랜덤 선택
print(sorted(lucky_numbers)) # 정렬해서 출력 ==> sorted(정렬대상)
