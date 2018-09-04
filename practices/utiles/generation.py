
import random

def int_list_generation(ll, hl, len):
    return [random.randint(ll, hl) for i in range(len)]


if __name__=='__main__':
    print(int_list_generation(-10 , 10, 10))