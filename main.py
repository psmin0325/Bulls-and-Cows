def bulls_cows(num, user): # bulls and cows 로직 구현
    res = [0, 0]
    num = str(num)
    user = str(user)

    if num == user:
        res = [4, 0]
        return res
    
    for i in range(len(num)):
        if num[i] == user[i]:
            res[0] += 1
            continue
        if user[i] in num:
            res[1] += 1
    return res

    # return list type [b_score, c_score]

def result(res): # 결과를 출력해주는 함수
    b, c = res
    print(f'{b}B {c}C')

import random

if __name__ == "__main__": # 난수 생성, 사용자 입력받아 위의 함수들을 사용
    temp = [i for i in range(10)]
    n = random.sample(temp, 4)
    n = ''.join(list(map(str, n)))
    
    while True:
        user = input()
        if len(set(list(map(int, list(user))))) != 4:
            print('중복된 숫자가 있습니다.')
            continue
        result(bulls_cows(n, user))
        if n == user:
            break
