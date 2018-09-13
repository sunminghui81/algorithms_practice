
from practices.utiles.generation import int_list_generation

given_list = int_list_generation(0, 100, 20)

'''
level 0           list[0]
                 /     \
level 1        list[1]  list[2]
.
.
.
'''



class Heap(object):
    def __init__(self, list):
        self.list = list

    def get_level_tree(self, n):
        ''' return specify level trees'''
        trees = []
        ln = self.get_level_index(n)
        lnn = self.get_level_index(n +1)
        for i in range(int((len(lnn) +1) / 2)):
            tree = (ln[i], lnn[2 * i], lnn[2 * i + 1]) if len(lnn) > 2 * i + 1 else  (ln[i], lnn[2 * i])
            trees.append(tree)
        return trees

    def get_level_index(self, n):
        ''' :return specify level list indexs as a list'''
        lindex = []
        for i in range(pow(2, n)):
            index = pow(2, n) - 1 + i
            if len(self.list) > index:
                lindex.append(index)
        return lindex



class MaxHeapIfy(Heap):
    def __init__(self, list):
        super(MaxHeapIfy, self).__init__(list)

    def exchange_tree(self, root, l, r):
        if root < l:
            root, l = l, root
        if root < r:
            root, r = r, root
        return root, l, r



    def do(self):
        pass

    def __call__(self):
        return  self.do()


if __name__ == '__main__':
    mhi = MaxHeapIfy(given_list)
    print(mhi.get_level_index(5))
    print(mhi.get_level_tree(3))