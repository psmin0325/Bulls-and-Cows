import random 


def get_digits(num):
    return [int(i) for i in str(num)]

#중복 확인
def check_duplicates(num):
    num_list = get_digits(num)
    if len(num_list) == len(set(num_list)):
        return True
    else:
        return False
     
def generate_num():
    while True:
        num = random.randint(1000,9999)
        if check_duplicates(num):
            return num
