
from practices.utiles.consuming import consuming

def insertion_sort_low(l):
    L = [l[0]]
    for n in l[1:]:
        for i, m in enumerate(L):
            if n <= m:
                L = L[:i] +[n] + L[i:]
                break
        else:
            L =  L +[n]
    return L


@consuming
def insertion_sort_high(l):
    L = [l[0]]
    for n in l[1:]:
        for i, m in enumerate(L):
            if n > m:
                L = L[:i] + [n] + L[i:]
                break
        else:
            L =  L + [n]
    return L

if __name__=='__main__':
    B = (34, 45, 23, 12, 31, 23, 64, 46, 2, 5)
    print(insertion_sort_high(B))