#!/usr/bins/env python3
# -*- coding utf-8 -*-

import jieba
from collections import Iterable
def hanoi(n, a="A", b="B", c="C"):
    if n == 1:
        print(a+" --> "+c)
    else:
        hanoi(n-1, a, c, b)
        print(a+" --> "+c)
        hanoi(n-1, b, a, c)


#hanoi(0)
L1= list(range(2))
#print(L1)
#print(L1)
#if isinstance("asdfasdf",Iterable):
#    print(isinstance("asdfasdf",Iterable))
for i, v in enumerate([1,"asdf",4,"eee"]):
    print(i,v)

list1 =[m+n+o for m in "abc" for n in "abc" for o in "abc" if m!=n and m!=o and n!=o]
print(list1)

generator1 = (x*x for x in range(0,10))

for i in generator1:
    print(i)


def triangles1():  # for 循环
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

def triangles():  # 列表生成式
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n = 0
results = []
for t in triangles1():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [[1],[1, 1],[1, 2, 1],[1, 3, 3, 1],[1, 4, 6, 4, 1],[1, 5, 10, 10, 5, 1],[1, 6, 15, 20, 15, 6, 1],[1, 7, 21, 35, 35, 21, 7, 1],[1, 8, 28, 56, 70, 56, 28, 8, 1],[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
    print('测试通过!')
else:
    print('测试失败!')
