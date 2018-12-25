import random

import time


def bubble_sort(l):
    print(l)
    for c in range(len(l)):
        count = 0
        for i in range(len(l) - c - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                count += 1
        print(c, count, l)
        if count == 0:
            return l
    return l


def insert_sort(l):
    print(l)
    el = []
    for i in l:
        tag = False
        for e in range(len(el)):
            if el[e] < i:
                tag = True
                tmp = el[e]
                el[e] = i
            # if tag:


def select_sort(l):
    return


if __name__ == '__main__':
    l = [i for i in range(3000)]
    random.shuffle(l)
    st = time.time()

    sort_l = bubble_sort(l)

    print(time.time() - st)
