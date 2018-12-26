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
    el = [l[0]]
    for i in l[1:]:
        tag = False
        # t = i
        for e in range(1, len(l)):
            if i >= el[e]:
                t = el[e + 1]
                el[e + 1] = i

            else:
                t = i
        print(el)

    return el


def quick_sort(l):
    if len(l) <= 1:
        return l
    half = l[len(l) // 2]
    left_list = []
    right_list = []
    mm = []
    for count in range(len(l)):
        if l[count] < half:
            left_list.append(l[count])
        elif l[count] == half:
            mm.append(l[count])
        else:
            right_list.append(l[count])
    l = quick_sort(left_list) + mm + quick_sort(right_list)
    return l


# def my_sort(l):
#     max_item = 0
#     for i in l:
#         if i >= max_item:
#             max_item = i
#     ml = [i for i in range(max_item)]
#     for i in l:

def walk(m):
    return walk(m - 1) + walk(m - 2) if m > 2 else 1 if m == 1 else 2
    # return walk(m - 1) + walk(m - 2)


def inertsort(l):
    N = len(l)
    for x in range(1, N):
        print(l)
        a, b = x, x
        n = l[x]
        while n < l[a - 1] and a - 1 >= 0:
            a = a - 1
            if a - 1 < 0:
                a = 0
        while b > a:
            l[b] = l[b - 1]
            b = b - 1
        l[a] = n

def select_sort(l):
    return


if __name__ == '__main__':
    l = [i for i in range(60)]
    random.shuffle(l)
    print(l)
    st = time.time()

    # sort_l = bubble_sort(l)
    # sort_l = quick_sort(l + l)
    # sort_l = insert_sort(l)
    sort_l = inertsort([3,4,5,5,2,1])
    # sort_l = walk(4)

    print(sort_l)
    print(time.time() - st)


