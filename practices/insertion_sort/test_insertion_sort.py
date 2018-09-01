
from practices.insertion_sort.insertion_sort import *


B = (34, 45, 23, 12, 31, 23, 64, 46, 2, 5)


def test_insertion_low():
    assert insertion_sort_low(B) == sorted(B)

def test_insertion_high():
    A = sorted(B)
    print(A)
    A.reverse()
    print(A)
    assert insertion_sort_high(B) == A