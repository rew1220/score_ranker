import math

#표준정규분포 (0,1)
def ND(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-math.pow(x,2)/2)

#정규분포 적분(구분구적법)
def Integ_ND(st):
    sum = 0.0
    for i in range(1000000):
        sum += ND(i/1000+st)/1000
    return sum

#표준정규분포에 활용할 Z점수 획득 함수
def Get_Zscore(x, m, sig):
    return (x - m)/sig


while(True):
    print("=====================================")
    #과목/평균 입력부
    try:
        subj = input("과목 이름을 입력해주세요: ")
        mean = float(input("과목 평균를 입력하세요: "))
        std_div = float(input("표준편차를 입력하세요: "))
    except:
        print("\n정보가 잘못 입력되었습니다.")
        continue



    while(True):
        #점수 입력부
        print("========================================")
        print(f"설정된 과목은 다음과 같습니다.\n과목: {subj}\n평균: {mean}\n표준편차: {std_div}\n'101' 입력시 입력창으로 돌아갑니다.\n\n")
        try:
            score = float(input("점수를 입력하세요: "))
        except:
            print("\n정보가 잘못 입력되었습니다.")
        if(score == 101):
            print("입력창으로 이동합니다.")
            break
        Rscore = round(score)#원점수
        Zscore = Get_Zscore(Rscore, mean, std_div)#Z점수
        rank = Integ_ND(Zscore)*100#상위 %

        print("해당 점수의 정보는 다음과 같습니다.")
        print(f"원점수: {Rscore}")
        print(f"상위{rank:.2f}%")

        if(rank <= 4):print("등급: 1")
        elif(rank <= 11):print("등급: 2")
        elif(rank <= 23):print("등급: 3")
        elif(rank <= 40):print("등급: 4")
        elif(rank <= 60):print("등급: 5")
        elif(rank <= 77):print("등급: 6")
        elif(rank <= 89):print("등급: 7")
        elif(rank <= 96):print("등급: 8")
        else:print("등급: 9")

        if(Rscore >= 80):print("성취도: A")
        elif(Rscore >= 60):print("성취도: B")
        elif(Rscore >= 40):print("성취도: C")
        elif(Rscore >= 20):print("성취도: D")
        else:print("성취도: E")




    