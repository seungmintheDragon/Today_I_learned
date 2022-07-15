#elif

# if 만약 ㅇㅇ 라면
# ㅁㅁ 해줘
# elif 만약 ㅇㅇ가 아니라 00라면
# 00해줘
# else 그게 아니라면
# ㅇㅇ 해줘

dust = 79

if dust > 70:
    print("미세먼지 농도는 70보다 크다.")
elif dust > 50: #dust가 70보다 크지 않을때 조건 검사
    print("미세먼지 농도는 50보다 크다.")
else:
    print("미세먼지 농도는 50보다 작거나 같다.")

#dust 변수에 들어있는 값을 기준으로 미세먼지 정보출력
#dust가 150보다 작다 : 매우나쁨
#dust가 80보다 크고 150이하이다 : 나쁨
#dust가 30보다 크고 80이하이다: 보통
#dust가 30이하이다: 좋음
#dust는 150보다 작은 수라고 가정

dust = 120

if dust > 150:
    print("미세먼지 : 매우나쁨")
elif 150 >= dust > 80:
    print("미세먼지 : 나쁨")
elif dust > 30 and dust <= 80:
    print("미세먼지 : 보통")
else:
    print("미세먼지 : 좋음")