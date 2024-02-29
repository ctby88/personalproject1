import random
# 기본 자료 구성
# 입력값 정합 판단
# 승패 판단
# 통계 제시
# 계속 여부 확인
# 시작, 중단



li = ['가위', '바위', '보']
di = {'승' : 0, '무' : 0, '패' : 0}
c=''

while c != 'n' and c != 'N':
    a = random.choice(li)
    b = input("가위, 바위, 보 셋 중 하나를 입력하세요.")
    while b not in li:
        print("잘못 입력하셨습니다. 형식에 맞게 입력해보세요.")
        b = input("가위, 바위, 보 셋 중 하나를 입력하세요.")

    if a == b:
        di['무']+=1
        print("비겼습니다")
        print(f"승 {di['승']} 무 {di['무']} 패 {di['패']}")
        c = input("한판 더 해보시겠어요? (Y/N)")
        while c not in ['y', 'Y', 'n', 'N']:
            c = input("(Y/N)으로 대답해주세요")
        if c == 'y' or c == 'Y':
            print("이번 판도 잘 해봅시다!")
        else:
            print("다음에 또 봐요")
    elif a == '가위' and b =='보':
        di['패']+=1
        print("졌습니다")
        print(f"승 {di['승']} 무 {di['무']} 패 {di['패']}")
        c = input("한판 더 해보시겠어요? (Y/N)")
        while c not in ['y', 'Y', 'n', 'N']:
            c = input("(Y/N)으로 대답해주세요")
        if c == 'y' or c == 'Y':
            print("이번 판도 잘 해봅시다!")
        else:
            print("다음에 또 봐요")
    elif a == '바위' and b == '가위':
        di['패']+=1
        print("졌습니다")
        print(f"승 {di['승']} 무 {di['무']} 패 {di['패']}")
        c = input("한판 더 해보시겠어요? (Y/N)")
        while c not in ['y', 'Y', 'n', 'N']:
            c = input("(Y/N)으로 대답해주세요")
        if c == 'y' or c == 'Y':
            print("이번 판도 잘 해봅시다!")
        else:
            print("다음에 또 봐요")
    elif a == '보' and b == '바위':
        di['패']+=1
        print("졌습니다")
        print(f"승 {di['승']} 무 {di['무']} 패 {di['패']}")
        c = input("한판 더 해보시겠어요? (Y/N)")
        while c not in ['y', 'Y', 'n', 'N']:
            c = input("(Y/N)으로 대답해주세요")
        if c == 'y' or c == 'Y':
            print("이번 판도 잘 해봅시다!")
        else:
            print("다음에 또 봐요")
    else:
        di['승']+=1
        print("이기셨네요!")
        print(f"승 {di['승']} 무 {di['무']} 패 {di['패']}")
        c = input("한판 더 해보시겠어요? (Y/N)")
        while c not in ['y', 'Y', 'n', 'N']:
            c = input("(Y/N)으로 대답해주세요")
        if c == 'y' or c == 'Y':
            print("이번 판도 잘 해봅시다!")
        else:
            print("다음에 또 봐요")            

