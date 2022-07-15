n = 0
while n < 3:
    print(n)
    n = n + 1 # n의 값을 계속 1씩 증가시키는 명령
print(n) # while의 범위 밖.(들여쓰기가 안되어있음)

# n은 0부터 시작
# n이 10보다 작을때까지 반복
# 반복할 문장 : n을 출력
# n을 2씩 증가시켜

print("================")
n = 0
while n < 10:
    print(n)
    n = n + 2

# alt 누르고 방향키 하면 줄 바뀜

dusts = [59, 24, 102] #리스트   // 리스트 안에 있는 값의 이름을 value라 하고 사용하겠다. // 리스트의 길이만큼 반복
for value in dusts: # ** = > value = 더스트 안에있는 59 24 102
    print(value) # OO 