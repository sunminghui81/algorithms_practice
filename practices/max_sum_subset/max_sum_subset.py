
from practices.utiles.consuming import consuming
from practices.utiles.generation import int_list_generation

def max_sum_subset(l):
    if len(l) == 1:
        return l[0]
    return max([max_sum_subset(l[:int(len(l)/2)]), mid_max(l), max_sum_subset(l[int(len(l)/2):])])


def mid_max(l):
    mi = 0
    if len(l) > 2:
        mi = int(len(l) / 2)
    sum_l = -1000000000
    s = 0
    for i in reversed(l[:mi]):
        s += i
        sum_l = s if sum_l < s else sum_l
    sum_h = -1000000000
    s = 0
    for i in l[mi:]:
        s += i
        sum_h = s if sum_h < s else sum_h
    return sum_h if sum_l < 0 else sum_h + sum_l

@consuming
def max_subset_sum(l, h, n):
    L = int_list_generation(l, h, n)
    print(L)
    print('---', max_sum_subset(L))



if __name__=='__main__':
    max_subset_sum(-10, 10, 10)