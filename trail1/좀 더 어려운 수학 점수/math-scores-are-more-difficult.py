# 영어점수 상관없이 수학점수가 높음 : 수학점수가 더 높은 학생의 이름을 출력
#                  수학점수가 같음 : 영어 점수가 더 높은 학생의 이름 출력

a_math, a_eng = map(int, input().split())               
b_math, b_eng = map(int, input().split())

if a_math > b_math:
    print("A")

elif a_math == b_math:
    if a_eng > b_eng:
        print("A")
    else:
        print("B")

else:
    print("B")