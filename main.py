#<<<<<<< main
import generate_rand_num
def bulls_cows(usr_input): # bulls and cows 로직 구현
#>>>>>>> main
    pass
    # return list type [b_score, c_score]

def result(res): # 결과를 출력해주는 함수
    b, c = res
    print(f'{b}B{c}C')


if __name__ == "__main__": # 난수 생성, 사용자 입력받아 위의 함수들을 사용

    #<<<<<<< main
    # random
    num = generate_rand_num
    print(num)
    # user.input()
    #=======
    #answer = rand
    while(True):
        user_input = input("insert number : ")
        if (bulls_cows(user_input)):
            break
    #>>>>>>> main
